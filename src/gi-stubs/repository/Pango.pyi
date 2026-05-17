from typing import Any
from typing import Final
from typing import Literal
from typing import type_check_only
from typing import TypeAlias
from typing_extensions import TypeVarTuple
from typing_extensions import Unpack

from collections.abc import Callable
from collections.abc import Sequence

from gi import _gi
from gi.repository import Gio
from gi.repository import GLib
from gi.repository import GObject
from gi.repository import HarfBuzz

_DataTs = TypeVarTuple("_DataTs", default=Unpack[tuple[()]])

ANALYSIS_FLAG_CENTERED_BASELINE: Final[int]
ANALYSIS_FLAG_IS_ELLIPSIS: Final[int]
ANALYSIS_FLAG_NEED_HYPHEN: Final[int]
ATTR_INDEX_FROM_TEXT_BEGINNING: Final[int]
ATTR_INDEX_TO_TEXT_END: Final[int]
GLYPH_EMPTY: Final[int]
GLYPH_INVALID_INPUT: Final[int]
GLYPH_UNKNOWN_FLAG: Final[int]
SCALE: Final[int]
VERSION_MAJOR: Final[int]
VERSION_MICRO: Final[int]
VERSION_MINOR: Final[int]
VERSION_STRING: Final = "1.57.1"

def attr_allow_breaks_new(allow_breaks: bool) -> Attribute: ...
def attr_background_alpha_new(alpha: int) -> Attribute: ...
def attr_background_new(red: int, green: int, blue: int) -> Attribute: ...
def attr_baseline_shift_new(shift: int) -> Attribute: ...
def attr_break(
    text: str, length: int, attr_list: AttrList, offset: int
) -> list[LogAttr]: ...
def attr_fallback_new(enable_fallback: bool) -> Attribute: ...
def attr_family_new(family: str) -> Attribute: ...
def attr_font_desc_new(desc: FontDescription) -> Attribute: ...
def attr_font_features_new(features: str) -> Attribute: ...
def attr_font_scale_new(scale: _FontScaleValueType) -> Attribute: ...
def attr_foreground_alpha_new(alpha: int) -> Attribute: ...
def attr_foreground_new(red: int, green: int, blue: int) -> Attribute: ...
def attr_gravity_hint_new(hint: _GravityHintValueType) -> Attribute: ...
def attr_gravity_new(gravity: _GravityValueType) -> Attribute: ...
def attr_insert_hyphens_new(insert_hyphens: bool) -> Attribute: ...
def attr_language_new(language: Language) -> Attribute: ...
def attr_letter_spacing_new(letter_spacing: int) -> Attribute: ...
def attr_line_height_new(factor: float) -> Attribute: ...
def attr_line_height_new_absolute(height: int) -> Attribute: ...
def attr_list_from_string(text: str) -> AttrList | None: ...
def attr_overline_color_new(red: int, green: int, blue: int) -> Attribute: ...
def attr_overline_new(overline: _OverlineValueType) -> Attribute: ...
def attr_rise_new(rise: int) -> Attribute: ...
def attr_scale_new(scale_factor: float) -> Attribute: ...
def attr_sentence_new() -> Attribute: ...
def attr_shape_new(ink_rect: Rectangle, logical_rect: Rectangle) -> Attribute: ...
def attr_shape_new_with_data(
    ink_rect: Rectangle,
    logical_rect: Rectangle,
    data: int | Any | None = None,
    copy_func: Callable[[Any | None], int] | None = None,
) -> Attribute: ...
def attr_show_new(flags: _ShowFlagsValueType) -> Attribute: ...
def attr_size_new(size: int) -> Attribute: ...
def attr_size_new_absolute(size: int) -> Attribute: ...
def attr_stretch_new(stretch: _StretchValueType) -> Attribute: ...
def attr_strikethrough_color_new(red: int, green: int, blue: int) -> Attribute: ...
def attr_strikethrough_new(strikethrough: bool) -> Attribute: ...
def attr_style_new(style: _StyleValueType) -> Attribute: ...
def attr_text_transform_new(transform: _TextTransformValueType) -> Attribute: ...
def attr_type_get_name(type: _AttrTypeValueType) -> str | None: ...
def attr_type_register(name: str) -> AttrType: ...
def attr_underline_color_new(red: int, green: int, blue: int) -> Attribute: ...
def attr_underline_new(underline: _UnderlineValueType) -> Attribute: ...
def attr_variant_new(variant: _VariantValueType) -> Attribute: ...
def attr_weight_new(weight: _WeightValueType) -> Attribute: ...
def attr_word_new() -> Attribute: ...
def bidi_type_for_unichar(ch: str) -> BidiType: ...
def break_(text: str, length: int, analysis: Analysis) -> list[LogAttr]: ...
def default_break(
    text: str, length: int, analysis: Analysis | None = None
) -> list[LogAttr]: ...
def extents_to_pixels(
    inclusive: Rectangle = ..., nearest: Rectangle = ...
) -> tuple[Rectangle, Rectangle]: ...
def find_base_dir(text: str, length: int) -> Direction: ...
def find_paragraph_boundary(text: str, length: int) -> tuple[int, int]: ...
def font_description_from_string(str: str) -> FontDescription: ...
def get_log_attrs(
    text: str, length: int, level: int, language: Language
) -> list[LogAttr]: ...
def get_mirror_char(ch: str) -> tuple[bool, str]: ...
def gravity_get_for_matrix(matrix: Matrix | None = None) -> Gravity: ...
def gravity_get_for_script(
    script: _ScriptValueType,
    base_gravity: _GravityValueType,
    hint: _GravityHintValueType,
) -> Gravity: ...
def gravity_get_for_script_and_width(
    script: _ScriptValueType,
    wide: bool,
    base_gravity: _GravityValueType,
    hint: _GravityHintValueType,
) -> Gravity: ...
def gravity_to_rotation(gravity: _GravityValueType) -> float: ...
def is_zero_width(ch: str) -> bool: ...
def itemize(
    context: Context,
    text: str,
    start_index: int,
    length: int,
    attrs: AttrList,
    cached_iter: AttrIterator | None = None,
) -> list[Item]: ...
def itemize_with_base_dir(
    context: Context,
    base_dir: _DirectionValueType,
    text: str,
    start_index: int,
    length: int,
    attrs: AttrList,
    cached_iter: AttrIterator | None = None,
) -> list[Item]: ...
def language_from_string(language: str | None = None) -> Language | None: ...
def language_get_default() -> Language: ...
def language_get_preferred() -> list[Language]: ...
def layout_deserialize_error_quark() -> int: ...
def log2vis_get_embedding_levels(
    text: str, length: int, pbase_dir: _DirectionValueType
) -> tuple[bytes, Direction]: ...
def markup_parser_finish(
    context: GLib.MarkupParseContext,
) -> tuple[bool, AttrList, str, str]: ...
def markup_parser_new(accel_marker: str) -> GLib.MarkupParseContext: ...
def parse_enum(
    type: type[Any], str: str | None, warn: bool
) -> tuple[bool, int, str]: ...
def parse_markup(
    markup_text: str, length: int, accel_marker: str
) -> tuple[bool, AttrList, str, str]: ...
def parse_stretch(str: str, warn: bool) -> tuple[bool, Stretch]: ...
def parse_style(str: str, warn: bool) -> tuple[bool, Style]: ...
def parse_variant(str: str, warn: bool) -> tuple[bool, Variant]: ...
def parse_weight(str: str, warn: bool) -> tuple[bool, Weight]: ...
def quantize_line_geometry(thickness: int, position: int) -> tuple[int, int]: ...
def read_line(stream: int | Any | None, str: GLib.String) -> int: ...
def reorder_items(items: list[Item]) -> list[Item]: ...
def scan_int(pos: str) -> tuple[bool, str, int]: ...
def scan_string(pos: str, out: GLib.String) -> tuple[bool, str]: ...
def scan_word(pos: str, out: GLib.String) -> tuple[bool, str]: ...
def script_for_unichar(ch: str) -> Script: ...
def script_get_sample_language(script: _ScriptValueType) -> Language | None: ...
def shape(text: str, length: int, analysis: Analysis) -> GlyphString: ...
def shape_full(
    item_text: str,
    item_length: int,
    paragraph_text: str | None,
    paragraph_length: int,
    analysis: Analysis,
) -> GlyphString: ...
def shape_item(
    item: Item,
    paragraph_text: str | None,
    paragraph_length: int,
    log_attrs: LogAttr | None,
    flags: _ShapeFlagsValueType,
) -> GlyphString: ...
def shape_with_flags(
    item_text: str,
    item_length: int,
    paragraph_text: str | None,
    paragraph_length: int,
    analysis: Analysis,
    flags: _ShapeFlagsValueType,
) -> GlyphString: ...
def skip_space(pos: str) -> tuple[bool, str]: ...
def split_file_list(str: str) -> list[str]: ...
def tab_array_from_string(text: str) -> TabArray | None: ...
def tailor_break(
    text: str, length: int, analysis: Analysis, offset: int
) -> list[LogAttr]: ...
def trim_string(str: str) -> str: ...
def unichar_direction(ch: str) -> Direction: ...
def units_from_double(d: float) -> int: ...
def units_to_double(i: int) -> float: ...
def version() -> int: ...
def version_check(
    required_major: int, required_minor: int, required_micro: int
) -> str | None: ...
def version_string() -> str: ...

class Analysis(_gi.Struct):
    """
    :Constructors:

    ::

        Analysis()
    """

    shape_engine: int
    lang_engine: int
    font: Font
    level: int
    gravity: int
    flags: int
    script: int
    language: Language
    extra_attrs: list[int]

class AttrClass(_gi.Struct):
    """
    :Constructors:

    ::

        AttrClass()
    """

    type: AttrType
    @property
    def copy(self) -> Callable[[Attribute], Attribute]: ...
    @property
    def destroy(self) -> Callable[[Attribute], None]: ...
    @property
    def equal(self) -> Callable[[Attribute, Attribute], bool]: ...

class AttrColor(_gi.Struct):
    """
    :Constructors:

    ::

        AttrColor()
    """

    attr: Attribute
    color: Color

class AttrFloat(_gi.Struct):
    """
    :Constructors:

    ::

        AttrFloat()
    """

    attr: Attribute
    value: float

class AttrFontDesc(_gi.Struct):
    """
    :Constructors:

    ::

        AttrFontDesc()
    """

    attr: Attribute
    desc: FontDescription
    @staticmethod
    def new(desc: FontDescription) -> Attribute: ...

class AttrFontFeatures(_gi.Struct):
    """
    :Constructors:

    ::

        AttrFontFeatures()
    """

    attr: Attribute
    features: str
    @staticmethod
    def new(features: str) -> Attribute: ...

class AttrInt(_gi.Struct):
    """
    :Constructors:

    ::

        AttrInt()
    """

    attr: Attribute
    value: int

