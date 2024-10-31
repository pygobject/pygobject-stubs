from typing import Any
from typing import Callable
from typing import Literal
from typing import Optional
from typing import Sequence
from typing import Tuple
from typing import Type
from typing import TypeVar

from gi.repository import GObject

PI: float = 3.141593
PI_2: float = 1.570796
VEC2_LEN: int = 2
VEC3_LEN: int = 3
VEC4_LEN: int = 4
_lock = ...  # FIXME Constant
_namespace: str = "Graphene"
_version: str = "1.0"

def box_empty() -> Box: ...
def box_infinite() -> Box: ...
def box_minus_one() -> Box: ...
def box_one() -> Box: ...
def box_one_minus_one() -> Box: ...
def box_zero() -> Box: ...
def point3d_zero() -> Point3D: ...
def point_zero() -> Point: ...
def rect_alloc() -> Rect: ...
def rect_zero() -> Rect: ...
def size_zero() -> Size: ...
def vec2_one() -> Vec2: ...
def vec2_x_axis() -> Vec2: ...
def vec2_y_axis() -> Vec2: ...
def vec2_zero() -> Vec2: ...
def vec3_one() -> Vec3: ...
def vec3_x_axis() -> Vec3: ...
def vec3_y_axis() -> Vec3: ...
def vec3_z_axis() -> Vec3: ...
def vec3_zero() -> Vec3: ...
def vec4_one() -> Vec4: ...
def vec4_w_axis() -> Vec4: ...
def vec4_x_axis() -> Vec4: ...
def vec4_y_axis() -> Vec4: ...
def vec4_z_axis() -> Vec4: ...
def vec4_zero() -> Vec4: ...

class Box(GObject.GBoxed):
    """
    :Constructors:

    ::

        Box()
        alloc() -> Graphene.Box
    """

    min: Vec3 = ...
    max: Vec3 = ...
    @classmethod
    def alloc(cls) -> Box: ...
    def contains_box(self, b: Box) -> bool: ...
    def contains_point(self, point: Point3D) -> bool: ...
    @staticmethod
    def empty() -> Box: ...
    def equal(self, b: Box) -> bool: ...
    def expand(self, point: Point3D) -> Box: ...
    def expand_scalar(self, scalar: float) -> Box: ...
    def expand_vec3(self, vec: Vec3) -> Box: ...
    def free(self) -> None: ...
    def get_bounding_sphere(self) -> Sphere: ...
    def get_center(self) -> Point3D: ...
    def get_depth(self) -> float: ...
    def get_height(self) -> float: ...
    def get_max(self) -> Point3D: ...
    def get_min(self) -> Point3D: ...
    def get_size(self) -> Vec3: ...
    def get_vertices(self) -> list[Vec3]: ...
    def get_width(self) -> float: ...
    @staticmethod
    def infinite() -> Box: ...
    def init(
        self, min: Optional[Point3D] = None, max: Optional[Point3D] = None
    ) -> Box: ...
    def init_from_box(self, src: Box) -> Box: ...
    def init_from_points(self, points: Sequence[Point3D]) -> Box: ...
    def init_from_vec3(
        self, min: Optional[Vec3] = None, max: Optional[Vec3] = None
    ) -> Box: ...
    def init_from_vectors(self, vectors: Sequence[Vec3]) -> Box: ...
    def intersection(self, b: Box) -> Tuple[bool, Box]: ...
    @staticmethod
    def minus_one() -> Box: ...
    @staticmethod
    def one() -> Box: ...
    @staticmethod
    def one_minus_one() -> Box: ...
    def union(self, b: Box) -> Box: ...
    @staticmethod
    def zero() -> Box: ...

