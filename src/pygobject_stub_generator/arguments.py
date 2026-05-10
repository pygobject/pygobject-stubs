from __future__ import annotations

from typing import Final
from typing import TYPE_CHECKING
from typing_extensions import Self

from dataclasses import dataclass

import gi._gi as GI

if TYPE_CHECKING:
    from collections.abc import Iterator

FROM_PYTHON: Final = frozenset({GI.Direction.IN, GI.Direction.INOUT})
TO_PYTHON: Final = frozenset({GI.Direction.OUT, GI.Direction.INOUT})


@dataclass(slots=True, frozen=True)
class VisibleArgument:
    info: GI.ArgInfo
    c_index: int
    from_python: bool
    to_python: bool
    required: bool
    nullable: bool
    is_closure_target: bool
    is_varargs_slot: bool
    is_varargs_callback: bool


@dataclass(slots=True, frozen=True)
class Arguments:
    args: tuple[GI.ArgInfo, ...]
    can_have_defaults: bool
    hidden: frozenset[int]
    closure_targets: frozenset[int]
    varargs_index: int | None

    @property
    def varargs_info(self) -> GI.ArgInfo | None:
        return self.args[self.varargs_index] if self.varargs_index is not None else None

    def __iter__(self) -> Iterator[VisibleArgument]:
        for index, gi_arg in enumerate(self.args):
            if index in self.hidden:
                continue

            direction = gi_arg.get_direction()
            nullable = gi_arg.may_be_null()
            closure_index = gi_arg.get_closure_index()

            yield VisibleArgument(
                info=gi_arg,
                c_index=index,
                from_python=direction in FROM_PYTHON,
                to_python=direction in TO_PYTHON,
                # An arg is "required" (no `= ...` default) iff PyGObject's
                # runtime would reject omitting it. The runtime accepts
                # omission iff pygi_arg_cache_allow_none() is true, which
                # boils down to may_be_null OR is_optional.
                required=not (nullable or gi_arg.is_optional()),
                nullable=nullable,
                is_closure_target=index in self.closure_targets,
                is_varargs_slot=index == self.varargs_index,
                is_varargs_callback=closure_index == self.varargs_index,
            )

    @classmethod
    def for_callable(
        cls, info: GI.CallableInfo, /, *, allow_varargs: bool = True
    ) -> Self:
        gi_args = info.get_arguments()

        hidden_indexes: set[int] = set()
        closure_indexes: set[int] = set()
        from_python_indexes: set[int] = set()

        if (
            return_array_length_index := info.get_return_type().get_array_length_index()
        ) > -1:
            hidden_indexes.add(return_array_length_index)

        is_callback = isinstance(info, GI.CallbackInfo)

        if is_callback:
            # Callback arguments that are used for closure have a closure index
            # that matches their argument index, so we can just check for that
            # instead of checking the type and direction
            for arg_index, arg in enumerate(gi_args):
                if arg.get_closure_index() == arg_index:
                    closure_indexes.add(arg_index)

                from_python_indexes.add(arg_index)

            # Apply PyGObject's user_data heuristic when no explicit closure
            # annotation is present. This mirrors the auto-detection in
            # pygi_closure_cache_new (pygi-cache.c lines 1092-1111), which
            # picks the first IN-direction void-pointer arg and treats it
            # as the user_data slot for the callback.
            if not closure_indexes:
                for arg_index, arg in enumerate(gi_args):
                    if arg.get_direction() != GI.Direction.IN:
                        continue
                    type_info = arg.get_type_info()
                    if (
                        type_info.get_tag() == GI.TypeTag.VOID
                        and type_info.is_pointer()
                    ):
                        closure_indexes.add(arg_index)
                        break
        else:
            for arg_index, arg in enumerate(gi_args):
                type_info = arg.get_type_info()
                tag = type_info.get_tag()
                is_from_python = arg.get_direction() in FROM_PYTHON

                # Hide array length args
                if (
                    tag == GI.TypeTag.ARRAY
                    and (array_length_index := type_info.get_array_length_index()) > -1
                ):
                    hidden_indexes.add(array_length_index)

                # Hide destroy and closure args for callbacks
                if (
                    tag == GI.TypeTag.INTERFACE
                    and isinstance(type_info.get_interface(), GI.CallbackInfo)
                    and arg_index not in hidden_indexes
                    and arg_index not in closure_indexes
                ):
                    if (
                        closure_index := arg.get_closure_index()
                    ) > -1 and is_from_python:
                        closure_indexes.add(closure_index)

                    if (destroy_index := arg.get_destroy_index()) > -1:
                        hidden_indexes.add(destroy_index)

                if is_from_python:
                    from_python_indexes.add(arg_index)

        # Find the last closure argument whether it comes before or after the callback.
        last_visible_from_python = max(from_python_indexes - hidden_indexes, default=-1)

        # Treat a user_data slot as the *varargs argument iff it is the
        # trailing FROM_PYTHON arg in C-arg order (i.e. no other visible
        # FROM_PYTHON arg has a higher C-arg index). This mirrors
        # PyGObject's runtime varargs detection in the reverse loop of
        # _callable_cache_generate_args_cache_real, which picks the last
        # FROM_PYTHON arg and only treats it as varargs when it is a
        # CHILD_WITH_PYARG (i.e. a user_data slot).
        varargs_index = (
            last_visible_from_python
            if allow_varargs and last_visible_from_python in closure_indexes
            else None
        )

        return cls(
            args=gi_args,
            can_have_defaults=isinstance(info, GI.FunctionInfo),
            hidden=frozenset(hidden_indexes),
            closure_targets=frozenset(closure_indexes),
            varargs_index=varargs_index,
        )