class AttrIterator(GObject.GBoxed):
    def copy(self) -> AttrIterator: ...
    def destroy(self) -> None: ...
    def get(self, type: _AttrTypeValueType) -> Attribute | None: ...
    def get_attrs(self) -> list[Attribute]: ...
    def get_font(self, desc: FontDescription) -> tuple[Language, list[Attribute]]: ...
    def next(self) -> bool: ...
    def range(self) -> tuple[int, int]: ...

class AttrLanguage(_gi.Struct):
    """
    :Constructors:

    ::

        AttrLanguage()
    """

    attr: Attribute
    value: Language
    @staticmethod
    def new(language: Language) -> Attribute: ...

class AttrList(GObject.GBoxed):
    """
    :Constructors:

    ::

        new() -> Pango.AttrList
    """
    def __init__(self) -> None: ...
    def change(self, attr: Attribute) -> None: ...
    def copy(self) -> AttrList | None: ...
    def equal(self, other_list: AttrList) -> bool: ...
    def filter(
        self, func: Callable[[Attribute, Unpack[_DataTs]], bool], *data: Unpack[_DataTs]
    ) -> AttrList | None: ...
    @staticmethod
    def from_string(text: str) -> AttrList | None: ...
    def get_attributes(self) -> list[Attribute]: ...
    def get_iterator(self) -> AttrIterator: ...
    def insert(self, attr: Attribute) -> None: ...
    def insert_before(self, attr: Attribute) -> None: ...
    @classmethod
    def new(cls) -> AttrList: ...
    def ref(self) -> AttrList: ...
    def splice(self, other: AttrList, pos: int, len: int) -> None: ...
    def to_string(self) -> str: ...
    def unref(self) -> None: ...
    def update(self, pos: int, remove: int, add: int) -> None: ...

class AttrShape(_gi.Struct):
    """
    :Constructors:

    ::

        AttrShape()
    """

    attr: Attribute
    ink_rect: Rectangle
    logical_rect: Rectangle
    data: int
    copy_func: Callable[[Any | None], int]
    destroy_func: Callable[[Any | None], None]
    @staticmethod
    def new(ink_rect: Rectangle, logical_rect: Rectangle) -> Attribute: ...
    @staticmethod
    def new_with_data(
        ink_rect: Rectangle,
        logical_rect: Rectangle,
        data: int | Any | None = None,
        copy_func: Callable[[Any | None], int] | None = None,
    ) -> Attribute: ...

class AttrSize(_gi.Struct):
    """
    :Constructors:

    ::

        AttrSize()
    """

    attr: Attribute
    size: int
    absolute: int
    @staticmethod
    def new(size: int) -> Attribute: ...
    @staticmethod
    def new_absolute(size: int) -> Attribute: ...

class AttrString(_gi.Struct):
    """
    :Constructors:

    ::

        AttrString()
    """

    attr: Attribute
    value: str

class Attribute(GObject.GBoxed):
    """
    :Constructors:

    ::

        Attribute()
    """

    klass: AttrClass
    start_index: int
    end_index: int
    def as_color(self) -> AttrColor | None: ...
    def as_float(self) -> AttrFloat | None: ...
    def as_font_desc(self) -> AttrFontDesc | None: ...
    def as_font_features(self) -> AttrFontFeatures | None: ...
    def as_int(self) -> AttrInt | None: ...
    def as_language(self) -> AttrLanguage | None: ...
    def as_shape(self) -> AttrShape | None: ...
    def as_size(self) -> AttrSize | None: ...
    def as_string(self) -> AttrString | None: ...
    def copy(self) -> Attribute: ...
    def destroy(self) -> None: ...
    def equal(self, attr2: Attribute) -> bool: ...
    def init(self, klass: AttrClass) -> None: ...

class Color(GObject.GBoxed):
    """
    :Constructors:

    ::

        Color()
    """

    red: int
    green: int
    blue: int
    def copy(self) -> Color | None: ...
    def free(self) -> None: ...
    def parse(self, spec: str) -> bool: ...
    def parse_with_alpha(self, spec: str) -> tuple[bool, int]: ...
    def to_string(self) -> str: ...

class Context(GObject.Object):
    """
    :Constructors:

    ::

        Context(**properties)
        new() -> Pango.Context

    Object PangoContext

    Signals from GObject:
      notify (GParam)
    """
    def changed(self) -> None: ...
    def get_base_dir(self) -> Direction: ...
    def get_base_gravity(self) -> Gravity: ...
    def get_font_description(self) -> FontDescription | None: ...
    def get_font_map(self) -> FontMap | None: ...
    def get_gravity(self) -> Gravity: ...
    def get_gravity_hint(self) -> GravityHint: ...
    def get_language(self) -> Language: ...
    def get_matrix(self) -> Matrix | None: ...
    def get_metrics(
        self, desc: FontDescription | None = None, language: Language | None = None
    ) -> FontMetrics: ...
    def get_round_glyph_positions(self) -> bool: ...
    def get_serial(self) -> int: ...
    def list_families(self) -> list[FontFamily]: ...
    def load_font(self, desc: FontDescription) -> Font | None: ...
    def load_fontset(
        self, desc: FontDescription, language: Language
    ) -> Fontset | None: ...
    @classmethod
    def new(cls) -> Context: ...
    def set_base_dir(self, direction: _DirectionValueType) -> None: ...
    def set_base_gravity(self, gravity: _GravityValueType) -> None: ...
    def set_font_description(self, desc: FontDescription) -> None: ...
    def set_font_map(self, font_map: FontMap | None = None) -> None: ...
    def set_gravity_hint(self, hint: _GravityHintValueType) -> None: ...
    def set_language(self, language: Language | None = None) -> None: ...
    def set_matrix(self, matrix: Matrix | None = None) -> None: ...
    def set_round_glyph_positions(self, round_positions: bool) -> None: ...

class ContextClass(_gi.Struct): ...

class Coverage(GObject.Object):
    """
    :Constructors:

    ::

        Coverage(**properties)
        new() -> Pango.Coverage

    Object PangoCoverage

    Signals from GObject:
      notify (GParam)
    """
    def copy(self) -> Coverage: ...
    @staticmethod
    def from_bytes(bytes: Sequence[int]) -> Coverage | None: ...
    def get(self, index_: int) -> CoverageLevel: ...
    def max(self, other: Coverage) -> None: ...
    @classmethod
    def new(cls) -> Coverage: ...
    def ref(self) -> Coverage: ...
    def set(self, index_: int, level: _CoverageLevelValueType) -> None: ...
    def to_bytes(self) -> bytes: ...
    def unref(self) -> None: ...

class Font(GObject.Object):
    """
    :Constructors:

    ::

        Font(**properties)

    Object PangoFont

    Signals from GObject:
      notify (GParam)
    """
    @property
    def parent_instance(self) -> GObject.Object: ...
    def describe(self) -> FontDescription: ...
    def describe_with_absolute_size(self) -> FontDescription: ...
    @staticmethod
    def descriptions_free(descs: Sequence[FontDescription] | None = None) -> None: ...
    @staticmethod
    def deserialize(context: Context, bytes: GLib.Bytes) -> Font | None: ...
    def do_create_hb_font(self) -> HarfBuzz.font_t: ...
    def do_describe(self) -> FontDescription: ...
    def do_describe_absolute(self) -> FontDescription: ...
    def do_get_coverage(self, language: Language, /) -> Coverage: ...
    def do_get_features(
        self, num_features: int, /
    ) -> tuple[list[HarfBuzz.feature_t], int]: ...
    def do_get_font_map(self) -> FontMap | None: ...
    def do_get_glyph_extents(self, glyph: int, /) -> tuple[Rectangle, Rectangle]: ...
    def do_get_metrics(self, language: Language | None, /) -> FontMetrics: ...
    def get_coverage(self, language: Language) -> Coverage: ...
    def get_face(self) -> FontFace | None: ...
    def get_features(
        self, num_features: int
    ) -> tuple[list[HarfBuzz.feature_t], int]: ...
    def get_font_map(self) -> FontMap | None: ...
    def get_glyph_extents(self, glyph: int) -> tuple[Rectangle, Rectangle]: ...
    def get_languages(self) -> list[Language]: ...
    def get_metrics(self, language: Language | None = None) -> FontMetrics: ...
    def has_char(self, wc: str) -> bool: ...
    def serialize(self) -> GLib.Bytes: ...

class FontClass(_gi.Struct):
    """
    :Constructors:

    ::

        FontClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...
    @property
    def describe(self) -> Callable[[Font], FontDescription]: ...
    @property
    def get_coverage(self) -> Callable[[Font, Language], Coverage]: ...
    @property
    def get_glyph_extents(
        self,
    ) -> Callable[[Font | None, int], tuple[Rectangle, Rectangle]]: ...
    @property
    def get_metrics(self) -> Callable[[Font | None, Language | None], FontMetrics]: ...
    @property
    def get_font_map(self) -> Callable[[Font | None], FontMap | None]: ...
    @property
    def describe_absolute(self) -> Callable[[Font], FontDescription]: ...
    @property
    def get_features(
        self,
    ) -> Callable[[Font, int, int], tuple[list[HarfBuzz.feature_t], int]]: ...
    @property
    def create_hb_font(self) -> Callable[[Font], HarfBuzz.font_t]: ...

class FontDescription(GObject.GBoxed):
    """
    :Constructors:

    ::

        new() -> Pango.FontDescription
    """
    def __init__(self, string: str | None = None) -> None: ...
    def better_match(
        self, old_match: FontDescription | None, new_match: FontDescription
    ) -> bool: ...
    def copy(self) -> FontDescription | None: ...
    def copy_static(self) -> FontDescription | None: ...
    def equal(self, desc2: FontDescription) -> bool: ...
    def free(self) -> None: ...
    @staticmethod
    def from_string(str: str) -> FontDescription: ...
    def get_color(self) -> FontColor: ...
    def get_family(self) -> str | None: ...
    def get_features(self) -> str | None: ...
    def get_gravity(self) -> Gravity: ...
    def get_set_fields(self) -> FontMask: ...
    def get_size(self) -> int: ...
    def get_size_is_absolute(self) -> bool: ...
    def get_stretch(self) -> Stretch: ...
    def get_style(self) -> Style: ...
    def get_variant(self) -> Variant: ...
    def get_variations(self) -> str | None: ...
    def get_weight(self) -> Weight: ...
    def hash(self) -> int: ...
    def merge(
        self, desc_to_merge: FontDescription | None, replace_existing: bool
    ) -> None: ...
    def merge_static(
        self, desc_to_merge: FontDescription, replace_existing: bool
    ) -> None: ...
    @classmethod
    def new(cls) -> FontDescription: ...
    def set_absolute_size(self, size: float) -> None: ...
    def set_color(self, color: _FontColorValueType) -> None: ...
    def set_family(self, family: str) -> None: ...
    def set_family_static(self, family: str) -> None: ...
    def set_features(self, features: str | None = None) -> None: ...
    def set_features_static(self, features: str) -> None: ...
    def set_gravity(self, gravity: _GravityValueType) -> None: ...
    def set_size(self, size: int) -> None: ...
    def set_stretch(self, stretch: _StretchValueType) -> None: ...
    def set_style(self, style: _StyleValueType) -> None: ...
    def set_variant(self, variant: _VariantValueType) -> None: ...
    def set_variations(self, variations: str | None = None) -> None: ...
    def set_variations_static(self, variations: str) -> None: ...
    def set_weight(self, weight: _WeightValueType) -> None: ...
    def to_filename(self) -> str | None: ...
    def to_string(self) -> str: ...
    def unset_fields(self, to_unset: _FontMaskValueType) -> None: ...

class FontFace(GObject.Object):
    """
    :Constructors:

    ::

        FontFace(**properties)

    Object PangoFontFace

    Signals from GObject:
      notify (GParam)
    """
    @property
    def parent_instance(self) -> GObject.Object: ...
    def describe(self) -> FontDescription: ...
    def do_describe(self) -> FontDescription: ...
    def do_get_face_name(self) -> str: ...
    def do_get_family(self) -> FontFamily: ...
    def do_is_synthesized(self) -> bool: ...
    def do_list_sizes(self) -> list[int]: ...
    def get_face_name(self) -> str: ...
    def get_family(self) -> FontFamily: ...
    def is_synthesized(self) -> bool: ...
    def list_sizes(self) -> list[int]: ...

class FontFaceClass(_gi.Struct):
    """
    :Constructors:

    ::

        FontFaceClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...
    @property
    def get_face_name(self) -> Callable[[FontFace], str]: ...
    @property
    def describe(self) -> Callable[[FontFace], FontDescription]: ...
    @property
    def list_sizes(self) -> Callable[[FontFace], tuple[list[int], int]]: ...
    @property
    def is_synthesized(self) -> Callable[[FontFace], bool]: ...
    @property
    def get_family(self) -> Callable[[FontFace], FontFamily]: ...