class Euler(GObject.GBoxed):
    """
    :Constructors:

    ::

        Euler()
        alloc() -> Graphene.Euler
    """

    angles: Vec3 = ...
    order: EulerOrder = ...
    @classmethod
    def alloc(cls) -> Euler: ...
    def equal(self, b: Euler) -> bool: ...
    def free(self) -> None: ...
    def get_alpha(self) -> float: ...
    def get_beta(self) -> float: ...
    def get_gamma(self) -> float: ...
    def get_order(self) -> EulerOrder: ...
    def get_x(self) -> float: ...
    def get_y(self) -> float: ...
    def get_z(self) -> float: ...
    def init(self, x: float, y: float, z: float) -> Euler: ...
    def init_from_euler(self, src: Optional[Euler] = None) -> Euler: ...
    def init_from_matrix(self, m: Optional[Matrix], order: EulerOrder) -> Euler: ...
    def init_from_quaternion(
        self, q: Optional[Quaternion], order: EulerOrder
    ) -> Euler: ...
    def init_from_radians(
        self, x: float, y: float, z: float, order: EulerOrder
    ) -> Euler: ...
    def init_from_vec3(self, v: Optional[Vec3], order: EulerOrder) -> Euler: ...
    def init_with_order(
        self, x: float, y: float, z: float, order: EulerOrder
    ) -> Euler: ...
    def reorder(self, order: EulerOrder) -> Euler: ...
    def to_matrix(self) -> Matrix: ...
    def to_quaternion(self) -> Quaternion: ...
    def to_vec3(self) -> Vec3: ...

class Frustum(GObject.GBoxed):
    """
    :Constructors:

    ::

        Frustum()
        alloc() -> Graphene.Frustum
    """

    planes: list[Plane] = ...
    @classmethod
    def alloc(cls) -> Frustum: ...
    def contains_point(self, point: Point3D) -> bool: ...
    def equal(self, b: Frustum) -> bool: ...
    def free(self) -> None: ...
    def get_planes(self) -> list[Plane]: ...
    def init(
        self, p0: Plane, p1: Plane, p2: Plane, p3: Plane, p4: Plane, p5: Plane
    ) -> Frustum: ...
    def init_from_frustum(self, src: Frustum) -> Frustum: ...
    def init_from_matrix(self, matrix: Matrix) -> Frustum: ...
    def intersects_box(self, box: Box) -> bool: ...
    def intersects_sphere(self, sphere: Sphere) -> bool: ...

