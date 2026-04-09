from typing import Any
from typing import TypeVar
from typing_extensions import Self

from collections.abc import Callable
from collections.abc import Sequence

import cairo
from gi import _gi
from gi.repository import _Gdk4
from gi.repository import GLib
from gi.repository import GObject
from gi.repository import Graphene
from gi.repository import Pango

T = TypeVar("T")
_SomeSurface = TypeVar("_SomeSurface", bound=cairo.Surface)

def component_transfer_equal(self: None, other: None) -> bool: ...
def path_parse(string: str) -> Path | None: ...
def serialization_error_quark() -> int: ...
def stroke_equal(stroke1: None, stroke2: None) -> bool: ...
def transform_parse(string: str) -> tuple[bool, Transform]: ...
def value_dup_render_node(value: Any) -> RenderNode | None: ...
def value_get_render_node(value: Any) -> RenderNode | None: ...
def value_set_render_node(value: Any, node: RenderNode) -> None: ...
def value_take_render_node(value: Any, node: RenderNode | None = None) -> None: ...

class BlendNode(RenderNode):
    """
    :Constructors:

    ::

        BlendNode(**properties)
        new(bottom:Gsk.RenderNode, top:Gsk.RenderNode, blend_mode:Gsk.BlendMode) -> Gsk.BlendNode
    """
    def get_blend_mode(self) -> BlendMode: ...
    def get_bottom_child(self) -> RenderNode: ...
    def get_top_child(self) -> RenderNode: ...
    @classmethod
    def new(
        cls, bottom: RenderNode, top: RenderNode, blend_mode: BlendMode
    ) -> BlendNode: ...

class BlurNode(RenderNode):
    """
    :Constructors:

    ::

        BlurNode(**properties)
        new(child:Gsk.RenderNode, radius:float) -> Gsk.BlurNode
    """
    def get_child(self) -> RenderNode: ...
    def get_radius(self) -> float: ...
    @classmethod
    def new(cls, child: RenderNode, radius: float) -> BlurNode: ...

class BorderNode(RenderNode):
    """
    :Constructors:

    ::

        BorderNode(**properties)
        new(outline:Gsk.RoundedRect, border_width:list, border_color:list) -> Gsk.BorderNode
    """
    def get_colors(self) -> list[_Gdk4.RGBA]: ...
    def get_outline(self) -> RoundedRect: ...
    def get_widths(self) -> list[float]: ...
    @classmethod
    def new(
        cls,
        outline: RoundedRect,
        border_width: Sequence[float],
        border_color: Sequence[_Gdk4.RGBA],
    ) -> BorderNode: ...

class CairoNode(RenderNode):
    """
    :Constructors:

    ::

        CairoNode(**properties)
        new(bounds:Graphene.Rect) -> Gsk.CairoNode
    """
    def get_draw_context(self) -> cairo.Context: ...
    def get_surface(self) -> cairo.Surface: ...
    @classmethod
    def new(cls, bounds: Graphene.Rect) -> CairoNode: ...

class CairoRenderer(Renderer):
    """
    :Constructors:

    ::

        CairoRenderer(**properties)
        new() -> Gsk.Renderer

    Object GskCairoRenderer

    Properties from GskRenderer:
      realized -> gboolean: realized
      surface -> GdkSurface: surface

    Signals from GObject:
      notify (GParam)
    """
    class Props(Renderer.Props):
        realized: bool
        surface: _Gdk4.Surface | None

    @property
    def props(self) -> Props: ...
    @classmethod
    def new(cls) -> CairoRenderer: ...

class CairoRendererClass(GObject.GPointer): ...

class ClipNode(RenderNode):
    """
    :Constructors:

    ::

        ClipNode(**properties)
        new(child:Gsk.RenderNode, clip:Graphene.Rect) -> Gsk.ClipNode
    """
    def get_child(self) -> RenderNode: ...
    def get_clip(self) -> Graphene.Rect: ...
    @classmethod
    def new(cls, child: RenderNode, clip: Graphene.Rect) -> ClipNode: ...

class ColorMatrixNode(RenderNode):
    """
    :Constructors:

    ::

        ColorMatrixNode(**properties)
        new(child:Gsk.RenderNode, color_matrix:Graphene.Matrix, color_offset:Graphene.Vec4) -> Gsk.ColorMatrixNode
    """
    def get_child(self) -> RenderNode: ...
    def get_color_matrix(self) -> Graphene.Matrix: ...
    def get_color_offset(self) -> Graphene.Vec4: ...
    @classmethod
    def new(
        cls,
        child: RenderNode,
        color_matrix: Graphene.Matrix,
        color_offset: Graphene.Vec4,
    ) -> ColorMatrixNode: ...

class ColorNode(RenderNode):
    """
    :Constructors:

    ::

        ColorNode(**properties)
        new(rgba:Gdk.RGBA, bounds:Graphene.Rect) -> Gsk.ColorNode
    """
    def get_color(self) -> _Gdk4.RGBA: ...
    @classmethod
    def new(cls, rgba: _Gdk4.RGBA, bounds: Graphene.Rect) -> ColorNode: ...

class ColorStop(GObject.GPointer):
    """
    :Constructors:

    ::

        ColorStop()
    """

    offset: float = ...
    color: _Gdk4.RGBA = ...