class FontFamily(GObject.Object, Gio.ListModel):
    """
    :Constructors:

    ::

        FontFamily(**properties)

    Object PangoFontFamily

    Properties from PangoFontFamily:
      item-type -> GType:

      n-items -> guint:

      name -> gchararray:

      is-monospace -> gboolean:

      is-variable -> gboolean:


    Signals from GListModel:
      items-changed (guint, guint, guint)

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(GObject.Object.Props):
        @property
        def is_monospace(self) -> bool: ...
        @property
        def is_variable(self) -> bool: ...
        @property
        def item_type(self) -> type[Any]: ...
        @property
        def n_items(self) -> int: ...
        @property
        def name(self) -> str: ...

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> GObject.Object: ...
    def do_get_face(self, name: str | None, /) -> FontFace | None: ...
    def do_get_name(self) -> str: ...
    def do_is_monospace(self) -> bool: ...
    def do_is_variable(self) -> bool: ...
    def do_list_faces(self) -> list[FontFace]: ...
    def get_face(self, name: str | None = None) -> FontFace | None: ...
    def get_name(self) -> str: ...
    def is_monospace(self) -> bool: ...
    def is_variable(self) -> bool: ...
    def list_faces(self) -> list[FontFace]: ...

class FontFamilyClass(_gi.Struct):
    """
    :Constructors:

    ::

        FontFamilyClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...
    @property
    def list_faces(self) -> Callable[[FontFamily], tuple[list[FontFace], int]]: ...
    @property
    def get_name(self) -> Callable[[FontFamily], str]: ...
    @property
    def is_monospace(self) -> Callable[[FontFamily], bool]: ...
    @property
    def is_variable(self) -> Callable[[FontFamily], bool]: ...
    @property
    def get_face(self) -> Callable[[FontFamily, str | None], FontFace | None]: ...

class FontMap(GObject.Object, Gio.ListModel):
    """
    :Constructors:

    ::

        FontMap(**properties)

    Object PangoFontMap

    Properties from PangoFontMap:
      item-type -> GType:

      n-items -> guint:


    Signals from GListModel:
      items-changed (guint, guint, guint)

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(GObject.Object.Props):
        @property
        def item_type(self) -> type[Any]: ...
        @property
        def n_items(self) -> int: ...

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> GObject.Object: ...
    def add_font_file(self, filename: str) -> bool: ...
    def changed(self) -> None: ...
    def create_context(self) -> Context: ...
    def do_changed(self) -> None: ...
    def do_get_family(self, name: str, /) -> FontFamily | None: ...
    def do_get_serial(self) -> int: ...
    def do_list_families(self) -> list[FontFamily]: ...
    def do_load_font(
        self, context: Context, desc: FontDescription, /
    ) -> Font | None: ...
    def do_load_fontset(
        self, context: Context, desc: FontDescription, language: Language, /
    ) -> Fontset | None: ...
    def get_family(self, name: str) -> FontFamily | None: ...
    def get_serial(self) -> int: ...
    def list_families(self) -> list[FontFamily]: ...
    def load_font(self, context: Context, desc: FontDescription) -> Font | None: ...
    def load_fontset(
        self, context: Context, desc: FontDescription, language: Language
    ) -> Fontset | None: ...
    def reload_font(
        self,
        font: Font,
        scale: float,
        context: Context | None = None,
        variations: str | None = None,
    ) -> Font: ...

class FontMapClass(_gi.Struct):
    """
    :Constructors:

    ::

        FontMapClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...
    @property
    def load_font(
        self,
    ) -> Callable[[FontMap, Context, FontDescription], Font | None]: ...
    @property
    def list_families(self) -> Callable[[FontMap], tuple[list[FontFamily], int]]: ...
    @property
    def load_fontset(
        self,
    ) -> Callable[[FontMap, Context, FontDescription, Language], Fontset | None]: ...
    @property
    def shape_engine_type(self) -> str: ...
    @property
    def get_serial(self) -> Callable[[FontMap], int]: ...
    @property
    def changed(self) -> Callable[[FontMap], None]: ...
    @property
    def get_family(self) -> Callable[[FontMap, str], FontFamily | None]: ...
    @property
    def get_face(self) -> int: ...

class FontMetrics(GObject.GBoxed):
    """
    :Constructors:

    ::

        FontMetrics()
    """
    @property
    def ref_count(self) -> int: ...
    @property
    def ascent(self) -> int: ...
    @property
    def descent(self) -> int: ...
    @property
    def height(self) -> int: ...
    @property
    def approximate_char_width(self) -> int: ...
    @property
    def approximate_digit_width(self) -> int: ...
    @property
    def underline_position(self) -> int: ...
    @property
    def underline_thickness(self) -> int: ...
    @property
    def strikethrough_position(self) -> int: ...
    @property
    def strikethrough_thickness(self) -> int: ...
    def get_approximate_char_width(self) -> int: ...
    def get_approximate_digit_width(self) -> int: ...
    def get_ascent(self) -> int: ...
    def get_descent(self) -> int: ...
    def get_height(self) -> int: ...
    def get_strikethrough_position(self) -> int: ...
    def get_strikethrough_thickness(self) -> int: ...
    def get_underline_position(self) -> int: ...
    def get_underline_thickness(self) -> int: ...
    def ref(self) -> FontMetrics | None: ...
    def unref(self) -> None: ...

class Fontset(GObject.Object):
    """
    :Constructors:

    ::

        Fontset(**properties)

    Object PangoFontset

    Signals from GObject:
      notify (GParam)
    """
    @property
    def parent_instance(self) -> GObject.Object: ...
    def do_foreach(
        self,
        func: Callable[[Fontset, Font, Any | None], bool],
        data: int | Any | None,
        /,
    ) -> None: ...
    def do_get_font(self, wc: int, /) -> Font: ...
    def do_get_language(self) -> Language: ...
    def do_get_metrics(self) -> FontMetrics: ...
    def foreach(
        self,
        func: Callable[[Fontset, Font, Unpack[_DataTs]], bool],
        *data: Unpack[_DataTs],
    ) -> None: ...
    def get_font(self, wc: int) -> Font: ...
    def get_metrics(self) -> FontMetrics: ...

