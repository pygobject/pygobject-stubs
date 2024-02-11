from typing import Any
from typing import Callable
from typing import Literal
from typing import Optional
from typing import Sequence
from typing import Tuple
from typing import Type
from typing import TypeVar

import cairo
from gi.repository import Gdk
from gi.repository import GLib
from gi.repository import GObject
from gi.repository import Graphene
from gi.repository import Pango

_SomeSurface = TypeVar("_SomeSurface", bound=cairo.Surface)

_lock = ...  # FIXME Constant
_namespace: str = "Gsk"
_version: str = "4.0"

def serialization_error_quark() -> int: ...
def transform_parse(string: str) -> Tuple[bool, Transform]: ...
def value_dup_render_node(value: Any) -> Optional[RenderNode]: ...
def value_get_render_node(value: Any) -> Optional[RenderNode]: ...
def value_set_render_node(value: Any, node: RenderNode) -> None: ...
def value_take_render_node(value: Any, node: Optional[RenderNode] = None) -> None: ...

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

    def get_colors(self) -> Gdk.RGBA: ...
    def get_outline(self) -> RoundedRect: ...
    def get_widths(self) -> list[float]: ...
    @classmethod
    def new(
        cls,
        outline: RoundedRect,
        border_width: Sequence[float],
        border_color: Sequence[Gdk.RGBA],
    ) -> BorderNode: ...