class ComponentTransfer(GObject.GBoxed):
    """
    :Constructors:

    ::

        new_discrete(values:list) -> Gsk.ComponentTransfer
        new_gamma(amp:float, exp:float, ofs:float) -> Gsk.ComponentTransfer
        new_identity() -> Gsk.ComponentTransfer
        new_levels(n:float) -> Gsk.ComponentTransfer
        new_linear(m:float, b:float) -> Gsk.ComponentTransfer
        new_table(values:list) -> Gsk.ComponentTransfer
    """
    def copy(self) -> ComponentTransfer: ...
    # override
    @staticmethod
    def equal(value1: None, value2: None) -> bool: ...
    def free(self) -> None: ...
    @classmethod
    def new_discrete(cls, values: Sequence[float]) -> ComponentTransfer: ...
    @classmethod
    def new_gamma(cls, amp: float, exp: float, ofs: float) -> ComponentTransfer: ...
    @classmethod
    def new_identity(cls) -> ComponentTransfer: ...
    @classmethod
    def new_levels(cls, n: float) -> ComponentTransfer: ...
    @classmethod
    def new_linear(cls, m: float, b: float) -> ComponentTransfer: ...
    @classmethod
    def new_table(cls, values: Sequence[float]) -> ComponentTransfer: ...

class ComponentTransferNode(RenderNode):
    """
    :Constructors:

    ::

        ComponentTransferNode(**properties)
        new(child:Gsk.RenderNode, r:Gsk.ComponentTransfer, g:Gsk.ComponentTransfer, b:Gsk.ComponentTransfer, a:Gsk.ComponentTransfer) -> Gsk.ComponentTransferNode
    """
    def get_child(self) -> RenderNode: ...
    def get_transfer(self, component: _Gdk4.ColorChannel) -> ComponentTransfer: ...
    @classmethod
    def new(
        cls,
        child: RenderNode,
        r: ComponentTransfer,
        g: ComponentTransfer,
        b: ComponentTransfer,
        a: ComponentTransfer,
    ) -> ComponentTransferNode: ...

class CompositeNode(RenderNode):
    """
    :Constructors:

    ::

        CompositeNode(**properties)
        new(child:Gsk.RenderNode, mask:Gsk.RenderNode, op:Gsk.PorterDuff) -> Gsk.CompositeNode
    """
    def get_child(self) -> RenderNode: ...
    def get_mask(self) -> RenderNode: ...
    def get_operator(self) -> PorterDuff: ...
    @classmethod
    def new(
        cls, child: RenderNode, mask: RenderNode, op: PorterDuff
    ) -> CompositeNode: ...

class ConicGradientNode(RenderNode):
    """
    :Constructors:

    ::

        ConicGradientNode(**properties)
        new(bounds:Graphene.Rect, center:Graphene.Point, rotation:float, color_stops:list) -> Gsk.ConicGradientNode
    """
    def get_angle(self) -> float: ...
    def get_center(self) -> Graphene.Point: ...
    def get_color_stops(self) -> list[ColorStop]: ...
    def get_n_color_stops(self) -> int: ...
    def get_rotation(self) -> float: ...
    @classmethod
    def new(
        cls,
        bounds: Graphene.Rect,
        center: Graphene.Point,
        rotation: float,
        color_stops: Sequence[ColorStop],
    ) -> ConicGradientNode: ...

class ContainerNode(RenderNode):
    """
    :Constructors:

    ::

        ContainerNode(**properties)
        new(children:list) -> Gsk.ContainerNode
    """
    def get_child(self, idx: int) -> RenderNode: ...
    def get_n_children(self) -> int: ...
    @classmethod
    def new(cls, children: Sequence[RenderNode]) -> ContainerNode: ...

class CopyNode(RenderNode):
    """
    :Constructors:

    ::

        CopyNode(**properties)
        new(child:Gsk.RenderNode) -> Gsk.CopyNode
    """
    def get_child(self) -> RenderNode: ...
    @classmethod
    def new(cls, child: RenderNode) -> CopyNode: ...

class CrossFadeNode(RenderNode):
    """
    :Constructors:

    ::

        CrossFadeNode(**properties)
        new(start:Gsk.RenderNode, end:Gsk.RenderNode, progress:float) -> Gsk.CrossFadeNode
    """
    def get_end_child(self) -> RenderNode: ...
    def get_progress(self) -> float: ...
    def get_start_child(self) -> RenderNode: ...
    @classmethod
    def new(
        cls, start: RenderNode, end: RenderNode, progress: float
    ) -> CrossFadeNode: ...

class DebugNode(RenderNode):
    """
    :Constructors:

    ::

        DebugNode(**properties)
        new(child:Gsk.RenderNode, message:str) -> Gsk.DebugNode
    """
    def get_child(self) -> RenderNode: ...
    def get_message(self) -> str: ...
    @classmethod
    def new(cls, child: RenderNode, message: str) -> DebugNode: ...

class FillNode(RenderNode):
    """
    :Constructors:

    ::

        FillNode(**properties)
        new(child:Gsk.RenderNode, path:Gsk.Path, fill_rule:Gsk.FillRule) -> Gsk.FillNode
    """
    def get_child(self) -> RenderNode: ...
    def get_fill_rule(self) -> FillRule: ...
    def get_path(self) -> Path: ...
    @classmethod
    def new(cls, child: RenderNode, path: Path, fill_rule: FillRule) -> FillNode: ...

class GLRenderer(Renderer):
    """
    :Constructors:

    ::

        GLRenderer(**properties)
        new() -> Gsk.Renderer

    Object GskGLRenderer

    Properties from GskRenderer:
      realized -> gboolean: realized
      surface -> GdkSurface: surface

    Signals from GObject:
      notify (GParam)
    """
    class Props(Renderer.Props):
        realized: bool
        surface: _Gdk4.Surface | None

    @property
    def props(self) -> Props: ...
    @classmethod
    def new(cls) -> GLRenderer: ...

class GLRendererClass(GObject.GPointer): ...