class FontsetClass(_gi.Struct):
    """
    :Constructors:

    ::

        FontsetClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...
    @property
    def get_font(self) -> Callable[[Fontset, int], Font]: ...
    @property
    def get_metrics(self) -> Callable[[Fontset], FontMetrics]: ...
    @property
    def get_language(self) -> Callable[[Fontset], Language]: ...
    @property
    def foreach(
        self,
    ) -> Callable[
        [Fontset, Callable[[Fontset, Font, Any | None], bool], Any | None], None
    ]: ...

class FontsetSimple(Fontset):
    """
    :Constructors:

    ::

        FontsetSimple(**properties)
        new(language:Pango.Language) -> Pango.FontsetSimple

    Object PangoFontsetSimple

    Signals from GObject:
      notify (GParam)
    """
    def append(self, font: Font) -> None: ...
    @classmethod
    def new(cls, language: Language) -> FontsetSimple: ...
    def size(self) -> int: ...

class FontsetSimpleClass(_gi.Struct): ...

class GlyphGeometry(_gi.Struct):
    """
    :Constructors:

    ::

        GlyphGeometry()
    """

    width: int
    x_offset: int
    y_offset: int

class GlyphInfo(_gi.Struct):
    """
    :Constructors:

    ::

        GlyphInfo()
    """

    glyph: int
    geometry: GlyphGeometry
    attr: GlyphVisAttr

class GlyphItem(GObject.GBoxed):
    """
    :Constructors:

    ::

        GlyphItem()
    """

    item: Item
    glyphs: GlyphString
    y_offset: int
    start_x_offset: int
    end_x_offset: int
    def apply_attrs(self, text: str, list: AttrList) -> list[GlyphItem]: ...
    def copy(self) -> GlyphItem | None: ...
    def free(self) -> None: ...
    def get_logical_widths(self, text: str) -> list[int]: ...
    def letter_space(
        self, text: str, log_attrs: Sequence[LogAttr], letter_spacing: int
    ) -> None: ...
    def split(self, text: str, split_index: int) -> GlyphItem | None: ...

class GlyphItemIter(GObject.GBoxed):
    """
    :Constructors:

    ::

        GlyphItemIter()
    """

    glyph_item: GlyphItem
    text: str
    start_glyph: int
    start_index: int
    start_char: int
    end_glyph: int
    end_index: int
    end_char: int
    def copy(self) -> GlyphItemIter | None: ...
    def free(self) -> None: ...
    def init_end(self, glyph_item: GlyphItem, text: str) -> bool: ...
    def init_start(self, glyph_item: GlyphItem, text: str) -> bool: ...
    def next_cluster(self) -> bool: ...
    def prev_cluster(self) -> bool: ...

class GlyphString(GObject.GBoxed):
    """
    :Constructors:

    ::

        GlyphString()
        new() -> Pango.GlyphString
    """

    num_glyphs: int
    glyphs: list[GlyphInfo]
    log_clusters: int
    @property
    def space(self) -> int: ...
    def __init__(self) -> None: ...
    def copy(self) -> GlyphString | None: ...
    def extents(self, font: Font) -> tuple[Rectangle, Rectangle]: ...
    def extents_range(
        self, start: int, end: int, font: Font
    ) -> tuple[Rectangle, Rectangle]: ...
    def free(self) -> None: ...
    def get_logical_widths(
        self, text: str, length: int, embedding_level: int
    ) -> list[int]: ...
    def get_width(self) -> int: ...
    def index_to_x(
        self, text: str, length: int, analysis: Analysis, index_: int, trailing: bool
    ) -> int: ...
    def index_to_x_full(
        self,
        text: str,
        length: int,
        analysis: Analysis,
        attrs: LogAttr | None,
        index_: int,
        trailing: bool,
    ) -> int: ...
    @classmethod
    def new(cls) -> GlyphString: ...
    def set_size(self, new_len: int) -> None: ...
    def x_to_index(
        self, text: str, length: int, analysis: Analysis, x_pos: int
    ) -> tuple[int, int]: ...

class GlyphVisAttr(_gi.Struct):
    """
    :Constructors:

    ::

        GlyphVisAttr()
    """

    is_cluster_start: int
    is_color: int

class Item(GObject.GBoxed):
    """
    :Constructors:

    ::

        Item()
        new() -> Pango.Item
    """

    offset: int
    length: int
    num_chars: int
    analysis: Analysis
    def __init__(self) -> None: ...
    def apply_attrs(self, iter: AttrIterator) -> None: ...
    def copy(self) -> Item | None: ...
    def free(self) -> None: ...
    def get_char_offset(self) -> int: ...
    @classmethod
    def new(cls) -> Item: ...
    def split(self, split_index: int, split_offset: int) -> Item: ...

class Language(GObject.GBoxed):
    @staticmethod
    def from_string(language: str | None = None) -> Language | None: ...
    @staticmethod
    def get_default() -> Language: ...
    @staticmethod
    def get_preferred() -> list[Language]: ...
    def get_sample_string(self) -> str: ...
    def get_scripts(self) -> list[Script]: ...
    def includes_script(self, script: _ScriptValueType) -> bool: ...
    def matches(self, range_list: str) -> bool: ...
    def to_string(self) -> str: ...

class Layout(GObject.Object):
    """
    :Constructors:

    ::

        Layout(**properties)
        new(context:Pango.Context) -> Pango.Layout

    Object PangoLayout

    Signals from GObject:
      notify (GParam)
    """
    def __init__(self, context: Context) -> None: ...
    def context_changed(self) -> None: ...
    def copy(self) -> Layout: ...
    @staticmethod
    def deserialize(
        context: Context, bytes: GLib.Bytes, flags: _LayoutDeserializeFlagsValueType
    ) -> Layout | None: ...
    def get_alignment(self) -> Alignment: ...
    def get_attributes(self) -> AttrList | None: ...
    def get_auto_dir(self) -> bool: ...
    def get_baseline(self) -> int: ...
    def get_caret_pos(self, index_: int) -> tuple[Rectangle, Rectangle]: ...
    def get_character_count(self) -> int: ...
    def get_context(self) -> Context: ...
    def get_cursor_pos(self, index_: int) -> tuple[Rectangle, Rectangle]: ...
    def get_direction(self, index: int) -> Direction: ...
    def get_ellipsize(self) -> EllipsizeMode: ...
    def get_extents(self) -> tuple[Rectangle, Rectangle]: ...
    def get_font_description(self) -> FontDescription | None: ...
    def get_height(self) -> int: ...
    def get_indent(self) -> int: ...
    def get_iter(self) -> LayoutIter: ...
    def get_justify(self) -> bool: ...
    def get_justify_last_line(self) -> bool: ...
    def get_line(self, line: int) -> LayoutLine | None: ...
    def get_line_count(self) -> int: ...
    def get_line_readonly(self, line: int) -> LayoutLine | None: ...
    def get_line_spacing(self) -> float: ...
    def get_lines(self) -> list[LayoutLine]: ...
    def get_lines_readonly(self) -> list[LayoutLine]: ...
    def get_log_attrs(self) -> list[LogAttr]: ...
    def get_log_attrs_readonly(self) -> list[LogAttr]: ...
    def get_pixel_extents(self) -> tuple[Rectangle, Rectangle]: ...
    def get_pixel_size(self) -> tuple[int, int]: ...
    def get_serial(self) -> int: ...
    def get_single_paragraph_mode(self) -> bool: ...
    def get_size(self) -> tuple[int, int]: ...
    def get_spacing(self) -> int: ...
    def get_tabs(self) -> TabArray | None: ...
    def get_text(self) -> str: ...
    def get_unknown_glyphs_count(self) -> int: ...
    def get_width(self) -> int: ...
    def get_wrap(self) -> WrapMode: ...
    def index_to_line_x(self, index_: int, trailing: bool) -> tuple[int, int]: ...
    def index_to_pos(self, index_: int) -> Rectangle: ...
    def is_ellipsized(self) -> bool: ...
    def is_wrapped(self) -> bool: ...
    def move_cursor_visually(
        self, strong: bool, old_index: int, old_trailing: int, direction: int
    ) -> tuple[int, int]: ...
    @classmethod
    def new(cls, context: Context) -> Layout: ...
    def serialize(self, flags: _LayoutSerializeFlagsValueType) -> GLib.Bytes: ...
    def set_alignment(self, alignment: _AlignmentValueType) -> None: ...
    def set_attributes(self, attrs: AttrList | None = None) -> None: ...
    def set_auto_dir(self, auto_dir: bool) -> None: ...
    def set_ellipsize(self, ellipsize: _EllipsizeModeValueType) -> None: ...
    def set_font_description(self, desc: FontDescription | None = None) -> None: ...
    def set_height(self, height: int) -> None: ...
    def set_indent(self, indent: int) -> None: ...
    def set_justify(self, justify: bool) -> None: ...
    def set_justify_last_line(self, justify: bool) -> None: ...
    def set_line_spacing(self, factor: float) -> None: ...
    def set_markup(self, text: str, length: int = -1) -> None: ...
    def set_markup_with_accel(
        self, markup: str, length: int, accel_marker: str
    ) -> str: ...
    def set_single_paragraph_mode(self, setting: bool) -> None: ...
    def set_spacing(self, spacing: int) -> None: ...
    def set_tabs(self, tabs: TabArray | None = None) -> None: ...
    def set_text(self, text: str, length: int = -1) -> None: ...
    def set_width(self, width: int) -> None: ...
    def set_wrap(self, wrap: _WrapModeValueType) -> None: ...
    def write_to_file(
        self, flags: _LayoutSerializeFlagsValueType, filename: str
    ) -> bool: ...
    def xy_to_index(self, x: int, y: int) -> tuple[bool, int, int]: ...

class LayoutClass(_gi.Struct): ...

class LayoutIter(GObject.GBoxed):
    def at_last_line(self) -> bool: ...
    def copy(self) -> LayoutIter | None: ...
    def free(self) -> None: ...
    def get_baseline(self) -> int: ...
    def get_char_extents(self) -> Rectangle: ...
    def get_cluster_extents(self) -> tuple[Rectangle, Rectangle]: ...
    def get_index(self) -> int: ...
    def get_layout(self) -> Layout | None: ...
    def get_layout_extents(self) -> tuple[Rectangle, Rectangle]: ...
    def get_line(self) -> LayoutLine | None: ...
    def get_line_extents(self) -> tuple[Rectangle, Rectangle]: ...
    def get_line_readonly(self) -> LayoutLine | None: ...
    def get_line_yrange(self) -> tuple[int, int]: ...
    def get_run(self) -> GlyphItem | None: ...
    def get_run_baseline(self) -> int: ...
    def get_run_extents(self) -> tuple[Rectangle, Rectangle]: ...
    def get_run_readonly(self) -> GlyphItem | None: ...
    def next_char(self) -> bool: ...
    def next_cluster(self) -> bool: ...
    def next_line(self) -> bool: ...
    def next_run(self) -> bool: ...

class LayoutLine(GObject.GBoxed):
    """
    :Constructors:

    ::

        LayoutLine()
    """

    layout: Layout
    start_index: int
    length: int
    runs: list[GlyphItem]
    resolved_dir: int
    def get_extents(self) -> tuple[Rectangle, Rectangle]: ...
    def get_height(self) -> int: ...
    def get_length(self) -> int: ...
    def get_pixel_extents(self) -> tuple[Rectangle, Rectangle]: ...
    def get_resolved_direction(self) -> Direction: ...
    def get_start_index(self) -> int: ...
    def get_x_ranges(self, start_index: int, end_index: int) -> list[int]: ...
    def index_to_x(self, index_: int, trailing: bool) -> int: ...
    def is_paragraph_start(self) -> bool: ...
    def ref(self) -> LayoutLine | None: ...
    def unref(self) -> None: ...
    def x_to_index(self, x_pos: int) -> tuple[bool, int, int]: ...

class LogAttr(_gi.Struct):
    """
    :Constructors:

    ::

        LogAttr()
    """

    is_line_break: int
    is_mandatory_break: int
    is_char_break: int
    is_white: int
    is_cursor_position: int
    is_word_start: int
    is_word_end: int
    is_sentence_boundary: int
    is_sentence_start: int
    is_sentence_end: int
    backspace_deletes_character: int
    is_expandable_space: int
    is_word_boundary: int
    break_inserts_hyphen: int
    break_removes_preceding: int
    reserved: int

class Matrix(GObject.GBoxed):
    """
    :Constructors:

    ::

        Matrix()
    """

    xx: float
    xy: float
    yx: float
    yy: float
    x0: float
    y0: float
    def concat(self, new_matrix: Matrix) -> None: ...
    def copy(self) -> Matrix | None: ...
    def free(self) -> None: ...
    def get_font_scale_factor(self) -> float: ...
    def get_font_scale_factors(self) -> tuple[float, float]: ...
    def get_slant_ratio(self) -> float: ...
    def rotate(self, degrees: float) -> None: ...
    def scale(self, scale_x: float, scale_y: float) -> None: ...
    def transform_distance(self, dx: float, dy: float) -> tuple[float, float]: ...
    def transform_pixel_rectangle(self, rect: Rectangle = ...) -> Rectangle: ...
    def transform_point(self, x: float, y: float) -> tuple[float, float]: ...
    def transform_rectangle(self, rect: Rectangle = ...) -> Rectangle: ...
    def translate(self, tx: float, ty: float) -> None: ...

class Rectangle(_gi.Struct):
    """
    :Constructors:

    ::

        Rectangle()
    """

    x: int
    y: int
    width: int
    height: int

class Renderer(GObject.Object):
    """
    :Constructors:

    ::

        Renderer(**properties)

    Object PangoRenderer

    Signals from GObject:
      notify (GParam)
    """
    @property
    def parent_instance(self) -> GObject.Object: ...
    @property
    def underline(self) -> Underline: ...
    @property
    def strikethrough(self) -> bool: ...
    @property
    def active_count(self) -> int: ...
    @property
    def matrix(self) -> Matrix: ...
    @property
    def priv(self) -> RendererPrivate: ...
    def activate(self) -> None: ...
    def deactivate(self) -> None: ...
    def do_begin(self) -> None: ...
    def do_draw_error_underline(
        self, x: int, y: int, width: int, height: int, /
    ) -> None: ...
    def do_draw_glyph(self, font: Font, glyph: int, x: float, y: float, /) -> None: ...
    def do_draw_glyph_item(
        self, text: str | None, glyph_item: GlyphItem, x: int, y: int, /
    ) -> None: ...
    def do_draw_glyphs(
        self, font: Font, glyphs: GlyphString, x: int, y: int, /
    ) -> None: ...
    def do_draw_rectangle(
        self, part: _RenderPartValueType, x: int, y: int, width: int, height: int, /
    ) -> None: ...
    def do_draw_shape(self, attr: AttrShape, x: int, y: int, /) -> None: ...
    def do_draw_trapezoid(
        self,
        part: _RenderPartValueType,
        y1_: float,
        x11: float,
        x21: float,
        y2: float,
        x12: float,
        x22: float,
        /,
    ) -> None: ...
    def do_end(self) -> None: ...
    def do_part_changed(self, part: _RenderPartValueType, /) -> None: ...
    def do_prepare_run(self, run: GlyphItem, /) -> None: ...
    def draw_error_underline(self, x: int, y: int, width: int, height: int) -> None: ...
    def draw_glyph(self, font: Font, glyph: int, x: float, y: float) -> None: ...
    def draw_glyph_item(
        self, text: str | None, glyph_item: GlyphItem, x: int, y: int
    ) -> None: ...
    def draw_glyphs(self, font: Font, glyphs: GlyphString, x: int, y: int) -> None: ...
    def draw_layout(self, layout: Layout, x: int, y: int) -> None: ...
    def draw_layout_line(self, line: LayoutLine, x: int, y: int) -> None: ...
    def draw_rectangle(
        self, part: _RenderPartValueType, x: int, y: int, width: int, height: int
    ) -> None: ...
    def draw_trapezoid(
        self,
        part: _RenderPartValueType,
        y1_: float,
        x11: float,
        x21: float,
        y2: float,
        x12: float,
        x22: float,
    ) -> None: ...
    def get_alpha(self, part: _RenderPartValueType) -> int: ...
    def get_color(self, part: _RenderPartValueType) -> Color | None: ...
    def get_layout(self) -> Layout | None: ...
    def get_layout_line(self) -> LayoutLine | None: ...
    def get_matrix(self) -> Matrix | None: ...
    def part_changed(self, part: _RenderPartValueType) -> None: ...
    def set_alpha(self, part: _RenderPartValueType, alpha: int) -> None: ...
    def set_color(
        self, part: _RenderPartValueType, color: Color | None = None
    ) -> None: ...
    def set_matrix(self, matrix: Matrix | None = None) -> None: ...

class RendererClass(_gi.Struct):
    """
    :Constructors:

    ::

        RendererClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...
    @property
    def draw_glyphs(
        self,
    ) -> Callable[[Renderer, Font, GlyphString, int, int], None]: ...
    @property
    def draw_rectangle(
        self,
    ) -> Callable[[Renderer, _RenderPartValueType, int, int, int, int], None]: ...
    @property
    def draw_error_underline(
        self,
    ) -> Callable[[Renderer, int, int, int, int], None]: ...
    @property
    def draw_shape(self) -> Callable[[Renderer, AttrShape, int, int], None]: ...
    @property
    def draw_trapezoid(
        self,
    ) -> Callable[
        [Renderer, _RenderPartValueType, float, float, float, float, float, float], None
    ]: ...
    @property
    def draw_glyph(self) -> Callable[[Renderer, Font, int, float, float], None]: ...
    @property
    def part_changed(self) -> Callable[[Renderer, _RenderPartValueType], None]: ...
    @property
    def begin(self) -> Callable[[Renderer], None]: ...
    @property
    def end(self) -> Callable[[Renderer], None]: ...
    @property
    def prepare_run(self) -> Callable[[Renderer, GlyphItem], None]: ...
    @property
    def draw_glyph_item(
        self,
    ) -> Callable[[Renderer, str | None, GlyphItem, int, int], None]: ...