class Matrix(GObject.GBoxed):
    """
    :Constructors:

    ::

        Matrix()
        alloc() -> Graphene.Matrix
    """

    value: Simd4X4F = ...
    @classmethod
    def alloc(cls) -> Matrix: ...
    def decompose(self) -> Tuple[bool, Vec3, Vec3, Quaternion, Vec3, Vec4]: ...
    def determinant(self) -> float: ...
    def equal(self, b: Matrix) -> bool: ...
    def equal_fast(self, b: Matrix) -> bool: ...
    def free(self) -> None: ...
    def get_row(self, index_: int) -> Vec4: ...
    def get_value(self, row: int, col: int) -> float: ...
    def get_x_scale(self) -> float: ...
    def get_x_translation(self) -> float: ...
    def get_y_scale(self) -> float: ...
    def get_y_translation(self) -> float: ...
    def get_z_scale(self) -> float: ...
    def get_z_translation(self) -> float: ...
    def init_from_2d(
        self, xx: float, yx: float, xy: float, yy: float, x_0: float, y_0: float
    ) -> Matrix: ...
    def init_from_float(self, v: Sequence[float]) -> Matrix: ...
    def init_from_matrix(self, src: Matrix) -> Matrix: ...
    def init_from_vec4(self, v0: Vec4, v1: Vec4, v2: Vec4, v3: Vec4) -> Matrix: ...
    def init_frustum(
        self,
        left: float,
        right: float,
        bottom: float,
        top: float,
        z_near: float,
        z_far: float,
    ) -> Matrix: ...
    def init_identity(self) -> Matrix: ...
    def init_look_at(self, eye: Vec3, center: Vec3, up: Vec3) -> Matrix: ...
    def init_ortho(
        self,
        left: float,
        right: float,
        top: float,
        bottom: float,
        z_near: float,
        z_far: float,
    ) -> Matrix: ...
    def init_perspective(
        self, fovy: float, aspect: float, z_near: float, z_far: float
    ) -> Matrix: ...
    def init_rotate(self, angle: float, axis: Vec3) -> Matrix: ...
    def init_scale(self, x: float, y: float, z: float) -> Matrix: ...
    def init_skew(self, x_skew: float, y_skew: float) -> Matrix: ...
    def init_translate(self, p: Point3D) -> Matrix: ...
    def interpolate(self, b: Matrix, factor: float) -> Matrix: ...
    def inverse(self) -> Tuple[bool, Matrix]: ...
    def is_2d(self) -> bool: ...
    def is_backface_visible(self) -> bool: ...
    def is_identity(self) -> bool: ...
    def is_singular(self) -> bool: ...
    def multiply(self, b: Matrix) -> Matrix: ...
    def near(self, b: Matrix, epsilon: float) -> bool: ...
    def normalize(self) -> Matrix: ...
    def perspective(self, depth: float) -> Matrix: ...
    def print_(self) -> None: ...
    def project_point(self, p: Point) -> Point: ...
    def project_rect(self, r: Rect) -> Quad: ...
    def project_rect_bounds(self, r: Rect) -> Rect: ...
    def rotate(self, angle: float, axis: Vec3) -> None: ...
    def rotate_euler(self, e: Euler) -> None: ...
    def rotate_quaternion(self, q: Quaternion) -> None: ...
    def rotate_x(self, angle: float) -> None: ...
    def rotate_y(self, angle: float) -> None: ...
    def rotate_z(self, angle: float) -> None: ...
    def scale(self, factor_x: float, factor_y: float, factor_z: float) -> None: ...
    def skew_xy(self, factor: float) -> None: ...
    def skew_xz(self, factor: float) -> None: ...
    def skew_yz(self, factor: float) -> None: ...
    def to_2d(self) -> Tuple[bool, float, float, float, float, float, float]: ...
    def to_float(self) -> list[float]: ...
    def transform_bounds(self, r: Rect) -> Rect: ...
    def transform_box(self, b: Box) -> Box: ...
    def transform_point(self, p: Point) -> Point: ...
    def transform_point3d(self, p: Point3D) -> Point3D: ...
    def transform_ray(self, r: Ray) -> Ray: ...
    def transform_rect(self, r: Rect) -> Quad: ...
    def transform_sphere(self, s: Sphere) -> Sphere: ...
    def transform_vec3(self, v: Vec3) -> Vec3: ...
    def transform_vec4(self, v: Vec4) -> Vec4: ...
    def translate(self, pos: Point3D) -> None: ...
    def transpose(self) -> Matrix: ...
    def unproject_point3d(self, modelview: Matrix, point: Point3D) -> Point3D: ...
    def untransform_bounds(self, r: Rect, bounds: Rect) -> Rect: ...
    def untransform_point(self, p: Point, bounds: Rect) -> Tuple[bool, Point]: ...

class Plane(GObject.GBoxed):
    """
    :Constructors:

    ::

        Plane()
        alloc() -> Graphene.Plane
    """

    normal: Vec3 = ...
    constant: float = ...
    @classmethod
    def alloc(cls) -> Plane: ...
    def distance(self, point: Point3D) -> float: ...
    def equal(self, b: Plane) -> bool: ...
    def free(self) -> None: ...
    def get_constant(self) -> float: ...
    def get_normal(self) -> Vec3: ...
    def init(self, normal: Optional[Vec3], constant: float) -> Plane: ...
    def init_from_plane(self, src: Plane) -> Plane: ...
    def init_from_point(self, normal: Vec3, point: Point3D) -> Plane: ...
    def init_from_points(self, a: Point3D, b: Point3D, c: Point3D) -> Plane: ...
    def init_from_vec4(self, src: Vec4) -> Plane: ...
    def negate(self) -> Plane: ...
    def normalize(self) -> Plane: ...
    def transform(
        self, matrix: Matrix, normal_matrix: Optional[Matrix] = None
    ) -> Plane: ...