class BroadwayRenderer(Renderer):
    """
    :Constructors:

    ::

        BroadwayRenderer(**properties)
        new() -> Gsk.Renderer

    Object GskBroadwayRenderer

    Properties from GskRenderer:
      realized -> gboolean: realized
      surface -> GdkSurface: surface

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        realized: bool
        surface: Optional[Gdk.Surface]
    props: Props = ...
    @classmethod
    def new(cls) -> BroadwayRenderer: ...

class BroadwayRendererClass(GObject.GPointer): ...

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

    class Props:
        realized: bool
        surface: Optional[Gdk.Surface]
    props: Props = ...
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

    def get_color(self) -> Gdk.RGBA: ...
    @classmethod
    def new(cls, rgba: Gdk.RGBA, bounds: Graphene.Rect) -> ColorNode: ...

class ColorStop(GObject.GPointer):
    """
    :Constructors:

    ::

        ColorStop()
    """

    offset: float = ...
    color: Gdk.RGBA = ...

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

    class Props:
        realized: bool
        surface: Optional[Gdk.Surface]
    props: Props = ...
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

    class Props:
        resource: Optional[str]
        source: GLib.Bytes
    props: Props = ...
    def __init__(self, resource: str = ..., source: GLib.Bytes = ...): ...
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
    def get_resource(self) -> Optional[str]: ...
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

    parent_class: GObject.ObjectClass = ...

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
        children: Optional[Sequence[RenderNode]] = None,
    ) -> GLShaderNode: ...

class InsetShadowNode(RenderNode):
    """
    :Constructors:

    ::

        InsetShadowNode(**properties)
        new(outline:Gsk.RoundedRect, color:Gdk.RGBA, dx:float, dy:float, spread:float, blur_radius:float) -> Gsk.InsetShadowNode
    """

    def get_blur_radius(self) -> float: ...
    def get_color(self) -> Gdk.RGBA: ...
    def get_dx(self) -> float: ...
    def get_dy(self) -> float: ...
    def get_outline(self) -> RoundedRect: ...
    def get_spread(self) -> float: ...
    @classmethod
    def new(
        cls,
        outline: RoundedRect,
        color: Gdk.RGBA,
        dx: float,
        dy: float,
        spread: float,
        blur_radius: float,
    ) -> InsetShadowNode: ...

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

    class Props:
        realized: bool
        surface: Optional[Gdk.Surface]
    props: Props = ...
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
    def get_color(self) -> Gdk.RGBA: ...
    def get_dx(self) -> float: ...
    def get_dy(self) -> float: ...
    def get_outline(self) -> RoundedRect: ...
    def get_spread(self) -> float: ...
    @classmethod
    def new(
        cls,
        outline: RoundedRect,
        color: Gdk.RGBA,
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

class RenderNode:
    """
    :Constructors:

    ::

        RenderNode(**properties)
    """

    @staticmethod
    def deserialize(
        bytes: GLib.Bytes,
        error_func: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> Optional[RenderNode]: ...
    def draw(self, cr: cairo.Context[_SomeSurface]) -> None: ...
    def get_bounds(self) -> Graphene.Rect: ...
    def get_node_type(self) -> RenderNodeType: ...
    def ref(self) -> RenderNode: ...
    def serialize(self) -> GLib.Bytes: ...
    def unref(self) -> None: ...
    def write_to_file(self, filename: str) -> bool: ...

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

    class Props:
        realized: bool
        surface: Optional[Gdk.Surface]
    props: Props = ...
    def get_surface(self) -> Optional[Gdk.Surface]: ...
    def is_realized(self) -> bool: ...
    @classmethod
    def new_for_surface(cls, surface: Gdk.Surface) -> Optional[Renderer]: ...
    def realize(self, surface: Optional[Gdk.Surface] = None) -> bool: ...
    def render(
        self, root: RenderNode, region: Optional[cairo.Region] = None
    ) -> None: ...
    def render_texture(
        self, root: RenderNode, viewport: Optional[Graphene.Rect] = None
    ) -> Gdk.Texture: ...
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
        child_bounds: Optional[Graphene.Rect] = None,
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

    @classmethod
    def new(
        cls, shader: GLShader, initial_values: Optional[GLib.Bytes] = None
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

    color: Gdk.RGBA = ...
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

class TextNode(RenderNode):
    """
    :Constructors:

    ::

        TextNode(**properties)
        new(font:Pango.Font, glyphs:Pango.GlyphString, color:Gdk.RGBA, offset:Graphene.Point) -> Gsk.TextNode or None
    """

    def get_color(self) -> Gdk.RGBA: ...
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
        color: Gdk.RGBA,
        offset: Graphene.Point,
    ) -> Optional[TextNode]: ...

class TextureNode(RenderNode):
    """
    :Constructors:

    ::

        TextureNode(**properties)
        new(texture:Gdk.Texture, bounds:Graphene.Rect) -> Gsk.TextureNode
    """

    def get_texture(self) -> Gdk.Texture: ...
    @classmethod
    def new(cls, texture: Gdk.Texture, bounds: Graphene.Rect) -> TextureNode: ...

class TextureScaleNode(RenderNode):
    """
    :Constructors:

    ::

        TextureScaleNode(**properties)
        new(texture:Gdk.Texture, bounds:Graphene.Rect, filter:Gsk.ScalingFilter) -> Gsk.TextureScaleNode
    """

    def get_filter(self) -> ScalingFilter: ...
    def get_texture(self) -> Gdk.Texture: ...
    @classmethod
    def new(
        cls, texture: Gdk.Texture, bounds: Graphene.Rect, filter: ScalingFilter
    ) -> TextureScaleNode: ...

class Transform(GObject.GBoxed):
    """
    :Constructors:

    ::

        new() -> Gsk.Transform
    """

    def equal(self, second: Optional[Transform] = None) -> bool: ...
    def get_category(self) -> TransformCategory: ...
    def invert(self) -> Optional[Transform]: ...
    def matrix(self, matrix: Graphene.Matrix) -> Transform: ...
    @classmethod
    def new(cls) -> Transform: ...
    @staticmethod
    def parse(string: str) -> Tuple[bool, Transform]: ...
    def perspective(self, depth: float) -> Transform: ...
    def print_(self, string: GLib.String) -> None: ...
    def ref(self) -> Optional[Transform]: ...
    def rotate(self, angle: float) -> Optional[Transform]: ...
    def rotate_3d(self, angle: float, axis: Graphene.Vec3) -> Optional[Transform]: ...
    def scale(self, factor_x: float, factor_y: float) -> Optional[Transform]: ...
    def scale_3d(
        self, factor_x: float, factor_y: float, factor_z: float
    ) -> Optional[Transform]: ...
    def skew(self, skew_x: float, skew_y: float) -> Optional[Transform]: ...
    def to_2d(self) -> Tuple[float, float, float, float, float, float]: ...
    def to_2d_components(
        self,
    ) -> Tuple[float, float, float, float, float, float, float]: ...
    def to_affine(self) -> Tuple[float, float, float, float]: ...
    def to_matrix(self) -> Graphene.Matrix: ...
    def to_string(self) -> str: ...
    def to_translate(self) -> Tuple[float, float]: ...
    def transform(self, other: Optional[Transform] = None) -> Optional[Transform]: ...
    def transform_bounds(self, rect: Graphene.Rect) -> Graphene.Rect: ...
    def transform_point(self, point: Graphene.Point) -> Graphene.Point: ...
    def translate(self, point: Graphene.Point) -> Optional[Transform]: ...
    def translate_3d(self, point: Graphene.Point3D) -> Optional[Transform]: ...
    def unref(self) -> None: ...

class TransformNode(RenderNode):
    """
    :Constructors:

    ::

        TransformNode(**properties)
        new(child:Gsk.RenderNode, transform:Gsk.Transform) -> Gsk.TransformNode
    """

    def get_child(self) -> RenderNode: ...
    def get_transform(self) -> Transform: ...
    @classmethod
    def new(cls, child: RenderNode, transform: Transform) -> TransformNode: ...

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

class GLUniformType(GObject.GEnum):
    BOOL = 4
    FLOAT = 1
    INT = 2
    NONE = 0
    UINT = 3
    VEC2 = 5
    VEC3 = 6
    VEC4 = 7

class MaskMode(GObject.GEnum):
    ALPHA = 0
    INVERTED_ALPHA = 1
    INVERTED_LUMINANCE = 3
    LUMINANCE = 2

class RenderNodeType(GObject.GEnum):
    BLEND_NODE = 20
    BLUR_NODE = 23
    BORDER_NODE = 9
    CAIRO_NODE = 2
    CLIP_NODE = 17
    COLOR_MATRIX_NODE = 15
    COLOR_NODE = 3
    CONIC_GRADIENT_NODE = 8
    CONTAINER_NODE = 1
    CROSS_FADE_NODE = 21
    DEBUG_NODE = 24
    GL_SHADER_NODE = 25
    INSET_SHADOW_NODE = 11
    LINEAR_GRADIENT_NODE = 4
    MASK_NODE = 27
    NOT_A_RENDER_NODE = 0
    OPACITY_NODE = 14
    OUTSET_SHADOW_NODE = 12
    RADIAL_GRADIENT_NODE = 6
    REPEATING_LINEAR_GRADIENT_NODE = 5
    REPEATING_RADIAL_GRADIENT_NODE = 7
    REPEAT_NODE = 16
    ROUNDED_CLIP_NODE = 18
    SHADOW_NODE = 19
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