class RendererPrivate(_gi.Struct): ...

class ScriptIter(GObject.GBoxed):
    """
    :Constructors:

    ::

        new(text:str, length:int) -> Pango.ScriptIter
    """
    def __init__(self, text: str, length: int) -> None: ...
    def free(self) -> None: ...
    def get_range(self) -> tuple[str, str, Script]: ...
    @classmethod
    def new(cls, text: str, length: int) -> ScriptIter: ...
    def next(self) -> bool: ...

class TabArray(GObject.GBoxed):
    """
    :Constructors:

    ::

        new(initial_size:int, positions_in_pixels:bool) -> Pango.TabArray
    """
    def __init__(self, initial_size: int, positions_in_pixels: bool) -> None: ...
    def copy(self) -> TabArray: ...
    def free(self) -> None: ...
    @staticmethod
    def from_string(text: str) -> TabArray | None: ...
    def get_decimal_point(self, tab_index: int) -> str: ...
    def get_positions_in_pixels(self) -> bool: ...
    def get_size(self) -> int: ...
    def get_tab(self, tab_index: int) -> tuple[TabAlign, int]: ...
    def get_tabs(self) -> tuple[TabAlign, list[int]]: ...
    @classmethod
    def new(cls, initial_size: int, positions_in_pixels: bool) -> TabArray: ...
    def resize(self, new_size: int) -> None: ...
    def set_decimal_point(self, tab_index: int, decimal_point: str) -> None: ...
    def set_positions_in_pixels(self, positions_in_pixels: bool) -> None: ...
    def set_tab(
        self, tab_index: int, alignment: _TabAlignValueType, location: int
    ) -> None: ...
    def sort(self) -> None: ...
    def to_string(self) -> str: ...

class FontMask(GObject.GFlags):
    COLOR = 512
    FAMILY = 1
    FEATURES = 256
    GRAVITY = 64
    SIZE = 32
    STRETCH = 16
    STYLE = 2
    VARIANT = 4
    VARIATIONS = 128
    WEIGHT = 8

_FontMaskLiteralType: TypeAlias = Literal[
    "PANGO_FONT_MASK_COLOR",
    "PANGO_FONT_MASK_FAMILY",
    "PANGO_FONT_MASK_FEATURES",
    "PANGO_FONT_MASK_GRAVITY",
    "PANGO_FONT_MASK_SIZE",
    "PANGO_FONT_MASK_STRETCH",
    "PANGO_FONT_MASK_STYLE",
    "PANGO_FONT_MASK_VARIANT",
    "PANGO_FONT_MASK_VARIATIONS",
    "PANGO_FONT_MASK_WEIGHT",
    "color",
    "family",
    "features",
    "gravity",
    "size",
    "stretch",
    "style",
    "variant",
    "variations",
    "weight",
]
_FontMaskValueType: TypeAlias = (
    FontMask | _FontMaskLiteralType | tuple[_FontMaskLiteralType, ...]
)

class LayoutDeserializeFlags(GObject.GFlags):
    CONTEXT = 1
    DEFAULT = 0

_LayoutDeserializeFlagsLiteralType: TypeAlias = Literal[
    "PANGO_LAYOUT_DESERIALIZE_CONTEXT",
    "PANGO_LAYOUT_DESERIALIZE_DEFAULT",
    "context",
    "default",
]
_LayoutDeserializeFlagsValueType: TypeAlias = (
    LayoutDeserializeFlags
    | _LayoutDeserializeFlagsLiteralType
    | tuple[_LayoutDeserializeFlagsLiteralType, ...]
)

class LayoutSerializeFlags(GObject.GFlags):
    CONTEXT = 1
    DEFAULT = 0
    OUTPUT = 2

_LayoutSerializeFlagsLiteralType: TypeAlias = Literal[
    "PANGO_LAYOUT_SERIALIZE_CONTEXT",
    "PANGO_LAYOUT_SERIALIZE_DEFAULT",
    "PANGO_LAYOUT_SERIALIZE_OUTPUT",
    "context",
    "default",
    "output",
]
_LayoutSerializeFlagsValueType: TypeAlias = (
    LayoutSerializeFlags
    | _LayoutSerializeFlagsLiteralType
    | tuple[_LayoutSerializeFlagsLiteralType, ...]
)

class ShapeFlags(GObject.GFlags):
    NONE = 0
    ROUND_POSITIONS = 1

_ShapeFlagsLiteralType: TypeAlias = Literal[
    "PANGO_SHAPE_NONE", "PANGO_SHAPE_ROUND_POSITIONS", "none", "round-positions"
]
_ShapeFlagsValueType: TypeAlias = (
    ShapeFlags | _ShapeFlagsLiteralType | tuple[_ShapeFlagsLiteralType, ...]
)

class ShowFlags(GObject.GFlags):
    IGNORABLES = 4
    LINE_BREAKS = 2
    NONE = 0
    SPACES = 1

_ShowFlagsLiteralType: TypeAlias = Literal[
    "PANGO_SHOW_IGNORABLES",
    "PANGO_SHOW_LINE_BREAKS",
    "PANGO_SHOW_NONE",
    "PANGO_SHOW_SPACES",
    "ignorables",
    "line-breaks",
    "none",
    "spaces",
]
_ShowFlagsValueType: TypeAlias = (
    ShowFlags | _ShowFlagsLiteralType | tuple[_ShowFlagsLiteralType, ...]
)

class Alignment(GObject.GEnum):
    CENTER = 1
    LEFT = 0
    RIGHT = 2

_AlignmentLiteralType: TypeAlias = Literal[
    "PANGO_ALIGN_CENTER",
    "PANGO_ALIGN_LEFT",
    "PANGO_ALIGN_RIGHT",
    "center",
    "left",
    "right",
]
_AlignmentValueType: TypeAlias = Alignment | _AlignmentLiteralType