class Point(GObject.GBoxed):
    """
    :Constructors:

    ::

        Point()
        alloc() -> Graphene.Point
    """

    x: float = ...
    y: float = ...
    @classmethod
    def alloc(cls) -> Point: ...
    def distance(self, b: Point) -> Tuple[float, float, float]: ...
    def equal(self, b: Point) -> bool: ...
    def free(self) -> None: ...
    def init(self, x: float, y: float) -> Point: ...
    def init_from_point(self, src: Point) -> Point: ...
    def init_from_vec2(self, src: Vec2) -> Point: ...
    def interpolate(self, b: Point, factor: float) -> Point: ...
    def near(self, b: Point, epsilon: float) -> bool: ...
    def to_vec2(self) -> Vec2: ...
    @staticmethod
    def zero() -> Point: ...

class Point3D(GObject.GBoxed):
    """
    :Constructors:

    ::

        Point3D()
        alloc() -> Graphene.Point3D
    """

    x: float = ...
    y: float = ...
    z: float = ...
    @classmethod
    def alloc(cls) -> Point3D: ...
    def cross(self, b: Point3D) -> Point3D: ...
    def distance(self, b: Point3D) -> Tuple[float, Vec3]: ...
    def dot(self, b: Point3D) -> float: ...
    def equal(self, b: Point3D) -> bool: ...
    def free(self) -> None: ...
    def init(self, x: float, y: float, z: float) -> Point3D: ...
    def init_from_point(self, src: Point3D) -> Point3D: ...
    def init_from_vec3(self, v: Vec3) -> Point3D: ...
    def interpolate(self, b: Point3D, factor: float) -> Point3D: ...
    def length(self) -> float: ...
    def near(self, b: Point3D, epsilon: float) -> bool: ...
    def normalize(self) -> Point3D: ...
    def normalize_viewport(
        self, viewport: Rect, z_near: float, z_far: float
    ) -> Point3D: ...
    def scale(self, factor: float) -> Point3D: ...
    def to_vec3(self) -> Vec3: ...
    @staticmethod
    def zero() -> Point3D: ...

class Quad(GObject.GBoxed):
    """
    :Constructors:

    ::

        Quad()
        alloc() -> Graphene.Quad
    """

    points: list[Point] = ...
    @classmethod
    def alloc(cls) -> Quad: ...
    def bounds(self) -> Rect: ...
    def contains(self, p: Point) -> bool: ...
    def free(self) -> None: ...
    def get_point(self, index_: int) -> Point: ...
    def init(self, p1: Point, p2: Point, p3: Point, p4: Point) -> Quad: ...
    def init_from_points(self, points: Sequence[Point]) -> Quad: ...
    def init_from_rect(self, r: Rect) -> Quad: ...

class Quaternion(GObject.GBoxed):
    """
    :Constructors:

    ::

        Quaternion()
        alloc() -> Graphene.Quaternion
    """

    x: float = ...
    y: float = ...
    z: float = ...
    w: float = ...
    def add(self, b: Quaternion) -> Quaternion: ...
    @classmethod
    def alloc(cls) -> Quaternion: ...
    def dot(self, b: Quaternion) -> float: ...
    def equal(self, b: Quaternion) -> bool: ...
    def free(self) -> None: ...
    def init(self, x: float, y: float, z: float, w: float) -> Quaternion: ...
    def init_from_angle_vec3(self, angle: float, axis: Vec3) -> Quaternion: ...
    def init_from_angles(
        self, deg_x: float, deg_y: float, deg_z: float
    ) -> Quaternion: ...
    def init_from_euler(self, e: Euler) -> Quaternion: ...
    def init_from_matrix(self, m: Matrix) -> Quaternion: ...
    def init_from_quaternion(self, src: Quaternion) -> Quaternion: ...
    def init_from_radians(
        self, rad_x: float, rad_y: float, rad_z: float
    ) -> Quaternion: ...
    def init_from_vec4(self, src: Vec4) -> Quaternion: ...
    def init_identity(self) -> Quaternion: ...
    def invert(self) -> Quaternion: ...
    def multiply(self, b: Quaternion) -> Quaternion: ...
    def normalize(self) -> Quaternion: ...
    def scale(self, factor: float) -> Quaternion: ...
    def slerp(self, b: Quaternion, factor: float) -> Quaternion: ...
    def to_angle_vec3(self) -> Tuple[float, Vec3]: ...
    def to_angles(self) -> Tuple[float, float, float]: ...
    def to_matrix(self) -> Matrix: ...
    def to_radians(self) -> Tuple[float, float, float]: ...
    def to_vec4(self) -> Vec4: ...