class GLShader(GObject.Object):
    """
    :Constructors:

    ::

        GLShader(**properties)
        new_from_bytes(sourcecode:GLib.Bytes) -> Gsk.GLShader
        new_from_resource(resource_path:str) -> Gsk.GLShader

    Object GskGLShader

    Properties from GskGLShader:
      source -> GBytes: source
      resource -> gchararray: resource

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        resource: str | None
        source: GLib.Bytes

    @property
    def props(self) -> Props: ...
    def __init__(self, *, resource: str = ..., source: GLib.Bytes = ...) -> None: ...
    def compile(self, renderer: Renderer) -> bool: ...
    def find_uniform_by_name(self, name: str) -> int: ...
    def get_arg_bool(self, args: GLib.Bytes, idx: int) -> bool: ...
    def get_arg_float(self, args: GLib.Bytes, idx: int) -> float: ...
    def get_arg_int(self, args: GLib.Bytes, idx: int) -> int: ...
    def get_arg_uint(self, args: GLib.Bytes, idx: int) -> int: ...
    def get_arg_vec2(
        self, args: GLib.Bytes, idx: int, out_value: Graphene.Vec2
    ) -> None: ...
    def get_arg_vec3(
        self, args: GLib.Bytes, idx: int, out_value: Graphene.Vec3
    ) -> None: ...
    def get_arg_vec4(
        self, args: GLib.Bytes, idx: int, out_value: Graphene.Vec4
    ) -> None: ...
    def get_args_size(self) -> int: ...
    def get_n_textures(self) -> int: ...
    def get_n_uniforms(self) -> int: ...
    def get_resource(self) -> str | None: ...
    def get_source(self) -> GLib.Bytes: ...
    def get_uniform_name(self, idx: int) -> str: ...
    def get_uniform_offset(self, idx: int) -> int: ...
    def get_uniform_type(self, idx: int) -> GLUniformType: ...
    @classmethod
    def new_from_bytes(cls, sourcecode: GLib.Bytes) -> GLShader: ...
    @classmethod
    def new_from_resource(cls, resource_path: str) -> GLShader: ...

class GLShaderClass(GObject.GPointer):
    """
    :Constructors:

    ::

        GLShaderClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...

class GLShaderNode(RenderNode):
    """
    :Constructors:

    ::

        GLShaderNode(**properties)
        new(shader:Gsk.GLShader, bounds:Graphene.Rect, args:GLib.Bytes, children:list=None) -> Gsk.GLShaderNode
    """
    def get_args(self) -> GLib.Bytes: ...
    def get_child(self, idx: int) -> RenderNode: ...
    def get_n_children(self) -> int: ...
    def get_shader(self) -> GLShader: ...
    @classmethod
    def new(
        cls,
        shader: GLShader,
        bounds: Graphene.Rect,
        args: GLib.Bytes,
        children: Sequence[RenderNode] | None = None,
    ) -> GLShaderNode: ...

class InsetShadowNode(RenderNode):
    """
    :Constructors:

    ::

        InsetShadowNode(**properties)
        new(outline:Gsk.RoundedRect, color:Gdk.RGBA, dx:float, dy:float, spread:float, blur_radius:float) -> Gsk.InsetShadowNode
    """
    def get_blur_radius(self) -> float: ...
    def get_color(self) -> _Gdk4.RGBA: ...
    def get_dx(self) -> float: ...
    def get_dy(self) -> float: ...
    def get_outline(self) -> RoundedRect: ...
    def get_spread(self) -> float: ...
    @classmethod
    def new(
        cls,
        outline: RoundedRect,
        color: _Gdk4.RGBA,
        dx: float,
        dy: float,
        spread: float,
        blur_radius: float,
    ) -> InsetShadowNode: ...

class IsolationNode(RenderNode):
    """
    :Constructors:

    ::

        IsolationNode(**properties)
        new(child:Gsk.RenderNode, isolations:Gsk.Isolation) -> Gsk.IsolationNode
    """
    def get_child(self) -> RenderNode: ...
    def get_isolations(self) -> Isolation: ...
    @classmethod
    def new(cls, child: RenderNode, isolations: Isolation) -> IsolationNode: ...

class LinearGradientNode(RenderNode):
    """
    :Constructors:

    ::

        LinearGradientNode(**properties)
        new(bounds:Graphene.Rect, start:Graphene.Point, end:Graphene.Point, color_stops:list) -> Gsk.LinearGradientNode
    """
    def get_color_stops(self) -> list[ColorStop]: ...
    def get_end(self) -> Graphene.Point: ...
    def get_n_color_stops(self) -> int: ...
    def get_start(self) -> Graphene.Point: ...
    @classmethod
    def new(
        cls,
        bounds: Graphene.Rect,
        start: Graphene.Point,
        end: Graphene.Point,
        color_stops: Sequence[ColorStop],
    ) -> LinearGradientNode: ...

class MaskNode(RenderNode):
    """
    :Constructors:

    ::

        MaskNode(**properties)
        new(source:Gsk.RenderNode, mask:Gsk.RenderNode, mask_mode:Gsk.MaskMode) -> Gsk.MaskNode
    """
    def get_mask(self) -> RenderNode: ...
    def get_mask_mode(self) -> MaskMode: ...
    def get_source(self) -> RenderNode: ...
    @classmethod
    def new(
        cls, source: RenderNode, mask: RenderNode, mask_mode: MaskMode
    ) -> MaskNode: ...

class NglRenderer(Renderer):
    """
    :Constructors:

    ::

        NglRenderer(**properties)
        new() -> Gsk.Renderer

    Object GskNglRenderer

    Properties from GskRenderer:
      realized -> gboolean: realized
      surface -> GdkSurface: surface

    Signals from GObject:
      notify (GParam)
    """
    class Props(Renderer.Props):
        realized: bool
        surface: _Gdk4.Surface | None

    @property
    def props(self) -> Props: ...
    @classmethod
    def new(cls) -> NglRenderer: ...