class AttrType(GObject.GEnum):
    ABSOLUTE_LINE_HEIGHT = 32
    ABSOLUTE_SIZE = 20
    ALLOW_BREAKS = 26
    BACKGROUND = 10
    BACKGROUND_ALPHA = 25
    BASELINE_SHIFT = 36
    FALLBACK = 16
    FAMILY = 2
    FONT_DESC = 8
    FONT_FEATURES = 23
    FONT_SCALE = 37
    FOREGROUND = 9
    FOREGROUND_ALPHA = 24
    GRAVITY = 21
    GRAVITY_HINT = 22
    INSERT_HYPHENS = 28
    INVALID = 0
    LANGUAGE = 1
    LETTER_SPACING = 17
    LINE_HEIGHT = 31
    OVERLINE = 29
    OVERLINE_COLOR = 30
    RISE = 13
    SCALE = 15
    SENTENCE = 35
    SHAPE = 14
    SHOW = 27
    SIZE = 7
    STRETCH = 6
    STRIKETHROUGH = 12
    STRIKETHROUGH_COLOR = 19
    STYLE = 3
    TEXT_TRANSFORM = 33
    UNDERLINE = 11
    UNDERLINE_COLOR = 18
    VARIANT = 5
    WEIGHT = 4
    WORD = 34
    @staticmethod
    def get_name(type: _AttrTypeValueType) -> str | None: ...
    @staticmethod
    def register(name: str) -> AttrType: ...

_AttrTypeLiteralType: TypeAlias = Literal[
    "PANGO_ATTR_ABSOLUTE_LINE_HEIGHT",
    "PANGO_ATTR_ABSOLUTE_SIZE",
    "PANGO_ATTR_ALLOW_BREAKS",
    "PANGO_ATTR_BACKGROUND",
    "PANGO_ATTR_BACKGROUND_ALPHA",
    "PANGO_ATTR_BASELINE_SHIFT",
    "PANGO_ATTR_FALLBACK",
    "PANGO_ATTR_FAMILY",
    "PANGO_ATTR_FONT_DESC",
    "PANGO_ATTR_FONT_FEATURES",
    "PANGO_ATTR_FONT_SCALE",
    "PANGO_ATTR_FOREGROUND",
    "PANGO_ATTR_FOREGROUND_ALPHA",
    "PANGO_ATTR_GRAVITY",
    "PANGO_ATTR_GRAVITY_HINT",
    "PANGO_ATTR_INSERT_HYPHENS",
    "PANGO_ATTR_INVALID",
    "PANGO_ATTR_LANGUAGE",
    "PANGO_ATTR_LETTER_SPACING",
    "PANGO_ATTR_LINE_HEIGHT",
    "PANGO_ATTR_OVERLINE",
    "PANGO_ATTR_OVERLINE_COLOR",
    "PANGO_ATTR_RISE",
    "PANGO_ATTR_SCALE",
    "PANGO_ATTR_SENTENCE",
    "PANGO_ATTR_SHAPE",
    "PANGO_ATTR_SHOW",
    "PANGO_ATTR_SIZE",
    "PANGO_ATTR_STRETCH",
    "PANGO_ATTR_STRIKETHROUGH",
    "PANGO_ATTR_STRIKETHROUGH_COLOR",
    "PANGO_ATTR_STYLE",
    "PANGO_ATTR_TEXT_TRANSFORM",
    "PANGO_ATTR_UNDERLINE",
    "PANGO_ATTR_UNDERLINE_COLOR",
    "PANGO_ATTR_VARIANT",
    "PANGO_ATTR_WEIGHT",
    "PANGO_ATTR_WORD",
    "absolute-line-height",
    "absolute-size",
    "allow-breaks",
    "background",
    "background-alpha",
    "baseline-shift",
    "fallback",
    "family",
    "font-desc",
    "font-features",
    "font-scale",
    "foreground",
    "foreground-alpha",
    "gravity",
    "gravity-hint",
    "insert-hyphens",
    "invalid",
    "language",
    "letter-spacing",
    "line-height",
    "overline",
    "overline-color",
    "rise",
    "scale",
    "sentence",
    "shape",
    "show",
    "size",
    "stretch",
    "strikethrough",
    "strikethrough-color",
    "style",
    "text-transform",
    "underline",
    "underline-color",
    "variant",
    "weight",
    "word",
]
_AttrTypeValueType: TypeAlias = AttrType | _AttrTypeLiteralType

class BaselineShift(GObject.GEnum):
    NONE = 0
    SUBSCRIPT = 2
    SUPERSCRIPT = 1

_BaselineShiftLiteralType: TypeAlias = Literal[
    "PANGO_BASELINE_SHIFT_NONE",
    "PANGO_BASELINE_SHIFT_SUBSCRIPT",
    "PANGO_BASELINE_SHIFT_SUPERSCRIPT",
    "none",
    "subscript",
    "superscript",
]
_BaselineShiftValueType: TypeAlias = BaselineShift | _BaselineShiftLiteralType

class BidiType(GObject.GEnum):
    AL = 4
    AN = 11
    B = 15
    BN = 14
    CS = 12
    EN = 8
    ES = 9
    ET = 10
    FSI = 21
    L = 0
    LRE = 1
    LRI = 19
    LRO = 2
    NSM = 13
    ON = 18
    PDF = 7
    PDI = 22
    R = 3
    RLE = 5
    RLI = 20
    RLO = 6
    S = 16
    WS = 17
    @staticmethod
    def for_unichar(ch: str) -> BidiType: ...

_BidiTypeLiteralType: TypeAlias = Literal[
    "PANGO_BIDI_TYPE_AL",
    "PANGO_BIDI_TYPE_AN",
    "PANGO_BIDI_TYPE_B",
    "PANGO_BIDI_TYPE_BN",
    "PANGO_BIDI_TYPE_CS",
    "PANGO_BIDI_TYPE_EN",
    "PANGO_BIDI_TYPE_ES",
    "PANGO_BIDI_TYPE_ET",
    "PANGO_BIDI_TYPE_FSI",
    "PANGO_BIDI_TYPE_L",
    "PANGO_BIDI_TYPE_LRE",
    "PANGO_BIDI_TYPE_LRI",
    "PANGO_BIDI_TYPE_LRO",
    "PANGO_BIDI_TYPE_NSM",
    "PANGO_BIDI_TYPE_ON",
    "PANGO_BIDI_TYPE_PDF",
    "PANGO_BIDI_TYPE_PDI",
    "PANGO_BIDI_TYPE_R",
    "PANGO_BIDI_TYPE_RLE",
    "PANGO_BIDI_TYPE_RLI",
    "PANGO_BIDI_TYPE_RLO",
    "PANGO_BIDI_TYPE_S",
    "PANGO_BIDI_TYPE_WS",
    "al",
    "an",
    "b",
    "bn",
    "cs",
    "en",
    "es",
    "et",
    "fsi",
    "l",
    "lre",
    "lri",
    "lro",
    "nsm",
    "on",
    "pdf",
    "pdi",
    "r",
    "rle",
    "rli",
    "rlo",
    "s",
    "ws",
]
_BidiTypeValueType: TypeAlias = BidiType | _BidiTypeLiteralType

class CoverageLevel(GObject.GEnum):
    APPROXIMATE = 2
    EXACT = 3
    FALLBACK = 1
    NONE = 0

_CoverageLevelLiteralType: TypeAlias = Literal[
    "PANGO_COVERAGE_APPROXIMATE",
    "PANGO_COVERAGE_EXACT",
    "PANGO_COVERAGE_FALLBACK",
    "PANGO_COVERAGE_NONE",
    "approximate",
    "exact",
    "fallback",
    "none",
]
_CoverageLevelValueType: TypeAlias = CoverageLevel | _CoverageLevelLiteralType

class Direction(GObject.GEnum):
    LTR = 0
    NEUTRAL = 6
    RTL = 1
    TTB_LTR = 2
    TTB_RTL = 3
    WEAK_LTR = 4
    WEAK_RTL = 5

_DirectionLiteralType: TypeAlias = Literal[
    "PANGO_DIRECTION_LTR",
    "PANGO_DIRECTION_NEUTRAL",
    "PANGO_DIRECTION_RTL",
    "PANGO_DIRECTION_TTB_LTR",
    "PANGO_DIRECTION_TTB_RTL",
    "PANGO_DIRECTION_WEAK_LTR",
    "PANGO_DIRECTION_WEAK_RTL",
    "ltr",
    "neutral",
    "rtl",
    "ttb-ltr",
    "ttb-rtl",
    "weak-ltr",
    "weak-rtl",
]
_DirectionValueType: TypeAlias = Direction | _DirectionLiteralType

class EllipsizeMode(GObject.GEnum):
    END = 3
    MIDDLE = 2
    NONE = 0
    START = 1

_EllipsizeModeLiteralType: TypeAlias = Literal[
    "PANGO_ELLIPSIZE_END",
    "PANGO_ELLIPSIZE_MIDDLE",
    "PANGO_ELLIPSIZE_NONE",
    "PANGO_ELLIPSIZE_START",
    "end",
    "middle",
    "none",
    "start",
]
_EllipsizeModeValueType: TypeAlias = EllipsizeMode | _EllipsizeModeLiteralType

class FontColor(GObject.GEnum):
    DONT_CARE = 2
    FORBIDDEN = 0
    REQUIRED = 1

_FontColorLiteralType: TypeAlias = Literal[
    "PANGO_FONT_COLOR_DONT_CARE",
    "PANGO_FONT_COLOR_FORBIDDEN",
    "PANGO_FONT_COLOR_REQUIRED",
    "dont-care",
    "forbidden",
    "required",
]
_FontColorValueType: TypeAlias = FontColor | _FontColorLiteralType

class FontScale(GObject.GEnum):
    NONE = 0
    SMALL_CAPS = 3
    SUBSCRIPT = 2
    SUPERSCRIPT = 1

_FontScaleLiteralType: TypeAlias = Literal[
    "PANGO_FONT_SCALE_NONE",
    "PANGO_FONT_SCALE_SMALL_CAPS",
    "PANGO_FONT_SCALE_SUBSCRIPT",
    "PANGO_FONT_SCALE_SUPERSCRIPT",
    "none",
    "small-caps",
    "subscript",
    "superscript",
]
_FontScaleValueType: TypeAlias = FontScale | _FontScaleLiteralType

class Gravity(GObject.GEnum):
    AUTO = 4
    EAST = 1
    NORTH = 2
    SOUTH = 0
    WEST = 3
    @staticmethod
    def get_for_matrix(matrix: Matrix | None = None) -> Gravity: ...
    @staticmethod
    def get_for_script(
        script: _ScriptValueType,
        base_gravity: _GravityValueType,
        hint: _GravityHintValueType,
    ) -> Gravity: ...
    @staticmethod
    def get_for_script_and_width(
        script: _ScriptValueType,
        wide: bool,
        base_gravity: _GravityValueType,
        hint: _GravityHintValueType,
    ) -> Gravity: ...
    @staticmethod
    def to_rotation(gravity: _GravityValueType) -> float: ...

_GravityLiteralType: TypeAlias = Literal[
    "PANGO_GRAVITY_AUTO",
    "PANGO_GRAVITY_EAST",
    "PANGO_GRAVITY_NORTH",
    "PANGO_GRAVITY_SOUTH",
    "PANGO_GRAVITY_WEST",
    "auto",
    "east",
    "north",
    "south",
    "west",
]
_GravityValueType: TypeAlias = Gravity | _GravityLiteralType