class Ray(GObject.GBoxed):
    """
    :Constructors:

    ::

        Ray()
        alloc() -> Graphene.Ray
    """

    origin: Vec3 = ...
    direction: Vec3 = ...
    @classmethod
    def alloc(cls) -> Ray: ...
    def equal(self, b: Ray) -> bool: ...
    def free(self) -> None: ...
    def get_closest_point_to_point(self, p: Point3D) -> Point3D: ...
    def get_direction(self) -> Vec3: ...
    def get_distance_to_plane(self, p: Plane) -> float: ...
    def get_distance_to_point(self, p: Point3D) -> float: ...
    def get_origin(self) -> Point3D: ...
    def get_position_at(self, t: float) -> Point3D: ...
    def init(
        self, origin: Optional[Point3D] = None, direction: Optional[Vec3] = None
    ) -> Ray: ...
    def init_from_ray(self, src: Ray) -> Ray: ...
    def init_from_vec3(
        self, origin: Optional[Vec3] = None, direction: Optional[Vec3] = None
    ) -> Ray: ...
    def intersect_box(self, b: Box) -> Tuple[RayIntersectionKind, float]: ...
    def intersect_sphere(self, s: Sphere) -> Tuple[RayIntersectionKind, float]: ...
    def intersect_triangle(self, t: Triangle) -> Tuple[RayIntersectionKind, float]: ...
    def intersects_box(self, b: Box) -> bool: ...
    def intersects_sphere(self, s: Sphere) -> bool: ...
    def intersects_triangle(self, t: Triangle) -> bool: ...

class Rect(GObject.GBoxed):
    """
    :Constructors:

    ::

        Rect()
    """

    origin: Point = ...
    size: Size = ...
    @staticmethod
    def alloc() -> Rect: ...
    def contains_point(self, p: Point) -> bool: ...
    def contains_rect(self, b: Rect) -> bool: ...
    def equal(self, b: Rect) -> bool: ...
    def expand(self, p: Point) -> Rect: ...
    def free(self) -> None: ...
    def get_area(self) -> float: ...
    def get_bottom_left(self) -> Point: ...
    def get_bottom_right(self) -> Point: ...
    def get_center(self) -> Point: ...
    def get_height(self) -> float: ...
    def get_top_left(self) -> Point: ...
    def get_top_right(self) -> Point: ...
    def get_vertices(self) -> list[Vec2]: ...
    def get_width(self) -> float: ...
    def get_x(self) -> float: ...
    def get_y(self) -> float: ...
    def init(self, x: float, y: float, width: float, height: float) -> Rect: ...
    def init_from_rect(self, src: Rect) -> Rect: ...
    def inset(self, d_x: float, d_y: float) -> Rect: ...
    def inset_r(self, d_x: float, d_y: float) -> Rect: ...
    def interpolate(self, b: Rect, factor: float) -> Rect: ...
    def intersection(self, b: Rect) -> Tuple[bool, Rect]: ...
    def normalize(self) -> Rect: ...
    def normalize_r(self) -> Rect: ...
    def offset(self, d_x: float, d_y: float) -> Rect: ...
    def offset_r(self, d_x: float, d_y: float) -> Rect: ...
    def round(self) -> Rect: ...
    def round_extents(self) -> Rect: ...
    def round_to_pixel(self) -> Rect: ...
    def scale(self, s_h: float, s_v: float) -> Rect: ...
    def union(self, b: Rect) -> Rect: ...
    @staticmethod
    def zero() -> Rect: ...

class Simd4F(GObject.GPointer):
    """
    :Constructors:

    ::

        Simd4F()
    """

    x: float = ...
    y: float = ...
    z: float = ...
    w: float = ...