class OpacityNode(RenderNode):
    """
    :Constructors:

    ::

        OpacityNode(**properties)
        new(child:Gsk.RenderNode, opacity:float) -> Gsk.OpacityNode
    """
    def get_child(self) -> RenderNode: ...
    def get_opacity(self) -> float: ...
    @classmethod
    def new(cls, child: RenderNode, opacity: float) -> OpacityNode: ...

class OutsetShadowNode(RenderNode):
    """
    :Constructors:

    ::

        OutsetShadowNode(**properties)
        new(outline:Gsk.RoundedRect, color:Gdk.RGBA, dx:float, dy:float, spread:float, blur_radius:float) -> Gsk.OutsetShadowNode
    """
    def get_blur_radius(self) -> float: ...
    def get_color(self) -> _Gdk4.RGBA: ...
    def get_dx(self) -> float: ...
    def get_dy(self) -> float: ...
    def get_outline(self) -> RoundedRect: ...
    def get_spread(self) -> float: ...
    @classmethod
    def new(
        cls,
        outline: RoundedRect,
        color: _Gdk4.RGBA,
        dx: float,
        dy: float,
        spread: float,
        blur_radius: float,
    ) -> OutsetShadowNode: ...

class ParseLocation(GObject.GPointer):
    """
    :Constructors:

    ::

        ParseLocation()
    """

    bytes: int = ...
    chars: int = ...
    lines: int = ...
    line_bytes: int = ...
    line_chars: int = ...

class PasteNode(RenderNode):
    """
    :Constructors:

    ::

        PasteNode(**properties)
        new(bounds:Graphene.Rect, depth:int) -> Gsk.PasteNode
    """
    def get_depth(self) -> int: ...
    @classmethod
    def new(cls, bounds: Graphene.Rect, depth: int) -> PasteNode: ...

class Path(GObject.GBoxed):
    def equal(self, path2: Path) -> bool: ...
    def foreach(
        self, flags: PathForeachFlags, func: Callable[..., bool], *user_data: Any
    ) -> bool: ...
    def foreach_intersection(
        self, path2: Path | None, func: Callable[..., bool], *user_data: Any
    ) -> bool: ...
    def get_bounds(self) -> tuple[bool, Graphene.Rect]: ...
    def get_closest_point(
        self, point: Graphene.Point, threshold: float
    ) -> tuple[bool, PathPoint, float]: ...
    def get_end_point(self) -> tuple[bool, PathPoint]: ...
    def get_next(self) -> tuple[bool, PathPoint]: ...
    def get_previous(self) -> tuple[bool, PathPoint]: ...
    def get_start_point(self) -> tuple[bool, PathPoint]: ...
    def get_stroke_bounds(self, stroke: Stroke) -> tuple[bool, Graphene.Rect]: ...
    def get_tight_bounds(self) -> tuple[bool, Graphene.Rect]: ...
    def in_fill(self, point: Graphene.Point, fill_rule: FillRule) -> bool: ...
    def is_closed(self) -> bool: ...
    def is_empty(self) -> bool: ...
    @staticmethod
    def parse(string: str) -> Path | None: ...
    def print_(self, string: GLib.String) -> None: ...
    def ref(self) -> Path: ...
    def to_cairo(self, cr: cairo.Context[_SomeSurface]) -> None: ...
    def to_string(self) -> str: ...
    def unref(self) -> None: ...

class PathBuilder(GObject.GBoxed):
    """
    :Constructors:

    ::

        new() -> Gsk.PathBuilder
    """
    @staticmethod
    def __new__(cls: type[Self]) -> Self: ...
    def add_cairo_path(self, path: cairo.Path) -> None: ...
    def add_circle(self, center: Graphene.Point, radius: float) -> None: ...
    def add_layout(self, layout: Pango.Layout) -> None: ...
    def add_path(self, path: Path) -> None: ...
    def add_rect(self, rect: Graphene.Rect) -> None: ...
    def add_reverse_path(self, path: Path) -> None: ...
    def add_rounded_rect(self, rect: RoundedRect) -> None: ...
    def add_segment(self, path: Path, start: PathPoint, end: PathPoint) -> None: ...
    def arc_to(self, x1: float, y1: float, x2: float, y2: float) -> None: ...
    def close(self) -> None: ...
    def conic_to(
        self, x1: float, y1: float, x2: float, y2: float, weight: float
    ) -> None: ...
    def cubic_to(
        self, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float
    ) -> None: ...
    def get_current_point(self) -> Graphene.Point: ...
    def html_arc_to(
        self, x1: float, y1: float, x2: float, y2: float, radius: float
    ) -> None: ...
    def line_to(self, x: float, y: float) -> None: ...
    def move_to(self, x: float, y: float) -> None: ...
    @classmethod
    def new(cls) -> PathBuilder: ...
    def quad_to(self, x1: float, y1: float, x2: float, y2: float) -> None: ...
    def ref(self) -> PathBuilder: ...
    def rel_arc_to(self, x1: float, y1: float, x2: float, y2: float) -> None: ...
    def rel_conic_to(
        self, x1: float, y1: float, x2: float, y2: float, weight: float
    ) -> None: ...
    def rel_cubic_to(
        self, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float
    ) -> None: ...
    def rel_html_arc_to(
        self, x1: float, y1: float, x2: float, y2: float, radius: float
    ) -> None: ...
    def rel_line_to(self, x: float, y: float) -> None: ...
    def rel_move_to(self, x: float, y: float) -> None: ...
    def rel_quad_to(self, x1: float, y1: float, x2: float, y2: float) -> None: ...
    def rel_svg_arc_to(
        self,
        rx: float,
        ry: float,
        x_axis_rotation: float,
        large_arc: bool,
        positive_sweep: bool,
        x: float,
        y: float,
    ) -> None: ...
    def svg_arc_to(
        self,
        rx: float,
        ry: float,
        x_axis_rotation: float,
        large_arc: bool,
        positive_sweep: bool,
        x: float,
        y: float,
    ) -> None: ...
    def to_path(self) -> Path: ...
    def unref(self) -> None: ...