class GravityHint(GObject.GEnum):
    LINE = 2
    NATURAL = 0
    STRONG = 1

_GravityHintLiteralType: TypeAlias = Literal[
    "PANGO_GRAVITY_HINT_LINE",
    "PANGO_GRAVITY_HINT_NATURAL",
    "PANGO_GRAVITY_HINT_STRONG",
    "line",
    "natural",
    "strong",
]
_GravityHintValueType: TypeAlias = GravityHint | _GravityHintLiteralType

class LayoutDeserializeError(GObject.GEnum):
    INVALID = 0
    INVALID_VALUE = 1
    MISSING_VALUE = 2
    @staticmethod
    def quark() -> int: ...

_LayoutDeserializeErrorLiteralType: TypeAlias = Literal[
    "PANGO_LAYOUT_DESERIALIZE_INVALID",
    "PANGO_LAYOUT_DESERIALIZE_INVALID_VALUE",
    "PANGO_LAYOUT_DESERIALIZE_MISSING_VALUE",
    "invalid",
    "invalid-value",
    "missing-value",
]
_LayoutDeserializeErrorValueType: TypeAlias = (
    LayoutDeserializeError | _LayoutDeserializeErrorLiteralType
)

class Overline(GObject.GEnum):
    NONE = 0
    SINGLE = 1

_OverlineLiteralType: TypeAlias = Literal[
    "PANGO_OVERLINE_NONE", "PANGO_OVERLINE_SINGLE", "none", "single"
]
_OverlineValueType: TypeAlias = Overline | _OverlineLiteralType

class RenderPart(GObject.GEnum):
    BACKGROUND = 1
    FOREGROUND = 0
    OVERLINE = 4
    STRIKETHROUGH = 3
    UNDERLINE = 2

_RenderPartLiteralType: TypeAlias = Literal[
    "PANGO_RENDER_PART_BACKGROUND",
    "PANGO_RENDER_PART_FOREGROUND",
    "PANGO_RENDER_PART_OVERLINE",
    "PANGO_RENDER_PART_STRIKETHROUGH",
    "PANGO_RENDER_PART_UNDERLINE",
    "background",
    "foreground",
    "overline",
    "strikethrough",
    "underline",
]
_RenderPartValueType: TypeAlias = RenderPart | _RenderPartLiteralType

class Script(GObject.GEnum):
    AHOM = 111
    ANATOLIAN_HIEROGLYPHS = 112
    ARABIC = 2
    ARMENIAN = 3
    BALINESE = 62
    BASSA_VAH = 88
    BATAK = 78
    BENGALI = 4
    BOPOMOFO = 5
    BRAHMI = 79
    BRAILLE = 46
    BUGINESE = 55
    BUHID = 44
    CANADIAN_ABORIGINAL = 40
    CARIAN = 75
    CAUCASIAN_ALBANIAN = 89
    CHAKMA = 81
    CHAM = 72
    CHEROKEE = 6
    COMMON = 0
    COPTIC = 7
    CUNEIFORM = 63
    CYPRIOT = 47
    CYRILLIC = 8
    DESERET = 9
    DEVANAGARI = 10
    DUPLOYAN = 90
    ELBASAN = 91
    ETHIOPIC = 11
    GEORGIAN = 12
    GLAGOLITIC = 56
    GOTHIC = 13
    GRANTHA = 92
    GREEK = 14
    GUJARATI = 15
    GURMUKHI = 16
    HAN = 17
    HANGUL = 18
    HANUNOO = 43
    HATRAN = 113
    HEBREW = 19
    HIRAGANA = 20
    INHERITED = 1
    INVALID_CODE = -1
    KANNADA = 21
    KATAKANA = 22
    KAYAH_LI = 67
    KHAROSHTHI = 60
    KHMER = 23
    KHOJKI = 93
    KHUDAWADI = 94
    LAO = 24
    LATIN = 25
    LEPCHA = 68
    LIMBU = 48
    LINEAR_A = 95
    LINEAR_B = 51
    LYCIAN = 76
    LYDIAN = 77
    MAHAJANI = 96
    MALAYALAM = 26
    MANDAIC = 80
    MANICHAEAN = 97
    MENDE_KIKAKUI = 98
    MEROITIC_CURSIVE = 82
    MEROITIC_HIEROGLYPHS = 83
    MIAO = 84
    MODI = 99
    MONGOLIAN = 27
    MRO = 100
    MULTANI = 114
    MYANMAR = 28
    NABATAEAN = 101
    NEW_TAI_LUE = 54
    NKO = 66
    OGHAM = 29
    OLD_HUNGARIAN = 115
    OLD_ITALIC = 30
    OLD_NORTH_ARABIAN = 102
    OLD_PERMIC = 103
    OLD_PERSIAN = 59
    OL_CHIKI = 73
    ORIYA = 31
    OSMANYA = 49
    PAHAWH_HMONG = 104
    PALMYRENE = 105
    PAU_CIN_HAU = 106
    PHAGS_PA = 65
    PHOENICIAN = 64
    PSALTER_PAHLAVI = 107
    REJANG = 69
    RUNIC = 32
    SAURASHTRA = 71
    SHARADA = 85
    SHAVIAN = 50
    SIDDHAM = 108
    SIGNWRITING = 116
    SINHALA = 33
    SORA_SOMPENG = 86
    SUNDANESE = 70
    SYLOTI_NAGRI = 58
    SYRIAC = 34
    TAGALOG = 42
    TAGBANWA = 45
    TAI_LE = 52
    TAKRI = 87
    TAMIL = 35
    TELUGU = 36
    THAANA = 37
    THAI = 38
    TIBETAN = 39
    TIFINAGH = 57
    TIRHUTA = 109
    UGARITIC = 53
    UNKNOWN = 61
    VAI = 74
    WARANG_CITI = 110
    YI = 41
    @staticmethod
    def for_unichar(ch: str) -> Script: ...
    @staticmethod
    def get_sample_language(script: _ScriptValueType) -> Language | None: ...

_ScriptLiteralType: TypeAlias = Literal[
    "PANGO_SCRIPT_AHOM",
    "PANGO_SCRIPT_ANATOLIAN_HIEROGLYPHS",
    "PANGO_SCRIPT_ARABIC",
    "PANGO_SCRIPT_ARMENIAN",
    "PANGO_SCRIPT_BALINESE",
    "PANGO_SCRIPT_BASSA_VAH",
    "PANGO_SCRIPT_BATAK",
    "PANGO_SCRIPT_BENGALI",
    "PANGO_SCRIPT_BOPOMOFO",
    "PANGO_SCRIPT_BRAHMI",
    "PANGO_SCRIPT_BRAILLE",
    "PANGO_SCRIPT_BUGINESE",
    "PANGO_SCRIPT_BUHID",
    "PANGO_SCRIPT_CANADIAN_ABORIGINAL",
    "PANGO_SCRIPT_CARIAN",
    "PANGO_SCRIPT_CAUCASIAN_ALBANIAN",
    "PANGO_SCRIPT_CHAKMA",
    "PANGO_SCRIPT_CHAM",
    "PANGO_SCRIPT_CHEROKEE",
    "PANGO_SCRIPT_COMMON",
    "PANGO_SCRIPT_COPTIC",
    "PANGO_SCRIPT_CUNEIFORM",
    "PANGO_SCRIPT_CYPRIOT",
    "PANGO_SCRIPT_CYRILLIC",
    "PANGO_SCRIPT_DESERET",
    "PANGO_SCRIPT_DEVANAGARI",
    "PANGO_SCRIPT_DUPLOYAN",
    "PANGO_SCRIPT_ELBASAN",
    "PANGO_SCRIPT_ETHIOPIC",
    "PANGO_SCRIPT_GEORGIAN",
    "PANGO_SCRIPT_GLAGOLITIC",
    "PANGO_SCRIPT_GOTHIC",
    "PANGO_SCRIPT_GRANTHA",
    "PANGO_SCRIPT_GREEK",
    "PANGO_SCRIPT_GUJARATI",
    "PANGO_SCRIPT_GURMUKHI",
    "PANGO_SCRIPT_HAN",
    "PANGO_SCRIPT_HANGUL",
    "PANGO_SCRIPT_HANUNOO",
    "PANGO_SCRIPT_HATRAN",
    "PANGO_SCRIPT_HEBREW",
    "PANGO_SCRIPT_HIRAGANA",
    "PANGO_SCRIPT_INHERITED",
    "PANGO_SCRIPT_INVALID_CODE",
    "PANGO_SCRIPT_KANNADA",
    "PANGO_SCRIPT_KATAKANA",
    "PANGO_SCRIPT_KAYAH_LI",
    "PANGO_SCRIPT_KHAROSHTHI",
    "PANGO_SCRIPT_KHMER",
    "PANGO_SCRIPT_KHOJKI",
    "PANGO_SCRIPT_KHUDAWADI",
    "PANGO_SCRIPT_LAO",
    "PANGO_SCRIPT_LATIN",
    "PANGO_SCRIPT_LEPCHA",
    "PANGO_SCRIPT_LIMBU",
    "PANGO_SCRIPT_LINEAR_A",
    "PANGO_SCRIPT_LINEAR_B",
    "PANGO_SCRIPT_LYCIAN",
    "PANGO_SCRIPT_LYDIAN",
    "PANGO_SCRIPT_MAHAJANI",
    "PANGO_SCRIPT_MALAYALAM",
    "PANGO_SCRIPT_MANDAIC",
    "PANGO_SCRIPT_MANICHAEAN",
    "PANGO_SCRIPT_MENDE_KIKAKUI",
    "PANGO_SCRIPT_MEROITIC_CURSIVE",
    "PANGO_SCRIPT_MEROITIC_HIEROGLYPHS",
    "PANGO_SCRIPT_MIAO",
    "PANGO_SCRIPT_MODI",
    "PANGO_SCRIPT_MONGOLIAN",
    "PANGO_SCRIPT_MRO",
    "PANGO_SCRIPT_MULTANI",
    "PANGO_SCRIPT_MYANMAR",
    "PANGO_SCRIPT_NABATAEAN",
    "PANGO_SCRIPT_NEW_TAI_LUE",
    "PANGO_SCRIPT_NKO",
    "PANGO_SCRIPT_OGHAM",
    "PANGO_SCRIPT_OLD_HUNGARIAN",
    "PANGO_SCRIPT_OLD_ITALIC",
    "PANGO_SCRIPT_OLD_NORTH_ARABIAN",
    "PANGO_SCRIPT_OLD_PERMIC",
    "PANGO_SCRIPT_OLD_PERSIAN",
    "PANGO_SCRIPT_OL_CHIKI",
    "PANGO_SCRIPT_ORIYA",
    "PANGO_SCRIPT_OSMANYA",
    "PANGO_SCRIPT_PAHAWH_HMONG",
    "PANGO_SCRIPT_PALMYRENE",
    "PANGO_SCRIPT_PAU_CIN_HAU",
    "PANGO_SCRIPT_PHAGS_PA",
    "PANGO_SCRIPT_PHOENICIAN",
    "PANGO_SCRIPT_PSALTER_PAHLAVI",
    "PANGO_SCRIPT_REJANG",
    "PANGO_SCRIPT_RUNIC",
    "PANGO_SCRIPT_SAURASHTRA",
    "PANGO_SCRIPT_SHARADA",
    "PANGO_SCRIPT_SHAVIAN",
    "PANGO_SCRIPT_SIDDHAM",
    "PANGO_SCRIPT_SIGNWRITING",
    "PANGO_SCRIPT_SINHALA",
    "PANGO_SCRIPT_SORA_SOMPENG",
    "PANGO_SCRIPT_SUNDANESE",
    "PANGO_SCRIPT_SYLOTI_NAGRI",
    "PANGO_SCRIPT_SYRIAC",
    "PANGO_SCRIPT_TAGALOG",
    "PANGO_SCRIPT_TAGBANWA",
    "PANGO_SCRIPT_TAI_LE",
    "PANGO_SCRIPT_TAKRI",
    "PANGO_SCRIPT_TAMIL",
    "PANGO_SCRIPT_TELUGU",
    "PANGO_SCRIPT_THAANA",
    "PANGO_SCRIPT_THAI",
    "PANGO_SCRIPT_TIBETAN",
    "PANGO_SCRIPT_TIFINAGH",
    "PANGO_SCRIPT_TIRHUTA",
    "PANGO_SCRIPT_UGARITIC",
    "PANGO_SCRIPT_UNKNOWN",
    "PANGO_SCRIPT_VAI",
    "PANGO_SCRIPT_WARANG_CITI",
    "PANGO_SCRIPT_YI",
    "ahom",
    "anatolian-hieroglyphs",
    "arabic",
    "armenian",
    "balinese",
    "bassa-vah",
    "batak",
    "bengali",
    "bopomofo",
    "brahmi",
    "braille",
    "buginese",
    "buhid",
    "canadian-aboriginal",
    "carian",
    "caucasian-albanian",
    "chakma",
    "cham",
    "cherokee",
    "common",
    "coptic",
    "cuneiform",
    "cypriot",
    "cyrillic",
    "deseret",
    "devanagari",
    "duployan",
    "elbasan",
    "ethiopic",
    "georgian",
    "glagolitic",
    "gothic",
    "grantha",
    "greek",
    "gujarati",
    "gurmukhi",
    "han",
    "hangul",
    "hanunoo",
    "hatran",
    "hebrew",
    "hiragana",
    "inherited",
    "invalid-code",
    "kannada",
    "katakana",
    "kayah-li",
    "kharoshthi",
    "khmer",
    "khojki",
    "khudawadi",
    "lao",
    "latin",
    "lepcha",
    "limbu",
    "linear-a",
    "linear-b",
    "lycian",
    "lydian",
    "mahajani",
    "malayalam",
    "mandaic",
    "manichaean",
    "mende-kikakui",
    "meroitic-cursive",
    "meroitic-hieroglyphs",
    "miao",
    "modi",
    "mongolian",
    "mro",
    "multani",
    "myanmar",
    "nabataean",
    "new-tai-lue",
    "nko",
    "ogham",
    "ol-chiki",
    "old-hungarian",
    "old-italic",
    "old-north-arabian",
    "old-permic",
    "old-persian",
    "oriya",
    "osmanya",
    "pahawh-hmong",
    "palmyrene",
    "pau-cin-hau",
    "phags-pa",
    "phoenician",
    "psalter-pahlavi",
    "rejang",
    "runic",
    "saurashtra",
    "sharada",
    "shavian",
    "siddham",
    "signwriting",
    "sinhala",
    "sora-sompeng",
    "sundanese",
    "syloti-nagri",
    "syriac",
    "tagalog",
    "tagbanwa",
    "tai-le",
    "takri",
    "tamil",
    "telugu",
    "thaana",
    "thai",
    "tibetan",
    "tifinagh",
    "tirhuta",
    "ugaritic",
    "unknown",
    "vai",
    "warang-citi",
    "yi",
]
_ScriptValueType: TypeAlias = Script | _ScriptLiteralType