class Simd4X4F(GObject.GPointer):
    """
    :Constructors:

    ::

        Simd4X4F()
    """

    x: Simd4F = ...
    y: Simd4F = ...
    z: Simd4F = ...
    w: Simd4F = ...

class Size(GObject.GBoxed):
    """
    :Constructors:

    ::

        Size()
        alloc() -> Graphene.Size
    """

    width: float = ...
    height: float = ...
    @classmethod
    def alloc(cls) -> Size: ...
    def equal(self, b: Size) -> bool: ...
    def free(self) -> None: ...
    def init(self, width: float, height: float) -> Size: ...
    def init_from_size(self, src: Size) -> Size: ...
    def interpolate(self, b: Size, factor: float) -> Size: ...
    def scale(self, factor: float) -> Size: ...
    @staticmethod
    def zero() -> Size: ...

class Sphere(GObject.GBoxed):
    """
    :Constructors:

    ::

        Sphere()
        alloc() -> Graphene.Sphere
    """

    center: Vec3 = ...
    radius: float = ...
    @classmethod
    def alloc(cls) -> Sphere: ...
    def contains_point(self, point: Point3D) -> bool: ...
    def distance(self, point: Point3D) -> float: ...
    def equal(self, b: Sphere) -> bool: ...
    def free(self) -> None: ...
    def get_bounding_box(self) -> Box: ...
    def get_center(self) -> Point3D: ...
    def get_radius(self) -> float: ...
    def init(self, center: Optional[Point3D], radius: float) -> Sphere: ...
    def init_from_points(
        self, points: Sequence[Point3D], center: Optional[Point3D] = None
    ) -> Sphere: ...
    def init_from_vectors(
        self, vectors: Sequence[Vec3], center: Optional[Point3D] = None
    ) -> Sphere: ...
    def is_empty(self) -> bool: ...
    def translate(self, point: Point3D) -> Sphere: ...

class Triangle(GObject.GBoxed):
    """
    :Constructors:

    ::

        Triangle()
        alloc() -> Graphene.Triangle
    """

    a: Vec3 = ...
    b: Vec3 = ...
    c: Vec3 = ...
    @classmethod
    def alloc(cls) -> Triangle: ...
    def contains_point(self, p: Point3D) -> bool: ...
    def equal(self, b: Triangle) -> bool: ...
    def free(self) -> None: ...
    def get_area(self) -> float: ...
    def get_barycoords(self, p: Optional[Point3D] = None) -> Tuple[bool, Vec2]: ...
    def get_bounding_box(self) -> Box: ...
    def get_midpoint(self) -> Point3D: ...
    def get_normal(self) -> Vec3: ...
    def get_plane(self) -> Plane: ...
    def get_points(self) -> Tuple[Point3D, Point3D, Point3D]: ...
    def get_uv(
        self, p: Optional[Point3D], uv_a: Vec2, uv_b: Vec2, uv_c: Vec2
    ) -> Tuple[bool, Vec2]: ...
    def get_vertices(self) -> Tuple[Vec3, Vec3, Vec3]: ...
    def init_from_float(
        self, a: Sequence[float], b: Sequence[float], c: Sequence[float]
    ) -> Triangle: ...
    def init_from_point3d(
        self,
        a: Optional[Point3D] = None,
        b: Optional[Point3D] = None,
        c: Optional[Point3D] = None,
    ) -> Triangle: ...
    def init_from_vec3(
        self,
        a: Optional[Vec3] = None,
        b: Optional[Vec3] = None,
        c: Optional[Vec3] = None,
    ) -> Triangle: ...