class PathMeasure(GObject.GBoxed):
    """
    :Constructors:

    ::

        new(path:Gsk.Path) -> Gsk.PathMeasure
        new_with_tolerance(path:Gsk.Path, tolerance:float) -> Gsk.PathMeasure
    """
    @staticmethod
    def __new__(cls: type[Self], path: Path) -> Self: ...
    def get_length(self) -> float: ...
    def get_path(self) -> Path: ...
    def get_point(self, distance: float) -> tuple[bool, PathPoint]: ...
    def get_tolerance(self) -> float: ...
    @classmethod
    def new(cls, path: Path) -> PathMeasure: ...
    @classmethod
    def new_with_tolerance(cls, path: Path, tolerance: float) -> PathMeasure: ...
    def ref(self) -> PathMeasure: ...
    def unref(self) -> None: ...

class PathPoint(GObject.GBoxed):
    def compare(self, point2: PathPoint) -> int: ...
    def copy(self) -> PathPoint: ...
    def equal(self, point2: PathPoint) -> bool: ...
    def free(self) -> None: ...
    def get_curvature(
        self, path: Path, direction: PathDirection
    ) -> tuple[float, Graphene.Point]: ...
    def get_distance(self, measure: PathMeasure) -> float: ...
    def get_position(self, path: Path) -> Graphene.Point: ...
    def get_rotation(self, path: Path, direction: PathDirection) -> float: ...
    def get_tangent(self, path: Path, direction: PathDirection) -> Graphene.Vec2: ...

class RadialGradientNode(RenderNode):
    """
    :Constructors:

    ::

        RadialGradientNode(**properties)
        new(bounds:Graphene.Rect, center:Graphene.Point, hradius:float, vradius:float, start:float, end:float, color_stops:list) -> Gsk.RadialGradientNode
    """
    def get_center(self) -> Graphene.Point: ...
    def get_color_stops(self) -> list[ColorStop]: ...
    def get_end(self) -> float: ...
    def get_hradius(self) -> float: ...
    def get_n_color_stops(self) -> int: ...
    def get_start(self) -> float: ...
    def get_vradius(self) -> float: ...
    @classmethod
    def new(
        cls,
        bounds: Graphene.Rect,
        center: Graphene.Point,
        hradius: float,
        vradius: float,
        start: float,
        end: float,
        color_stops: Sequence[ColorStop],
    ) -> RadialGradientNode: ...