class Stretch(GObject.GEnum):
    CONDENSED = 2
    EXPANDED = 6
    EXTRA_CONDENSED = 1
    EXTRA_EXPANDED = 7
    NORMAL = 4
    SEMI_CONDENSED = 3
    SEMI_EXPANDED = 5
    ULTRA_CONDENSED = 0
    ULTRA_EXPANDED = 8

_StretchLiteralType: TypeAlias = Literal[
    "PANGO_STRETCH_CONDENSED",
    "PANGO_STRETCH_EXPANDED",
    "PANGO_STRETCH_EXTRA_CONDENSED",
    "PANGO_STRETCH_EXTRA_EXPANDED",
    "PANGO_STRETCH_NORMAL",
    "PANGO_STRETCH_SEMI_CONDENSED",
    "PANGO_STRETCH_SEMI_EXPANDED",
    "PANGO_STRETCH_ULTRA_CONDENSED",
    "PANGO_STRETCH_ULTRA_EXPANDED",
    "condensed",
    "expanded",
    "extra-condensed",
    "extra-expanded",
    "normal",
    "semi-condensed",
    "semi-expanded",
    "ultra-condensed",
    "ultra-expanded",
]
_StretchValueType: TypeAlias = Stretch | _StretchLiteralType

class Style(GObject.GEnum):
    ITALIC = 2
    NORMAL = 0
    OBLIQUE = 1

_StyleLiteralType: TypeAlias = Literal[
    "PANGO_STYLE_ITALIC",
    "PANGO_STYLE_NORMAL",
    "PANGO_STYLE_OBLIQUE",
    "italic",
    "normal",
    "oblique",
]
_StyleValueType: TypeAlias = Style | _StyleLiteralType

class TabAlign(GObject.GEnum):
    CENTER = 2
    DECIMAL = 3
    LEFT = 0
    RIGHT = 1

_TabAlignLiteralType: TypeAlias = Literal[
    "PANGO_TAB_CENTER",
    "PANGO_TAB_DECIMAL",
    "PANGO_TAB_LEFT",
    "PANGO_TAB_RIGHT",
    "center",
    "decimal",
    "left",
    "right",
]
_TabAlignValueType: TypeAlias = TabAlign | _TabAlignLiteralType

class TextTransform(GObject.GEnum):
    CAPITALIZE = 3
    LOWERCASE = 1
    NONE = 0
    UPPERCASE = 2

_TextTransformLiteralType: TypeAlias = Literal[
    "PANGO_TEXT_TRANSFORM_CAPITALIZE",
    "PANGO_TEXT_TRANSFORM_LOWERCASE",
    "PANGO_TEXT_TRANSFORM_NONE",
    "PANGO_TEXT_TRANSFORM_UPPERCASE",
    "capitalize",
    "lowercase",
    "none",
    "uppercase",
]
_TextTransformValueType: TypeAlias = TextTransform | _TextTransformLiteralType

class Underline(GObject.GEnum):
    DOUBLE = 2
    DOUBLE_LINE = 6
    ERROR = 4
    ERROR_LINE = 7
    LOW = 3
    NONE = 0
    SINGLE = 1
    SINGLE_LINE = 5

_UnderlineLiteralType: TypeAlias = Literal[
    "PANGO_UNDERLINE_DOUBLE",
    "PANGO_UNDERLINE_DOUBLE_LINE",
    "PANGO_UNDERLINE_ERROR",
    "PANGO_UNDERLINE_ERROR_LINE",
    "PANGO_UNDERLINE_LOW",
    "PANGO_UNDERLINE_NONE",
    "PANGO_UNDERLINE_SINGLE",
    "PANGO_UNDERLINE_SINGLE_LINE",
    "double",
    "double-line",
    "error",
    "error-line",
    "low",
    "none",
    "single",
    "single-line",
]
_UnderlineValueType: TypeAlias = Underline | _UnderlineLiteralType

class Variant(GObject.GEnum):
    ALL_PETITE_CAPS = 4
    ALL_SMALL_CAPS = 2
    NORMAL = 0
    PETITE_CAPS = 3
    SMALL_CAPS = 1
    TITLE_CAPS = 6
    UNICASE = 5

_VariantLiteralType: TypeAlias = Literal[
    "PANGO_VARIANT_ALL_PETITE_CAPS",
    "PANGO_VARIANT_ALL_SMALL_CAPS",
    "PANGO_VARIANT_NORMAL",
    "PANGO_VARIANT_PETITE_CAPS",
    "PANGO_VARIANT_SMALL_CAPS",
    "PANGO_VARIANT_TITLE_CAPS",
    "PANGO_VARIANT_UNICASE",
    "all-petite-caps",
    "all-small-caps",
    "normal",
    "petite-caps",
    "small-caps",
    "title-caps",
    "unicase",
]
_VariantValueType: TypeAlias = Variant | _VariantLiteralType

class Weight(GObject.GEnum):
    BOLD = 700
    BOOK = 380
    HEAVY = 900
    LIGHT = 300
    MEDIUM = 500
    NORMAL = 400
    SEMIBOLD = 600
    SEMILIGHT = 350
    THIN = 100
    ULTRABOLD = 800
    ULTRAHEAVY = 1000
    ULTRALIGHT = 200

_WeightLiteralType: TypeAlias = Literal[
    "PANGO_WEIGHT_BOLD",
    "PANGO_WEIGHT_BOOK",
    "PANGO_WEIGHT_HEAVY",
    "PANGO_WEIGHT_LIGHT",
    "PANGO_WEIGHT_MEDIUM",
    "PANGO_WEIGHT_NORMAL",
    "PANGO_WEIGHT_SEMIBOLD",
    "PANGO_WEIGHT_SEMILIGHT",
    "PANGO_WEIGHT_THIN",
    "PANGO_WEIGHT_ULTRABOLD",
    "PANGO_WEIGHT_ULTRAHEAVY",
    "PANGO_WEIGHT_ULTRALIGHT",
    "bold",
    "book",
    "heavy",
    "light",
    "medium",
    "normal",
    "semibold",
    "semilight",
    "thin",
    "ultrabold",
    "ultraheavy",
    "ultralight",
]
_WeightValueType: TypeAlias = Weight | _WeightLiteralType

class WrapMode(GObject.GEnum):
    CHAR = 1
    NONE = 3
    WORD = 0
    WORD_CHAR = 2

_WrapModeLiteralType: TypeAlias = Literal[
    "PANGO_WRAP_CHAR",
    "PANGO_WRAP_NONE",
    "PANGO_WRAP_WORD",
    "PANGO_WRAP_WORD_CHAR",
    "char",
    "none",
    "word",
    "word-char",
]
_WrapModeValueType: TypeAlias = WrapMode | _WrapModeLiteralType