class Vec2(GObject.GBoxed):
    """
    :Constructors:

    ::

        Vec2()
        alloc() -> Graphene.Vec2
    """

    value: Simd4F = ...
    def add(self, b: Vec2) -> Vec2: ...
    @classmethod
    def alloc(cls) -> Vec2: ...
    def divide(self, b: Vec2) -> Vec2: ...
    def dot(self, b: Vec2) -> float: ...
    def equal(self, v2: Vec2) -> bool: ...
    def free(self) -> None: ...
    def get_x(self) -> float: ...
    def get_y(self) -> float: ...
    def init(self, x: float, y: float) -> Vec2: ...
    def init_from_float(self, src: Sequence[float]) -> Vec2: ...
    def init_from_vec2(self, src: Vec2) -> Vec2: ...
    def interpolate(self, v2: Vec2, factor: float) -> Vec2: ...
    def length(self) -> float: ...
    def max(self, b: Vec2) -> Vec2: ...
    def min(self, b: Vec2) -> Vec2: ...
    def multiply(self, b: Vec2) -> Vec2: ...
    def near(self, v2: Vec2, epsilon: float) -> bool: ...
    def negate(self) -> Vec2: ...
    def normalize(self) -> Vec2: ...
    @staticmethod
    def one() -> Vec2: ...
    def scale(self, factor: float) -> Vec2: ...
    def subtract(self, b: Vec2) -> Vec2: ...
    def to_float(self) -> list[float]: ...
    @staticmethod
    def x_axis() -> Vec2: ...
    @staticmethod
    def y_axis() -> Vec2: ...
    @staticmethod
    def zero() -> Vec2: ...

class Vec3(GObject.GBoxed):
    """
    :Constructors:

    ::

        Vec3()
        alloc() -> Graphene.Vec3
    """

    value: Simd4F = ...
    def add(self, b: Vec3) -> Vec3: ...
    @classmethod
    def alloc(cls) -> Vec3: ...
    def cross(self, b: Vec3) -> Vec3: ...
    def divide(self, b: Vec3) -> Vec3: ...
    def dot(self, b: Vec3) -> float: ...
    def equal(self, v2: Vec3) -> bool: ...
    def free(self) -> None: ...
    def get_x(self) -> float: ...
    def get_xy(self) -> Vec2: ...
    def get_xy0(self) -> Vec3: ...
    def get_xyz0(self) -> Vec4: ...
    def get_xyz1(self) -> Vec4: ...
    def get_xyzw(self, w: float) -> Vec4: ...
    def get_y(self) -> float: ...
    def get_z(self) -> float: ...
    def init(self, x: float, y: float, z: float) -> Vec3: ...
    def init_from_float(self, src: Sequence[float]) -> Vec3: ...
    def init_from_vec3(self, src: Vec3) -> Vec3: ...
    def interpolate(self, v2: Vec3, factor: float) -> Vec3: ...
    def length(self) -> float: ...
    def max(self, b: Vec3) -> Vec3: ...
    def min(self, b: Vec3) -> Vec3: ...
    def multiply(self, b: Vec3) -> Vec3: ...
    def near(self, v2: Vec3, epsilon: float) -> bool: ...
    def negate(self) -> Vec3: ...
    def normalize(self) -> Vec3: ...
    @staticmethod
    def one() -> Vec3: ...
    def scale(self, factor: float) -> Vec3: ...
    def subtract(self, b: Vec3) -> Vec3: ...
    def to_float(self) -> list[float]: ...
    @staticmethod
    def x_axis() -> Vec3: ...
    @staticmethod
    def y_axis() -> Vec3: ...
    @staticmethod
    def z_axis() -> Vec3: ...
    @staticmethod
    def zero() -> Vec3: ...