class RenderNode(_gi.Fundamental):
    """
    :Constructors:

    ::

        RenderNode(**properties)
    """
    @staticmethod
    def deserialize(
        bytes: GLib.Bytes,
        error_func: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> RenderNode | None: ...
    def draw(self, cr: cairo.Context[_SomeSurface]) -> None: ...
    def get_bounds(self) -> Graphene.Rect: ...
    def get_children(self) -> list[RenderNode] | None: ...
    def get_node_type(self) -> RenderNodeType: ...
    def get_opaque_rect(self) -> tuple[bool, Graphene.Rect]: ...
    def ref(self) -> RenderNode: ...
    def serialize(self) -> GLib.Bytes: ...
    def unref(self) -> None: ...
    def write_to_file(self, filename: str) -> bool: ...

class RenderReplay(GObject.GPointer):
    """
    :Constructors:

    ::

        new() -> Gsk.RenderReplay
    """
    @staticmethod
    def __new__(cls: type[Self]) -> Self: ...
    def default(self, node: RenderNode) -> RenderNode | None: ...
    def filter_font(self, font: Pango.Font) -> Pango.Font: ...
    def filter_node(self, node: RenderNode) -> RenderNode | None: ...
    def filter_texture(self, texture: _Gdk4.Texture) -> _Gdk4.Texture: ...
    def free(self) -> None: ...
    @classmethod
    def new(cls) -> RenderReplay: ...
    def set_font_filter(
        self, filter: Callable[..., Pango.Font] | None = None, *user_data: Any
    ) -> None: ...
    def set_node_filter(
        self, filter: Callable[..., RenderNode | None] | None = None, *user_data: Any
    ) -> None: ...
    def set_texture_filter(
        self, filter: Callable[..., _Gdk4.Texture] | None = None, *user_data: Any
    ) -> None: ...

class Renderer(GObject.Object):
    """
    :Constructors:

    ::

        Renderer(**properties)
        new_for_surface(surface:Gdk.Surface) -> Gsk.Renderer or None

    Object GskRenderer

    Properties from GskRenderer:
      realized -> gboolean: realized
      surface -> GdkSurface: surface

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        realized: bool
        surface: _Gdk4.Surface | None

    @property
    def props(self) -> Props: ...
    def get_surface(self) -> _Gdk4.Surface | None: ...
    def is_realized(self) -> bool: ...
    @classmethod
    def new_for_surface(cls, surface: _Gdk4.Surface) -> Renderer | None: ...
    def realize(self, surface: _Gdk4.Surface | None = None) -> bool: ...
    def realize_for_display(self, display: _Gdk4.Display) -> bool: ...
    def render(self, root: RenderNode, region: cairo.Region | None = None) -> None: ...
    def render_texture(
        self, root: RenderNode, viewport: Graphene.Rect | None = None
    ) -> _Gdk4.Texture: ...
    def unrealize(self) -> None: ...

class RendererClass(GObject.GPointer): ...

class RepeatNode(RenderNode):
    """
    :Constructors:

    ::

        RepeatNode(**properties)
        new(bounds:Graphene.Rect, child:Gsk.RenderNode, child_bounds:Graphene.Rect=None) -> Gsk.RepeatNode
    """
    def get_child(self) -> RenderNode: ...
    def get_child_bounds(self) -> Graphene.Rect: ...
    @classmethod
    def new(
        cls,
        bounds: Graphene.Rect,
        child: RenderNode,
        child_bounds: Graphene.Rect | None = None,
    ) -> RepeatNode: ...

class RepeatingLinearGradientNode(RenderNode):
    """
    :Constructors:

    ::

        RepeatingLinearGradientNode(**properties)
        new(bounds:Graphene.Rect, start:Graphene.Point, end:Graphene.Point, color_stops:list) -> Gsk.RepeatingLinearGradientNode
    """
    @classmethod
    def new(
        cls,
        bounds: Graphene.Rect,
        start: Graphene.Point,
        end: Graphene.Point,
        color_stops: Sequence[ColorStop],
    ) -> RepeatingLinearGradientNode: ...

class RepeatingRadialGradientNode(RenderNode):
    """
    :Constructors:

    ::

        RepeatingRadialGradientNode(**properties)
        new(bounds:Graphene.Rect, center:Graphene.Point, hradius:float, vradius:float, start:float, end:float, color_stops:list) -> Gsk.RepeatingRadialGradientNode
    """
    @classmethod
    def new(
        cls,
        bounds: Graphene.Rect,
        center: Graphene.Point,
        hradius: float,
        vradius: float,
        start: float,
        end: float,
        color_stops: Sequence[ColorStop],
    ) -> RepeatingRadialGradientNode: ...

class RoundedClipNode(RenderNode):
    """
    :Constructors:

    ::

        RoundedClipNode(**properties)
        new(child:Gsk.RenderNode, clip:Gsk.RoundedRect) -> Gsk.RoundedClipNode
    """
    def get_child(self) -> RenderNode: ...
    def get_clip(self) -> RoundedRect: ...
    @classmethod
    def new(cls, child: RenderNode, clip: RoundedRect) -> RoundedClipNode: ...

class RoundedRect(GObject.GPointer):
    """
    :Constructors:

    ::

        RoundedRect()
    """

    bounds: Graphene.Rect = ...
    corner: list[Graphene.Size] = ...
    def contains_point(self, point: Graphene.Point) -> bool: ...
    def contains_rect(self, rect: Graphene.Rect) -> bool: ...
    def init(
        self,
        bounds: Graphene.Rect,
        top_left: Graphene.Size,
        top_right: Graphene.Size,
        bottom_right: Graphene.Size,
        bottom_left: Graphene.Size,
    ) -> RoundedRect: ...
    def init_copy(self, src: RoundedRect) -> RoundedRect: ...
    def init_from_rect(self, bounds: Graphene.Rect, radius: float) -> RoundedRect: ...
    def intersects_rect(self, rect: Graphene.Rect) -> bool: ...
    def is_rectilinear(self) -> bool: ...
    def normalize(self) -> RoundedRect: ...
    def offset(self, dx: float, dy: float) -> RoundedRect: ...
    def shrink(
        self, top: float, right: float, bottom: float, left: float
    ) -> RoundedRect: ...

class ShaderArgsBuilder(GObject.GBoxed):
    """
    :Constructors:

    ::

        new(shader:Gsk.GLShader, initial_values:GLib.Bytes=None) -> Gsk.ShaderArgsBuilder
    """
    @staticmethod
    def __new__(
        cls: type[Self], shader: GLShader, initial_values: GLib.Bytes | None = None
    ) -> Self: ...
    @classmethod
    def new(
        cls, shader: GLShader, initial_values: GLib.Bytes | None = None
    ) -> ShaderArgsBuilder: ...
    def ref(self) -> ShaderArgsBuilder: ...
    def set_bool(self, idx: int, value: bool) -> None: ...
    def set_float(self, idx: int, value: float) -> None: ...
    def set_int(self, idx: int, value: int) -> None: ...
    def set_uint(self, idx: int, value: int) -> None: ...
    def set_vec2(self, idx: int, value: Graphene.Vec2) -> None: ...
    def set_vec3(self, idx: int, value: Graphene.Vec3) -> None: ...
    def set_vec4(self, idx: int, value: Graphene.Vec4) -> None: ...
    def to_args(self) -> GLib.Bytes: ...
    def unref(self) -> None: ...

class Shadow(GObject.GPointer):
    """
    :Constructors:

    ::

        Shadow()
    """

    color: _Gdk4.RGBA = ...
    dx: float = ...
    dy: float = ...
    radius: float = ...

class ShadowNode(RenderNode):
    """
    :Constructors:

    ::

        ShadowNode(**properties)
        new(child:Gsk.RenderNode, shadows:list) -> Gsk.ShadowNode
    """
    def get_child(self) -> RenderNode: ...
    def get_n_shadows(self) -> int: ...
    def get_shadow(self, i: int) -> Shadow: ...
    @classmethod
    def new(cls, child: RenderNode, shadows: Sequence[Shadow]) -> ShadowNode: ...

class Stroke(GObject.GBoxed):
    """
    :Constructors:

    ::

        new(line_width:float) -> Gsk.Stroke
    """
    @staticmethod
    def __new__(cls: type[Self], line_width: float) -> Self: ...
    def copy(self) -> Stroke: ...
    @staticmethod
    def equal(stroke1: None, stroke2: None) -> bool: ...
    def free(self) -> None: ...
    def get_dash(self) -> list[float] | None: ...
    def get_dash_offset(self) -> float: ...
    def get_line_cap(self) -> LineCap: ...
    def get_line_join(self) -> LineJoin: ...
    def get_line_width(self) -> float: ...
    def get_miter_limit(self) -> float: ...
    @classmethod
    def new(cls, line_width: float) -> Stroke: ...
    def set_dash(self, dash: Sequence[float] | None = None) -> None: ...
    def set_dash_offset(self, offset: float) -> None: ...
    def set_line_cap(self, line_cap: LineCap) -> None: ...
    def set_line_join(self, line_join: LineJoin) -> None: ...
    def set_line_width(self, line_width: float) -> None: ...
    def set_miter_limit(self, limit: float) -> None: ...
    def to_cairo(self, cr: cairo.Context[_SomeSurface]) -> None: ...

class StrokeNode(RenderNode):
    """
    :Constructors:

    ::

        StrokeNode(**properties)
        new(child:Gsk.RenderNode, path:Gsk.Path, stroke:Gsk.Stroke) -> Gsk.StrokeNode
    """
    def get_child(self) -> RenderNode: ...
    def get_path(self) -> Path: ...
    def get_stroke(self) -> Stroke: ...
    @classmethod
    def new(cls, child: RenderNode, path: Path, stroke: Stroke) -> StrokeNode: ...

class SubsurfaceNode(RenderNode):
    """
    :Constructors:

    ::

        SubsurfaceNode(**properties)
    """
    def get_child(self) -> RenderNode: ...

class TextNode(RenderNode):
    """
    :Constructors:

    ::

        TextNode(**properties)
        new(font:Pango.Font, glyphs:Pango.GlyphString, color:Gdk.RGBA, offset:Graphene.Point) -> Gsk.TextNode or None
    """
    def get_color(self) -> _Gdk4.RGBA: ...
    def get_font(self) -> Pango.Font: ...
    def get_glyphs(self) -> list[Pango.GlyphInfo]: ...
    def get_num_glyphs(self) -> int: ...
    def get_offset(self) -> Graphene.Point: ...
    def has_color_glyphs(self) -> bool: ...
    @classmethod
    def new(
        cls,
        font: Pango.Font,
        glyphs: Pango.GlyphString,
        color: _Gdk4.RGBA,
        offset: Graphene.Point,
    ) -> TextNode | None: ...

class TextureNode(RenderNode):
    """
    :Constructors:

    ::

        TextureNode(**properties)
        new(texture:Gdk.Texture, bounds:Graphene.Rect) -> Gsk.TextureNode
    """
    def get_texture(self) -> _Gdk4.Texture: ...
    @classmethod
    def new(cls, texture: _Gdk4.Texture, bounds: Graphene.Rect) -> TextureNode: ...

class TextureScaleNode(RenderNode):
    """
    :Constructors:

    ::

        TextureScaleNode(**properties)
        new(texture:Gdk.Texture, bounds:Graphene.Rect, filter:Gsk.ScalingFilter) -> Gsk.TextureScaleNode
    """
    def get_filter(self) -> ScalingFilter: ...
    def get_texture(self) -> _Gdk4.Texture: ...
    @classmethod
    def new(
        cls, texture: _Gdk4.Texture, bounds: Graphene.Rect, filter: ScalingFilter
    ) -> TextureScaleNode: ...

class Transform(GObject.GBoxed):
    """
    :Constructors:

    ::

        new() -> Gsk.Transform
    """
    @staticmethod
    def __new__(cls: type[Self]) -> Self: ...
    def equal(self, second: Transform | None = None) -> bool: ...
    def get_category(self) -> TransformCategory: ...
    def invert(self) -> Transform | None: ...
    def matrix(self, matrix: Graphene.Matrix) -> Transform: ...
    def matrix_2d(
        self, xx: float, yx: float, xy: float, yy: float, dx: float, dy: float
    ) -> Transform | None: ...
    @classmethod
    def new(cls) -> Transform: ...
    @staticmethod
    def parse(string: str) -> tuple[bool, Transform]: ...
    def perspective(self, depth: float) -> Transform: ...
    def print_(self, string: GLib.String) -> None: ...
    def ref(self) -> Transform | None: ...
    def rotate(self, angle: float) -> Transform | None: ...
    def rotate_3d(self, angle: float, axis: Graphene.Vec3) -> Transform | None: ...
    def scale(self, factor_x: float, factor_y: float) -> Transform | None: ...
    def scale_3d(
        self, factor_x: float, factor_y: float, factor_z: float
    ) -> Transform | None: ...
    def skew(self, skew_x: float, skew_y: float) -> Transform | None: ...
    def to_2d(self) -> tuple[float, float, float, float, float, float]: ...
    def to_2d_components(
        self,
    ) -> tuple[float, float, float, float, float, float, float]: ...
    def to_affine(self) -> tuple[float, float, float, float]: ...
    def to_matrix(self) -> Graphene.Matrix: ...
    def to_string(self) -> str: ...
    def to_translate(self) -> tuple[float, float]: ...
    def transform(self, other: Transform | None = None) -> Transform | None: ...
    def transform_bounds(self, rect: Graphene.Rect) -> Graphene.Rect: ...
    def transform_point(self, point: Graphene.Point) -> Graphene.Point: ...
    def translate(self, point: Graphene.Point) -> Transform | None: ...
    def translate_3d(self, point: Graphene.Point3D) -> Transform | None: ...
    def unref(self) -> None: ...

class TransformNode(RenderNode):
    """
    :Constructors:

    ::

        TransformNode(**properties)
        new(child:Gsk.RenderNode, transform:Gsk.Transform=None) -> Gsk.TransformNode
    """
    def get_child(self) -> RenderNode: ...
    def get_transform(self) -> Transform: ...
    @classmethod
    def new(
        cls, child: RenderNode, transform: Transform | None = None
    ) -> TransformNode: ...

class VulkanRenderer(Renderer):
    """
    :Constructors:

    ::

        VulkanRenderer(**properties)
        new() -> Gsk.Renderer

    Object GskVulkanRenderer

    Properties from GskRenderer:
      realized -> gboolean: realized
      surface -> GdkSurface: surface

    Signals from GObject:
      notify (GParam)
    """
    class Props(Renderer.Props):
        realized: bool
        surface: _Gdk4.Surface | None

    @property
    def props(self) -> Props: ...
    @classmethod
    def new(cls) -> VulkanRenderer: ...

class VulkanRendererClass(GObject.GPointer): ...

class Isolation(GObject.GFlags):
    ALL = 4294967295
    BACKGROUND = 1
    COPY_PASTE = 2
    NONE = 0

class PathForeachFlags(GObject.GFlags):
    CONIC = 4
    CUBIC = 2
    ONLY_LINES = 0
    QUAD = 1

class BlendMode(GObject.GEnum):
    COLOR = 12
    COLOR_BURN = 7
    COLOR_DODGE = 6
    DARKEN = 4
    DEFAULT = 0
    DIFFERENCE = 10
    EXCLUSION = 11
    HARD_LIGHT = 8
    HUE = 13
    LIGHTEN = 5
    LUMINOSITY = 15
    MULTIPLY = 1
    OVERLAY = 3
    SATURATION = 14
    SCREEN = 2
    SOFT_LIGHT = 9

class Corner(GObject.GEnum):
    BOTTOM_LEFT = 3
    BOTTOM_RIGHT = 2
    TOP_LEFT = 0
    TOP_RIGHT = 1

class FillRule(GObject.GEnum):
    EVEN_ODD = 1
    WINDING = 0

class GLUniformType(GObject.GEnum):
    BOOL = 4
    FLOAT = 1
    INT = 2
    NONE = 0
    UINT = 3
    VEC2 = 5
    VEC3 = 6
    VEC4 = 7

class LineCap(GObject.GEnum):
    BUTT = 0
    ROUND = 1
    SQUARE = 2

class LineJoin(GObject.GEnum):
    BEVEL = 2
    MITER = 0
    ROUND = 1

class MaskMode(GObject.GEnum):
    ALPHA = 0
    INVERTED_ALPHA = 1
    INVERTED_LUMINANCE = 3
    LUMINANCE = 2

class PathDirection(GObject.GEnum):
    FROM_END = 3
    FROM_START = 0
    TO_END = 2
    TO_START = 1

class PathIntersection(GObject.GEnum):
    END = 3
    NONE = 0
    NORMAL = 1
    START = 2

class PathOperation(GObject.GEnum):
    CLOSE = 1
    CONIC = 5
    CUBIC = 4
    LINE = 2
    MOVE = 0
    QUAD = 3

class PorterDuff(GObject.GEnum):
    CLEAR = 11
    DEST = 1
    DEST_ATOP_SOURCE = 9
    DEST_IN_SOURCE = 5
    DEST_OUT_SOURCE = 7
    DEST_OVER_SOURCE = 3
    SOURCE = 0
    SOURCE_ATOP_DEST = 8
    SOURCE_IN_DEST = 4
    SOURCE_OUT_DEST = 6
    SOURCE_OVER_DEST = 2
    XOR = 10

class RenderNodeType(GObject.GEnum):
    ARITHMETIC_NODE = 37
    BLEND_NODE = 20
    BLUR_NODE = 23
    BORDER_NODE = 9
    CAIRO_NODE = 2
    CLIP_NODE = 17
    COLOR_MATRIX_NODE = 15
    COLOR_NODE = 3
    COMPONENT_TRANSFER_NODE = 31
    COMPOSITE_NODE = 34
    CONIC_GRADIENT_NODE = 8
    CONTAINER_NODE = 1
    COPY_NODE = 32
    CROSS_FADE_NODE = 21
    DEBUG_NODE = 24
    DISPLACEMENT_NODE = 36
    FILL_NODE = 28
    GL_SHADER_NODE = 25
    INSET_SHADOW_NODE = 11
    ISOLATION_NODE = 35
    LINEAR_GRADIENT_NODE = 4
    MASK_NODE = 27
    NOT_A_RENDER_NODE = 0
    OPACITY_NODE = 14
    OUTSET_SHADOW_NODE = 12
    PASTE_NODE = 33
    RADIAL_GRADIENT_NODE = 6
    REPEATING_LINEAR_GRADIENT_NODE = 5
    REPEATING_RADIAL_GRADIENT_NODE = 7
    REPEAT_NODE = 16
    ROUNDED_CLIP_NODE = 18
    SHADOW_NODE = 19
    STROKE_NODE = 29
    SUBSURFACE_NODE = 30
    TEXTURE_NODE = 10
    TEXTURE_SCALE_NODE = 26
    TEXT_NODE = 22
    TRANSFORM_NODE = 13

class ScalingFilter(GObject.GEnum):
    LINEAR = 0
    NEAREST = 1
    TRILINEAR = 2

class SerializationError(GObject.GEnum):
    INVALID_DATA = 2
    UNSUPPORTED_FORMAT = 0
    UNSUPPORTED_VERSION = 1
    @staticmethod
    def quark() -> int: ...

class TransformCategory(GObject.GEnum):
    ANY = 1
    IDENTITY = 6
    UNKNOWN = 0