class Vec4(GObject.GBoxed):
    """
    :Constructors:

    ::

        Vec4()
        alloc() -> Graphene.Vec4
    """

    value: Simd4F = ...
    def add(self, b: Vec4) -> Vec4: ...
    @classmethod
    def alloc(cls) -> Vec4: ...
    def divide(self, b: Vec4) -> Vec4: ...
    def dot(self, b: Vec4) -> float: ...
    def equal(self, v2: Vec4) -> bool: ...
    def free(self) -> None: ...
    def get_w(self) -> float: ...
    def get_x(self) -> float: ...
    def get_xy(self) -> Vec2: ...
    def get_xyz(self) -> Vec3: ...
    def get_y(self) -> float: ...
    def get_z(self) -> float: ...
    def init(self, x: float, y: float, z: float, w: float) -> Vec4: ...
    def init_from_float(self, src: Sequence[float]) -> Vec4: ...
    def init_from_vec2(self, src: Vec2, z: float, w: float) -> Vec4: ...
    def init_from_vec3(self, src: Vec3, w: float) -> Vec4: ...
    def init_from_vec4(self, src: Vec4) -> Vec4: ...
    def interpolate(self, v2: Vec4, factor: float) -> Vec4: ...
    def length(self) -> float: ...
    def max(self, b: Vec4) -> Vec4: ...
    def min(self, b: Vec4) -> Vec4: ...
    def multiply(self, b: Vec4) -> Vec4: ...
    def near(self, v2: Vec4, epsilon: float) -> bool: ...
    def negate(self) -> Vec4: ...
    def normalize(self) -> Vec4: ...
    @staticmethod
    def one() -> Vec4: ...
    def scale(self, factor: float) -> Vec4: ...
    def subtract(self, b: Vec4) -> Vec4: ...
    def to_float(self) -> list[float]: ...
    @staticmethod
    def w_axis() -> Vec4: ...
    @staticmethod
    def x_axis() -> Vec4: ...
    @staticmethod
    def y_axis() -> Vec4: ...
    @staticmethod
    def z_axis() -> Vec4: ...
    @staticmethod
    def zero() -> Vec4: ...

class EulerOrder(GObject.GEnum):
    DEFAULT = -1
    RXYX = 19
    RXYZ = 28
    RXZX = 21
    RXZY = 22
    RYXY = 25
    RYXZ = 26
    RYZX = 20
    RYZY = 23
    RZXY = 24
    RZXZ = 27
    RZYX = 18
    RZYZ = 29
    SXYX = 7
    SXYZ = 6
    SXZX = 9
    SXZY = 8
    SYXY = 13
    SYXZ = 12
    SYZX = 10
    SYZY = 11
    SZXY = 14
    SZXZ = 15
    SZYX = 16
    SZYZ = 17
    XYZ = 0
    XZY = 3
    YXZ = 4
    YZX = 1
    ZXY = 2
    ZYX = 5

class RayIntersectionKind(GObject.GEnum):
    ENTER = 1
    LEAVE = 2
    NONE = 0

    def init_from_vec4(self, src: Vec4) -> Vec4: ...
    def interpolate(self, v2: Vec4, factor: float) -> Vec4: ...
    def length(self) -> float: ...
    def max(self, b: Vec4) -> Vec4: ...
    def min(self, b: Vec4) -> Vec4: ...
    def multiply(self, b: Vec4) -> Vec4: ...
    def near(self, v2: Vec4, epsilon: float) -> bool: ...
    def negate(self) -> Vec4: ...
    def normalize(self) -> Vec4: ...
    @staticmethod
    def one() -> Vec4: ...
    def scale(self, factor: float) -> Vec4: ...
    def subtract(self, b: Vec4) -> Vec4: ...
    def to_float(self) -> list[float]: ...
    @staticmethod
    def w_axis() -> Vec4: ...
    @staticmethod
    def x_axis() -> Vec4: ...
    @staticmethod
    def y_axis() -> Vec4: ...
    @staticmethod
    def z_axis() -> Vec4: ...
    @staticmethod
    def zero() -> Vec4: ...

class EulerOrder(GObject.GEnum):
    DEFAULT = -1
    RXYX = 19
    RXYZ = 28
    RXZX = 21
    RXZY = 22
    RYXY = 25
    RYXZ = 26
    RYZX = 20
    RYZY = 23
    RZXY = 24
    RZXZ = 27
    RZYX = 18
    RZYZ = 29
    SXYX = 7
    SXYZ = 6
    SXZX = 9
    SXZY = 8
    SYXY = 13
    SYXZ = 12
    SYZX = 10
    SYZY = 11
    SZXY = 14
    SZXZ = 15
    SZYX = 16
    SZYZ = 17
    XYZ = 0
    XZY = 3
    YXZ = 4
    YZX = 1
    ZXY = 2
    ZYX = 5

class RayIntersectionKind(GObject.GEnum):
    ENTER = 1
    LEAVE = 2
    NONE = 0
