import typing

from gi.repository import Gio
from gi.repository import GObject
from typing_extensions import Self

T = typing.TypeVar("T")

FAKE_CAMERA_ACQUISITION_FRAME_RATE_DEFAULT: float = 25.0
FAKE_CAMERA_BINNING_HORIZONTAL_DEFAULT: int = 1
FAKE_CAMERA_BINNING_VERTICAL_DEFAULT: int = 1
FAKE_CAMERA_EXPOSURE_TIME_US_DEFAULT: float = 10000.0
FAKE_CAMERA_HEIGHT_DEFAULT: int = 512
FAKE_CAMERA_MEMORY_SIZE: int = 65536
FAKE_CAMERA_REGISTER_ACQUISITION: int = 292
FAKE_CAMERA_REGISTER_ACQUISITION_FRAME_PERIOD_US: int = 312
FAKE_CAMERA_REGISTER_ACQUISITION_MODE: int = 300
FAKE_CAMERA_REGISTER_ACQUISITION_START_OFFSET: int = 32
FAKE_CAMERA_REGISTER_BINNING_HORIZONTAL: int = 264
FAKE_CAMERA_REGISTER_BINNING_VERTICAL: int = 268
FAKE_CAMERA_REGISTER_EXPOSURE_TIME_US: int = 288
FAKE_CAMERA_REGISTER_FRAME_START_OFFSET: int = 0
FAKE_CAMERA_REGISTER_GAIN_MODE: int = 276
FAKE_CAMERA_REGISTER_GAIN_RAW: int = 272
FAKE_CAMERA_REGISTER_HEIGHT: int = 260
FAKE_CAMERA_REGISTER_PIXEL_FORMAT: int = 296
FAKE_CAMERA_REGISTER_SENSOR_HEIGHT: int = 280
FAKE_CAMERA_REGISTER_SENSOR_WIDTH: int = 284
FAKE_CAMERA_REGISTER_TEST: int = 496
FAKE_CAMERA_REGISTER_TRIGGER_ACTIVATION: int = 776
FAKE_CAMERA_REGISTER_TRIGGER_MODE: int = 768
FAKE_CAMERA_REGISTER_TRIGGER_SOFTWARE: int = 780
FAKE_CAMERA_REGISTER_TRIGGER_SOURCE: int = 772
FAKE_CAMERA_REGISTER_WIDTH: int = 256
FAKE_CAMERA_REGISTER_X_OFFSET: int = 304
FAKE_CAMERA_REGISTER_Y_OFFSET: int = 308
FAKE_CAMERA_SENSOR_HEIGHT: int = 2048
FAKE_CAMERA_SENSOR_WIDTH: int = 2048
FAKE_CAMERA_TEST_REGISTER_DEFAULT: int = 305419896
FAKE_CAMERA_WIDTH_DEFAULT: int = 512
GV_FAKE_CAMERA_DEFAULT_INTERFACE: str = "127.0.0.1"
GV_FAKE_CAMERA_DEFAULT_SERIAL_NUMBER: str = "GV01"
PIXEL_FORMAT_BAYER_BG_10: int = 17825807
PIXEL_FORMAT_BAYER_BG_10P: int = 17432658
PIXEL_FORMAT_BAYER_BG_10_PACKED: int = 17563689
PIXEL_FORMAT_BAYER_BG_12: int = 17825811
PIXEL_FORMAT_BAYER_BG_12P: int = 17563731
PIXEL_FORMAT_BAYER_BG_12_PACKED: int = 17563693
PIXEL_FORMAT_BAYER_BG_16: int = 17825841
PIXEL_FORMAT_BAYER_BG_8: int = 17301515
PIXEL_FORMAT_BAYER_GB_10: int = 17825806
PIXEL_FORMAT_BAYER_GB_10P: int = 17432660
PIXEL_FORMAT_BAYER_GB_10_PACKED: int = 17563688
PIXEL_FORMAT_BAYER_GB_12: int = 17825810
PIXEL_FORMAT_BAYER_GB_12P: int = 17563733
PIXEL_FORMAT_BAYER_GB_12_PACKED: int = 17563692
PIXEL_FORMAT_BAYER_GB_16: int = 17825840
PIXEL_FORMAT_BAYER_GB_8: int = 17301514
PIXEL_FORMAT_BAYER_GR_10: int = 17825804
PIXEL_FORMAT_BAYER_GR_10P: int = 17432662
PIXEL_FORMAT_BAYER_GR_10_PACKED: int = 17563686
PIXEL_FORMAT_BAYER_GR_12: int = 17825808
PIXEL_FORMAT_BAYER_GR_12P: int = 17563735
PIXEL_FORMAT_BAYER_GR_12_PACKED: int = 17563690
PIXEL_FORMAT_BAYER_GR_16: int = 17825838
PIXEL_FORMAT_BAYER_GR_8: int = 17301512
PIXEL_FORMAT_BAYER_RG_10: int = 17825805
PIXEL_FORMAT_BAYER_RG_10P: int = 17432664
PIXEL_FORMAT_BAYER_RG_10_PACKED: int = 17563687
PIXEL_FORMAT_BAYER_RG_12: int = 17825809
PIXEL_FORMAT_BAYER_RG_12P: int = 17563737
PIXEL_FORMAT_BAYER_RG_12_PACKED: int = 17563691
PIXEL_FORMAT_BAYER_RG_16: int = 17825839
PIXEL_FORMAT_BAYER_RG_8: int = 17301513
PIXEL_FORMAT_BGRA_8_PACKED: int = 35651607
PIXEL_FORMAT_BGR_10_PACKED: int = 36700185
PIXEL_FORMAT_BGR_12_PACKED: int = 36700187
PIXEL_FORMAT_BGR_8_PACKED: int = 35127317
PIXEL_FORMAT_COORD3D_ABC_10P: int = 35520731
PIXEL_FORMAT_COORD3D_ABC_10P_PLANAR: int = 35520732
PIXEL_FORMAT_COORD3D_ABC_12P: int = 35913950
PIXEL_FORMAT_COORD3D_ABC_12P_PLANAR: int = 35913951
PIXEL_FORMAT_COORD3D_ABC_16: int = 36700345
PIXEL_FORMAT_COORD3D_ABC_16_PLANAR: int = 36700346
PIXEL_FORMAT_COORD3D_ABC_32F: int = 39846080
PIXEL_FORMAT_COORD3D_ABC_32F_PLANAR: int = 39846081
PIXEL_FORMAT_COORD3D_ABC_8: int = 35127474
PIXEL_FORMAT_COORD3D_ABC_8_PLANAR: int = 35127475
PIXEL_FORMAT_COORD3D_AC_10P: int = 34865392
PIXEL_FORMAT_COORD3D_AC_10P_PLANAR: int = 34865393
PIXEL_FORMAT_COORD3D_AC_12P: int = 35127538
PIXEL_FORMAT_COORD3D_AC_12P_PLANAR: int = 35127539
PIXEL_FORMAT_COORD3D_AC_16: int = 35651771
PIXEL_FORMAT_COORD3D_AC_16_PLANAR: int = 35651772
PIXEL_FORMAT_COORD3D_AC_32F: int = 37748930
PIXEL_FORMAT_COORD3D_AC_32F_PLANAR: int = 37748931
PIXEL_FORMAT_COORD3D_AC_8: int = 34603188
PIXEL_FORMAT_COORD3D_AC_8_PLANAR: int = 34603189
PIXEL_FORMAT_COORD3D_A_10P: int = 17432789
PIXEL_FORMAT_COORD3D_A_12P: int = 17563864
PIXEL_FORMAT_COORD3D_A_16: int = 17825974
PIXEL_FORMAT_COORD3D_A_32F: int = 18874557
PIXEL_FORMAT_COORD3D_A_8: int = 17301679
PIXEL_FORMAT_COORD3D_B_10P: int = 17432790
PIXEL_FORMAT_COORD3D_B_12P: int = 17563865
PIXEL_FORMAT_COORD3D_B_16: int = 17825975
PIXEL_FORMAT_COORD3D_B_32F: int = 18874558
PIXEL_FORMAT_COORD3D_B_8: int = 17301680
PIXEL_FORMAT_COORD3D_C_10P: int = 17432791
PIXEL_FORMAT_COORD3D_C_12P: int = 17563866
PIXEL_FORMAT_COORD3D_C_16: int = 17825976
PIXEL_FORMAT_COORD3D_C_32F: int = 18874559
PIXEL_FORMAT_COORD3D_C_8: int = 17301681
PIXEL_FORMAT_CUSTOM_BAYER_BG_12_PACKED: int = 2165047300
PIXEL_FORMAT_CUSTOM_BAYER_BG_16: int = 2165309449
PIXEL_FORMAT_CUSTOM_BAYER_GB_12_PACKED: int = 2165047299
PIXEL_FORMAT_CUSTOM_BAYER_GB_16: int = 2165309448
PIXEL_FORMAT_CUSTOM_BAYER_GR_12_PACKED: int = 2165047297
PIXEL_FORMAT_CUSTOM_BAYER_GR_16: int = 2165309446
PIXEL_FORMAT_CUSTOM_BAYER_RG_12_PACKED: int = 2165047298
PIXEL_FORMAT_CUSTOM_BAYER_RG_16: int = 2165309447
PIXEL_FORMAT_CUSTOM_YUV_422_YUYV_PACKED: int = 2182086661
PIXEL_FORMAT_DATA_16: int = 17826072
PIXEL_FORMAT_DATA_16S: int = 17826073
PIXEL_FORMAT_DATA_32: int = 18874650
PIXEL_FORMAT_DATA_32F: int = 18874652
PIXEL_FORMAT_DATA_32S: int = 18874651
PIXEL_FORMAT_DATA_64: int = 20971805
PIXEL_FORMAT_DATA_64F: int = 20971807
PIXEL_FORMAT_DATA_64S: int = 20971806
PIXEL_FORMAT_DATA_8: int = 17301782
PIXEL_FORMAT_DATA_8S: int = 17301783
PIXEL_FORMAT_MONO_10: int = 17825795
PIXEL_FORMAT_MONO_10_PACKED: int = 17563652
PIXEL_FORMAT_MONO_12: int = 17825797
PIXEL_FORMAT_MONO_12_PACKED: int = 17563654
PIXEL_FORMAT_MONO_14: int = 17825829
PIXEL_FORMAT_MONO_16: int = 17825799
PIXEL_FORMAT_MONO_8: int = 17301505
PIXEL_FORMAT_MONO_8_SIGNED: int = 17301506
PIXEL_FORMAT_RGBA_8_PACKED: int = 35651606
PIXEL_FORMAT_RGB_10_PACKED: int = 36700184
PIXEL_FORMAT_RGB_10_PLANAR: int = 36700194
PIXEL_FORMAT_RGB_12_PACKED: int = 36700186
PIXEL_FORMAT_RGB_12_PLANAR: int = 36700195
PIXEL_FORMAT_RGB_16_PLANAR: int = 36700196
PIXEL_FORMAT_RGB_8_PACKED: int = 35127316
PIXEL_FORMAT_RGB_8_PLANAR: int = 35127329
PIXEL_FORMAT_YUV_411_PACKED: int = 34340894
PIXEL_FORMAT_YUV_422_PACKED: int = 34603039
PIXEL_FORMAT_YUV_422_YUYV_PACKED: int = 34603058
PIXEL_FORMAT_YUV_444_PACKED: int = 35127328

def acquisition_mode_from_string(string: str) -> AcquisitionMode: ...
def acquisition_mode_to_string(value: AcquisitionMode) -> str: ...
def auto_from_string(string: str) -> Auto: ...
def auto_to_string(value: Auto) -> str: ...
def chunk_parser_error_quark() -> int: ...
def debug_enable(category_selection: str) -> bool: ...
def device_error_quark() -> int: ...
def disable_interface(interface_id: str) -> None: ...
def dom_implementation_add_document_type(
    qualified_name: str, document_type: typing.Type[typing.Any]
) -> None: ...
def dom_implementation_cleanup() -> None: ...
def dom_implementation_create_document(
    namespace_uri: str, qualified_name: str
) -> DomDocument: ...
def enable_interface(interface_id: str) -> None: ...
def exposure_mode_from_string(string: str) -> ExposureMode: ...
def exposure_mode_to_string(value: ExposureMode) -> str: ...
def gc_access_mode_from_string(string: str) -> GcAccessMode: ...
def gc_access_mode_to_string(value: GcAccessMode) -> str: ...
def gc_error_quark() -> int: ...
def get_device_address(index: int) -> str: ...
def get_device_id(index: int) -> str: ...
def get_device_manufacturer_info(index: int) -> str: ...
def get_device_model(index: int) -> str: ...
def get_device_physical_id(index: int) -> str: ...
def get_device_protocol(index: int) -> str: ...
def get_device_serial_nbr(index: int) -> str: ...
def get_device_vendor(index: int) -> str: ...
def get_interface_id(index: int) -> str: ...
def get_n_devices() -> int: ...
def get_n_interfaces() -> int: ...
def make_thread_high_priority(nice_level: int) -> bool: ...
def make_thread_realtime(priority: int) -> bool: ...
def open_device(device_id: str | None = None) -> Device: ...
def set_fake_camera_genicam_filename(filename: str) -> None: ...
def set_interface_flags(interface_id: str, flags: int) -> None: ...
def shutdown() -> None: ...
def update_device_list() -> None: ...
def xml_schema_error_quark() -> int: ...

class Buffer(GObject.Object):
    """
    :Constructors:

    ::

        Buffer(**properties)
        new(size:int, preallocated=None) -> Aravis.Buffer
        new_allocate(size:int) -> Aravis.Buffer
        new_full(size:int, preallocated=None, user_data=None, user_data_destroy_func:GLib.DestroyNotify=None) -> Aravis.Buffer

    Object ArvBuffer

    Signals from GObject:
      notify (GParam)
    """
    def find_component(self, component_id: int) -> int: ...
    def get_chunk_data(self, chunk_id: int) -> bytes: ...
    def get_data(self) -> bytes: ...
    def get_frame_id(self) -> int: ...
    def get_gendc_data(self) -> bytes: ...
    def get_gendc_descriptor(self) -> bytes: ...
    def get_image_data(self) -> bytes: ...
    def get_image_height(self) -> int: ...
    def get_image_padding(self) -> typing.Tuple[int, int]: ...
    def get_image_pixel_format(self) -> int: ...
    def get_image_region(self) -> typing.Tuple[int, int, int, int]: ...
    def get_image_width(self) -> int: ...
    def get_image_x(self) -> int: ...
    def get_image_y(self) -> int: ...
    def get_n_parts(self) -> int: ...
    def get_part_component_id(self, part_id: int) -> int: ...
    def get_part_data(self, part_id: int) -> bytes: ...
    def get_part_data_type(self, part_id: int) -> BufferPartDataType: ...
    def get_part_height(self, part_id: int) -> int: ...
    def get_part_padding(self, part_id: int) -> typing.Tuple[int, int]: ...
    def get_part_pixel_format(self, part_id: int) -> int: ...
    def get_part_region(self, part_id: int) -> typing.Tuple[int, int, int, int]: ...
    def get_part_width(self, part_id: int) -> int: ...
    def get_part_x(self, part_id: int) -> int: ...
    def get_part_y(self, part_id: int) -> int: ...
    def get_payload_type(self) -> BufferPayloadType: ...
    def get_status(self) -> BufferStatus: ...
    def get_system_timestamp(self) -> int: ...
    def get_timestamp(self) -> int: ...
    def get_user_data(self) -> None: ...
    def has_chunks(self) -> bool: ...
    def has_gendc(self) -> bool: ...
    @classmethod
    def new(cls, size: int, preallocated: None) -> Buffer: ...
    @classmethod
    def new_allocate(cls, size: int) -> Buffer: ...
    @classmethod
    def new_full(
        cls,
        size: int,
        preallocated: None,
        user_data: None,
        user_data_destroy_func: typing.Callable[[None], None] | None = None,
    ) -> Buffer: ...
    def set_frame_id(self, frame_id: int) -> None: ...
    def set_system_timestamp(self, timestamp_ns: int) -> None: ...
    def set_timestamp(self, timestamp_ns: int) -> None: ...

class BufferClass(GObject.GPointer):
    """
    :Constructors:

    ::

        BufferClass()
    """

    parent_class: GObject.ObjectClass = ...

class Camera(GObject.Object, Gio.Initable):
    """
    :Constructors:

    ::

        Camera(**properties)
        new(name:str=None) -> Aravis.Camera
        new_with_device(device:Aravis.Device) -> Aravis.Camera

    Object ArvCamera

    Properties from ArvCamera:
      name -> gchararray: Camera name
        The camera name
      device -> ArvDevice: Device
        The device associated with this camera

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        device: Device
        name: str

    props: Props = ...
    parent_instance: GObject.Object = ...
    def __init__(self, *, device: Device = ..., name: str = ...) -> None: ...
    def abort_acquisition(self) -> None: ...
    def acquisition(self, timeout: int) -> Buffer: ...
    def are_chunks_available(self) -> bool: ...
    def clear_triggers(self) -> None: ...
    def create_chunk_parser(self) -> ChunkParser: ...
    def create_stream(
        self,
        callback: typing.Callable[..., None] | None = None,
        *user_data: typing.Any,
    ) -> Stream: ...
    def dup_available_black_levels(self) -> list[str]: ...
    def dup_available_components(self) -> list[str]: ...
    def dup_available_enumerations(self, feature: str) -> list[int]: ...
    def dup_available_enumerations_as_display_names(
        self, feature: str
    ) -> list[str]: ...
    def dup_available_enumerations_as_strings(self, feature: str) -> list[str]: ...
    def dup_available_gains(self) -> list[str]: ...
    def dup_available_pixel_formats(self) -> list[int]: ...
    def dup_available_pixel_formats_as_display_names(self) -> list[str]: ...
    def dup_available_pixel_formats_as_strings(self) -> list[str]: ...
    def dup_available_trigger_sources(self) -> list[str]: ...
    def dup_available_triggers(self) -> list[str]: ...
    def dup_register(self, feature: str) -> int: ...
    def execute_command(self, feature: str) -> None: ...
    def get_acquisition_mode(self) -> AcquisitionMode: ...
    def get_binning(self) -> typing.Tuple[int, int]: ...
    def get_black_level(self) -> float: ...
    def get_black_level_auto(self) -> Auto: ...
    def get_black_level_bounds(self) -> typing.Tuple[float, float]: ...
    def get_boolean(self, feature: str) -> bool: ...
    def get_chunk_mode(self) -> bool: ...
    def get_chunk_state(self, chunk: str) -> bool: ...
    def get_device(self) -> Device: ...
    def get_device_id(self) -> str: ...
    def get_device_serial_number(self) -> str: ...
    def get_exposure_time(self) -> float: ...
    def get_exposure_time_auto(self) -> Auto: ...
    def get_exposure_time_bounds(self) -> typing.Tuple[float, float]: ...
    def get_exposure_time_representation(self) -> GcRepresentation: ...
    def get_feature_representation(self, feature: str) -> GcRepresentation: ...
    def get_float(self, feature: str) -> float: ...
    def get_float_bounds(self, feature: str) -> typing.Tuple[float, float]: ...
    def get_float_increment(self, feature: str) -> float: ...
    def get_frame_count(self) -> int: ...
    def get_frame_count_bounds(self) -> typing.Tuple[int, int]: ...
    def get_frame_rate(self) -> float: ...
    def get_frame_rate_bounds(self) -> typing.Tuple[float, float]: ...
    def get_frame_rate_enable(self) -> bool: ...
    def get_gain(self) -> float: ...
    def get_gain_auto(self) -> Auto: ...
    def get_gain_bounds(self) -> typing.Tuple[float, float]: ...
    def get_gain_representation(self) -> GcRepresentation: ...
    def get_height_bounds(self) -> typing.Tuple[int, int]: ...
    def get_height_increment(self) -> int: ...
    def get_integer(self, feature: str) -> int: ...
    def get_integer_bounds(self, feature: str) -> typing.Tuple[int, int]: ...
    def get_integer_increment(self, feature: str) -> int: ...
    def get_model_name(self) -> str: ...
    def get_payload(self) -> int: ...
    def get_pixel_format(self) -> int: ...
    def get_pixel_format_as_string(self) -> str: ...
    def get_region(self) -> typing.Tuple[int, int, int, int]: ...
    def get_sensor_size(self) -> typing.Tuple[int, int]: ...
    def get_string(self, feature: str) -> str: ...
    def get_trigger_source(self) -> str: ...
    def get_vendor_name(self) -> str: ...
    def get_width_bounds(self) -> typing.Tuple[int, int]: ...
    def get_width_increment(self) -> int: ...
    def get_x_binning_bounds(self) -> typing.Tuple[int, int]: ...
    def get_x_binning_increment(self) -> int: ...
    def get_x_offset_bounds(self) -> typing.Tuple[int, int]: ...
    def get_x_offset_increment(self) -> int: ...
    def get_y_binning_bounds(self) -> typing.Tuple[int, int]: ...
    def get_y_binning_increment(self) -> int: ...
    def get_y_offset_bounds(self) -> typing.Tuple[int, int]: ...
    def get_y_offset_increment(self) -> int: ...
    def gv_auto_packet_size(self) -> int: ...
    def gv_get_current_stream_channel(self) -> int: ...
    def gv_get_ip_configuration_mode(self) -> GvIpConfigurationMode: ...
    def gv_get_multipart(self) -> bool: ...
    def gv_get_n_network_interfaces(self) -> int: ...
    def gv_get_n_stream_channels(self) -> int: ...
    def gv_get_packet_delay(self) -> int: ...
    def gv_get_packet_size(self) -> int: ...
    def gv_get_persistent_ip(
        self,
    ) -> typing.Tuple[Gio.InetAddress, Gio.InetAddressMask, Gio.InetAddress]: ...
    def gv_is_multipart_supported(self) -> bool: ...
    def gv_select_stream_channel(self, channel_id: int) -> None: ...
    def gv_set_ip_configuration_mode(self, mode: GvIpConfigurationMode) -> None: ...
    def gv_set_multipart(self, enable: bool) -> None: ...
    def gv_set_packet_delay(self, delay_ns: int) -> None: ...
    def gv_set_packet_size(self, packet_size: int) -> None: ...
    def gv_set_packet_size_adjustment(
        self, adjustment: GvPacketSizeAdjustment
    ) -> None: ...
    def gv_set_persistent_ip(
        self, ip: Gio.InetAddress, mask: Gio.InetAddressMask, gateway: Gio.InetAddress
    ) -> None: ...
    def gv_set_persistent_ip_from_string(
        self, ip: str, mask: str, gateway: str
    ) -> None: ...
    def gv_set_stream_options(self, options: GvStreamOption) -> None: ...
    def is_binning_available(self) -> bool: ...
    def is_black_level_auto_available(self) -> bool: ...
    def is_black_level_available(self) -> bool: ...
    def is_component_available(self) -> bool: ...
    def is_enumeration_entry_available(self, feature: str, entry: str) -> bool: ...
    def is_exposure_auto_available(self) -> bool: ...
    def is_exposure_time_available(self) -> bool: ...
    def is_feature_available(self, feature: str) -> bool: ...
    def is_feature_implemented(self, feature: str) -> bool: ...
    def is_frame_rate_available(self) -> bool: ...
    def is_gain_auto_available(self) -> bool: ...
    def is_gain_available(self) -> bool: ...
    def is_gv_device(self) -> bool: ...
    def is_region_offset_available(self) -> bool: ...
    def is_software_trigger_supported(self) -> bool: ...
    def is_uv_device(self) -> bool: ...
    @classmethod
    def new(cls, name: str | None = None) -> Camera: ...
    @classmethod
    def new_with_device(cls, device: Device) -> Camera: ...
    def select_and_enable_component(
        self, component: str, disable_others: bool
    ) -> None: ...
    def select_black_level(self, selector: str) -> None: ...
    def select_component(
        self, component: str, flags: ComponentSelectionFlags
    ) -> typing.Tuple[bool, int]: ...
    def select_gain(self, selector: str) -> None: ...
    def set_access_check_policy(self, policy: AccessCheckPolicy) -> None: ...
    def set_acquisition_mode(self, value: AcquisitionMode) -> None: ...
    def set_binning(self, dx: int, dy: int) -> None: ...
    def set_black_level(self, blacklevel: float) -> None: ...
    def set_black_level_auto(self, auto_mode: Auto) -> None: ...
    def set_boolean(self, feature: str, value: bool) -> None: ...
    def set_chunk_mode(self, is_active: bool) -> None: ...
    def set_chunk_state(self, chunk: str, is_enabled: bool) -> None: ...
    def set_chunks(self, chunk_list: str) -> None: ...
    def set_exposure_mode(self, mode: ExposureMode) -> None: ...
    def set_exposure_time(self, exposure_time_us: float) -> None: ...
    def set_exposure_time_auto(self, auto_mode: Auto) -> None: ...
    def set_float(self, feature: str, value: float) -> None: ...
    def set_frame_count(self, frame_count: int) -> None: ...
    def set_frame_rate(self, frame_rate: float) -> None: ...
    def set_frame_rate_enable(self, enable: bool) -> None: ...
    def set_gain(self, gain: float) -> None: ...
    def set_gain_auto(self, auto_mode: Auto) -> None: ...
    def set_integer(self, feature: str, value: int) -> None: ...
    def set_pixel_format(self, format: int) -> None: ...
    def set_pixel_format_from_string(self, format: str) -> None: ...
    def set_range_check_policy(self, policy: RangeCheckPolicy) -> None: ...
    def set_region(self, x: int, y: int, width: int, height: int) -> None: ...
    def set_register(self, feature: str, length: int, value: None) -> None: ...
    def set_register_cache_policy(self, policy: RegisterCachePolicy) -> None: ...
    def set_string(self, feature: str, value: str) -> None: ...
    def set_trigger(self, source: str) -> None: ...
    def set_trigger_source(self, source: str) -> None: ...
    def software_trigger(self) -> None: ...
    def start_acquisition(self) -> None: ...
    def stop_acquisition(self) -> None: ...
    def uv_get_bandwidth(self) -> int: ...
    def uv_get_bandwidth_bounds(self) -> typing.Tuple[int, int]: ...
    def uv_is_bandwidth_control_available(self) -> bool: ...
    def uv_set_bandwidth(self, bandwidth: int) -> None: ...
    def uv_set_usb_mode(self, usb_mode: UvUsbMode) -> None: ...

class CameraClass(GObject.GPointer):
    """
    :Constructors:

    ::

        CameraClass()
    """

    parent_class: GObject.ObjectClass = ...

class ChunkParser(GObject.Object):
    """
    :Constructors:

    ::

        ChunkParser(**properties)
        new(xml:str, size:int) -> Aravis.ChunkParser

    Object ArvChunkParser

    Properties from ArvChunkParser:
      genicam -> ArvGc: genicam
        Genicam instance

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        genicam: Gc

    props: Props = ...
    def __init__(self, *, genicam: Gc = ...) -> None: ...
    def get_boolean_value(self, buffer: Buffer, chunk: str) -> bool: ...
    def get_float_value(self, buffer: Buffer, chunk: str) -> float: ...
    def get_integer_value(self, buffer: Buffer, chunk: str) -> int: ...
    def get_string_value(self, buffer: Buffer, chunk: str) -> str: ...
    @classmethod
    def new(cls, xml: str, size: int) -> ChunkParser: ...

class ChunkParserClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ChunkParserClass()
    """

    parent_class: GObject.ObjectClass = ...

class Device(GObject.Object, Gio.Initable):
    """
    :Constructors:

    ::

        Device(**properties)

    Object ArvDevice

    Signals from ArvDevice:
      control-lost ()

    Signals from GObject:
      notify (GParam)
    """

    parent_instance: GObject.Object = ...
    def create_chunk_parser(self) -> ChunkParser: ...
    def create_stream(
        self, callback: typing.Callable[..., None], *user_data: typing.Any
    ) -> Stream: ...
    def do_control_lost(self) -> None: ...
    def do_get_genicam(self) -> Gc: ...
    def do_get_genicam_xml(self) -> typing.Tuple[str, int]: ...
    def do_read_memory(self, address: int, size: int, buffer: None) -> bool: ...
    def do_read_register(self, address: int) -> typing.Tuple[bool, int]: ...
    def do_write_memory(self, address: int, size: int, buffer: None) -> bool: ...
    def do_write_register(self, address: int, value: int) -> bool: ...
    def dup_available_enumeration_feature_values(self, feature: str) -> list[int]: ...
    def dup_available_enumeration_feature_values_as_display_names(
        self, feature: str
    ) -> list[str]: ...
    def dup_available_enumeration_feature_values_as_strings(
        self, feature: str
    ) -> list[str]: ...
    def dup_register_feature_value(self, feature: str) -> int: ...
    def execute_command(self, feature: str) -> None: ...
    def get_boolean_feature_value(self, feature: str) -> bool: ...
    def get_feature(self, feature: str) -> GcNode: ...
    def get_feature_access_mode(self, feature: str) -> GcAccessMode: ...
    def get_feature_representation(self, feature: str) -> GcRepresentation: ...
    def get_feature_value(self, feature: str) -> typing.Any: ...
    def get_float_feature_bounds(self, feature: str) -> typing.Tuple[float, float]: ...
    def get_float_feature_increment(self, feature: str) -> float: ...
    def get_float_feature_value(self, feature: str) -> float: ...
    def get_genicam(self) -> Gc: ...
    def get_genicam_xml(self) -> typing.Tuple[str, int]: ...
    def get_integer_feature_bounds(self, feature: str) -> typing.Tuple[int, int]: ...
    def get_integer_feature_increment(self, feature: str) -> int: ...
    def get_integer_feature_value(self, feature: str) -> int: ...
    def get_string_feature_value(self, feature: str) -> str: ...
    def is_enumeration_entry_available(self, feature: str, entry: str) -> bool: ...
    def is_feature_available(self, feature: str) -> bool: ...
    def is_feature_implemented(self, feature: str) -> bool: ...
    def read_memory(self, address: int, size: int, buffer: None) -> bool: ...
    def read_register(self, address: int) -> typing.Tuple[bool, int]: ...
    def set_access_check_policy(self, policy: AccessCheckPolicy) -> None: ...
    def set_boolean_feature_value(self, feature: str, value: bool) -> None: ...
    def set_feature_value(self, feature: str, value: typing.Any) -> None: ...
    def set_features_from_string(self, string: str) -> bool: ...
    def set_float_feature_value(self, feature: str, value: float) -> None: ...
    def set_integer_feature_value(self, feature: str, value: int) -> None: ...
    def set_range_check_policy(self, policy: RangeCheckPolicy) -> None: ...
    def set_register_cache_policy(self, policy: RegisterCachePolicy) -> None: ...
    def set_register_feature_value(
        self, feature: str, length: int, value: None
    ) -> None: ...
    def set_string_feature_value(self, feature: str, value: str) -> None: ...
    def write_memory(self, address: int, size: int, buffer: None) -> bool: ...
    def write_register(self, address: int, value: int) -> bool: ...

class DeviceClass(GObject.GPointer):
    """
    :Constructors:

    ::

        DeviceClass()
    """

    parent_class: GObject.ObjectClass = ...
    create_stream: None = ...
    get_genicam_xml: typing.Callable[[Device], typing.Tuple[str, int]] = ...
    get_genicam: typing.Callable[[Device], Gc] = ...
    read_memory: typing.Callable[[Device, int, int, None], bool] = ...
    write_memory: typing.Callable[[Device, int, int, None], bool] = ...
    read_register: typing.Callable[[Device, int], typing.Tuple[bool, int]] = ...
    write_register: typing.Callable[[Device, int, int], bool] = ...
    control_lost: typing.Callable[[Device], None] = ...

class DomCharacterData(DomNode):
    """
    :Constructors:

    ::

        DomCharacterData(**properties)

    Object ArvDomCharacterData

    Signals from GObject:
      notify (GParam)
    """

    parent_instance: DomNode = ...
    def get_data(self) -> str: ...
    def set_data(self, value: str) -> None: ...

class DomCharacterDataClass(GObject.GPointer):
    """
    :Constructors:

    ::

        DomCharacterDataClass()
    """

    parent_class: DomNodeClass = ...

class DomDocument(DomNode):
    """
    :Constructors:

    ::

        DomDocument(**properties)
        new_from_memory(buffer=None, size:int) -> Aravis.DomDocument
        new_from_path(path:str) -> Aravis.DomDocument
        new_from_url(url:str) -> Aravis.DomDocument

    Object ArvDomDocument

    Signals from GObject:
      notify (GParam)
    """

    parent_instance: DomNode = ...
    def append_from_memory(self, node: DomNode, buffer: None, size: int) -> None: ...
    def create_element(self, tag_name: str) -> DomElement: ...
    def create_text_node(self, data: str) -> DomText: ...
    def do_create_element(self, tag_name: str) -> DomElement: ...
    def do_create_text_node(self, data: str) -> DomText: ...
    def do_get_document_element(self) -> DomElement: ...
    def get_document_element(self) -> DomElement: ...
    def get_href_data(self, href: str, size: int) -> None: ...
    def get_url(self) -> str: ...
    @classmethod
    def new_from_memory(cls, buffer: None, size: int) -> DomDocument: ...
    @classmethod
    def new_from_path(cls, path: str) -> DomDocument: ...
    @classmethod
    def new_from_url(cls, url: str) -> DomDocument: ...
    def set_path(self, path: str) -> None: ...
    def set_url(self, url: str) -> None: ...

class DomDocumentClass(GObject.GPointer):
    """
    :Constructors:

    ::

        DomDocumentClass()
    """

    parent_class: DomNodeClass = ...
    get_document_element: typing.Callable[[DomDocument], DomElement] = ...
    create_element: typing.Callable[[DomDocument, str], DomElement] = ...
    create_text_node: typing.Callable[[DomDocument, str], DomText] = ...

class DomDocumentFragment(DomNode):
    """
    :Constructors:

    ::

        DomDocumentFragment(**properties)
        new() -> Aravis.DomDocumentFragment

    Object ArvDomDocumentFragment

    Signals from GObject:
      notify (GParam)
    """

    parent_instance: DomNode = ...
    @classmethod
    def new(cls) -> DomDocumentFragment: ...

class DomDocumentFragmentClass(GObject.GPointer):
    """
    :Constructors:

    ::

        DomDocumentFragmentClass()
    """

    parent_class: DomNodeClass = ...

class DomElement(DomNode):
    """
    :Constructors:

    ::

        DomElement(**properties)

    Object ArvDomElement

    Signals from GObject:
      notify (GParam)
    """

    parent_instance: DomNode = ...
    def do_get_attribute(self, name: str) -> str: ...
    def do_set_attribute(self, name: str, attribute_value: str) -> None: ...
    def get_attribute(self, name: str) -> str: ...
    def get_tag_name(self) -> str: ...
    def set_attribute(self, name: str, attribute_value: str) -> None: ...

class DomElementClass(GObject.GPointer):
    """
    :Constructors:

    ::

        DomElementClass()
    """

    parent_class: DomNodeClass = ...
    get_attribute: typing.Callable[[DomElement, str], str] = ...
    set_attribute: typing.Callable[[DomElement, str, str], None] = ...

class DomNamedNodeMap(GObject.Object):
    """
    :Constructors:

    ::

        DomNamedNodeMap(**properties)

    Object ArvDomNamedNodeMap

    Signals from GObject:
      notify (GParam)
    """

    parent_instance: GObject.Object = ...
    def do_get_item(self, index: int) -> DomNode: ...
    def do_get_length(self) -> int: ...
    def get_item(self, index: int) -> DomNode: ...
    def get_length(self) -> int: ...
    def get_named_item(self, name: str) -> DomNode: ...
    def remove_named_item(self, name: str) -> DomNode: ...
    def set_named_item(self, item: DomNode) -> DomNode: ...

class DomNamedNodeMapClass(GObject.GPointer):
    """
    :Constructors:

    ::

        DomNamedNodeMapClass()
    """

    parent_class: GObject.ObjectClass = ...
    get: None = ...
    set: None = ...
    remove: None = ...
    get_item: typing.Callable[[DomNamedNodeMap, int], DomNode] = ...
    get_length: typing.Callable[[DomNamedNodeMap], int] = ...

class DomNode(GObject.Object):
    """
    :Constructors:

    ::

        DomNode(**properties)

    Object ArvDomNode

    Signals from GObject:
      notify (GParam)
    """

    parent_instance: GObject.Object = ...
    def append_child(self, new_child: DomNode) -> DomNode: ...
    def changed(self) -> None: ...
    def do_can_append_child(self, new_child: DomNode) -> bool: ...
    def do_changed(self) -> None: ...
    def do_child_changed(self, child: DomNode) -> bool: ...
    def do_get_node_name(self) -> str: ...
    def do_get_node_type(self) -> DomNodeType: ...
    def do_get_node_value(self) -> str: ...
    def do_post_new_child(self, child: DomNode) -> None: ...
    def do_pre_remove_child(self, child: DomNode) -> None: ...
    def do_set_node_value(self, new_value: str) -> None: ...
    def get_child_nodes(self) -> DomNodeList: ...
    def get_first_child(self) -> DomNode: ...
    def get_last_child(self) -> DomNode: ...
    def get_next_sibling(self) -> DomNode: ...
    def get_node_name(self) -> str: ...
    def get_node_type(self) -> DomNodeType: ...
    def get_node_value(self) -> str: ...
    def get_owner_document(self) -> DomDocument: ...
    def get_parent_node(self) -> DomNode: ...
    def get_previous_sibling(self) -> DomNode: ...
    def has_child_nodes(self) -> bool: ...
    def insert_before(self, new_child: DomNode, ref_child: DomNode) -> DomNode: ...
    def remove_child(self, old_child: DomNode) -> DomNode: ...
    def replace_child(self, new_child: DomNode, old_child: DomNode) -> DomNode: ...
    def set_node_value(self, new_value: str) -> None: ...

class DomNodeChildList(DomNodeList):
    """
    :Constructors:

    ::

        DomNodeChildList(**properties)
        new(parent_node:Aravis.DomNode) -> Aravis.DomNodeList

    Object ArvDomNodeChildList

    Signals from GObject:
      notify (GParam)
    """
    @classmethod
    def new(cls, parent_node: DomNode) -> DomNodeChildList: ...

class DomNodeChildListClass(GObject.GPointer):
    """
    :Constructors:

    ::

        DomNodeChildListClass()
    """

    parent_class: DomNodeListClass = ...

class DomNodeClass(GObject.GPointer):
    """
    :Constructors:

    ::

        DomNodeClass()
    """

    parent_class: GObject.ObjectClass = ...
    get_node_name: typing.Callable[[DomNode], str] = ...
    get_node_value: typing.Callable[[DomNode], str] = ...
    set_node_value: typing.Callable[[DomNode, str], None] = ...
    get_node_type: typing.Callable[[DomNode], DomNodeType] = ...
    can_append_child: typing.Callable[[DomNode, DomNode], bool] = ...
    post_new_child: typing.Callable[[DomNode, DomNode], None] = ...
    pre_remove_child: typing.Callable[[DomNode, DomNode], None] = ...
    changed: typing.Callable[[DomNode], None] = ...
    child_changed: typing.Callable[[DomNode, DomNode], bool] = ...

class DomNodeList(GObject.Object):
    """
    :Constructors:

    ::

        DomNodeList(**properties)

    Object ArvDomNodeList

    Signals from GObject:
      notify (GParam)
    """

    parent_instance: GObject.Object = ...
    def do_get_item(self, index: int) -> DomNode: ...
    def do_get_length(self) -> int: ...
    def get_item(self, index: int) -> DomNode: ...
    def get_length(self) -> int: ...

class DomNodeListClass(GObject.GPointer):
    """
    :Constructors:

    ::

        DomNodeListClass()
    """

    parent_class: GObject.ObjectClass = ...
    get_item: typing.Callable[[DomNodeList, int], DomNode] = ...
    get_length: typing.Callable[[DomNodeList], int] = ...

class DomText(DomCharacterData):
    """
    :Constructors:

    ::

        DomText(**properties)
        new(data:str) -> Aravis.DomNode

    Object ArvDomText

    Signals from GObject:
      notify (GParam)
    """

    parent_instance: DomCharacterData = ...
    @classmethod
    def new(cls, data: str) -> DomText: ...

class DomTextClass(GObject.GPointer):
    """
    :Constructors:

    ::

        DomTextClass()
    """

    parent_class: DomCharacterDataClass = ...

class Evaluator(GObject.Object):
    """
    :Constructors:

    ::

        Evaluator(**properties)
        new(expression:str=None) -> Aravis.Evaluator

    Object ArvEvaluator

    Signals from GObject:
      notify (GParam)
    """
    def evaluate_as_double(self) -> float: ...
    def evaluate_as_int64(self) -> int: ...
    def get_constant(self, name: str) -> str: ...
    def get_expression(self) -> str: ...
    def get_sub_expression(self, name: str) -> str: ...
    @classmethod
    def new(cls, expression: str | None = None) -> Evaluator: ...
    def set_constant(self, name: str, constant: str | None = None) -> None: ...
    def set_double_variable(self, name: str, v_double: float) -> None: ...
    def set_expression(self, expression: str) -> None: ...
    def set_int64_variable(self, name: str, v_int64: int) -> None: ...
    def set_sub_expression(self, name: str, expression: str | None = None) -> None: ...

class EvaluatorClass(GObject.GPointer):
    """
    :Constructors:

    ::

        EvaluatorClass()
    """

    parent_class: GObject.ObjectClass = ...

class FakeCamera(GObject.Object):
    """
    :Constructors:

    ::

        FakeCamera(**properties)
        new(serial_number:str) -> Aravis.FakeCamera
        new_full(serial_number:str, genicam_filename:str) -> Aravis.FakeCamera

    Object ArvFakeCamera

    Signals from GObject:
      notify (GParam)
    """
    def check_and_acknowledge_software_trigger(self) -> bool: ...
    def fill_buffer(self, buffer: Buffer) -> int: ...
    def get_acquisition_status(self) -> int: ...
    def get_control_channel_privilege(self) -> int: ...
    def get_genicam_xml(self) -> typing.Tuple[str, int]: ...
    def get_genicam_xml_url(self) -> str: ...
    def get_heartbeat_timeout(self) -> int: ...
    def get_payload(self) -> int: ...
    def get_sleep_time_for_next_frame(self) -> typing.Tuple[int, int]: ...
    def get_stream_address(self) -> Gio.SocketAddress: ...
    def is_in_free_running_mode(self) -> bool: ...
    def is_in_software_trigger_mode(self) -> bool: ...
    @classmethod
    def new(cls, serial_number: str) -> FakeCamera: ...
    @classmethod
    def new_full(cls, serial_number: str, genicam_filename: str) -> FakeCamera: ...
    def read_memory(self, address: int, size: int, buffer: None) -> bool: ...
    def read_register(self, address: int) -> typing.Tuple[bool, int]: ...
    def set_control_channel_privilege(self, privilege: int) -> None: ...
    def set_fill_pattern(
        self,
        fill_pattern_callback: typing.Callable[..., None],
        *fill_pattern_data: typing.Any,
    ) -> None: ...
    def set_inet_address(self, address: Gio.InetAddress) -> None: ...
    def set_trigger_frequency(self, frequency: float) -> None: ...
    def wait_for_next_frame(self) -> None: ...
    def write_memory(self, address: int, size: int, buffer: None) -> bool: ...
    def write_register(self, address: int, value: int) -> bool: ...

class FakeCameraClass(GObject.GPointer):
    """
    :Constructors:

    ::

        FakeCameraClass()
    """

    parent_class: GObject.ObjectClass = ...

class FakeDevice(Device, Gio.Initable):
    """
    :Constructors:

    ::

        FakeDevice(**properties)
        new(serial_number:str) -> Aravis.Device

    Object ArvFakeDevice

    Properties from ArvFakeDevice:
      serial-number -> gchararray: Serial number
        Fake device serial number

    Signals from ArvDevice:
      control-lost ()

    Signals from GObject:
      notify (GParam)
    """
    class Props(Device.Props):
        serial_number: str

    props: Props = ...
    def __init__(self, *, serial_number: str = ...) -> None: ...
    def get_fake_camera(self) -> FakeCamera: ...
    @classmethod
    def new(cls, serial_number: str) -> FakeDevice: ...

class FakeDeviceClass(GObject.GPointer):
    """
    :Constructors:

    ::

        FakeDeviceClass()
    """

    parent_class: DeviceClass = ...

class FakeInterface(Interface):
    """
    :Constructors:

    ::

        FakeInterface(**properties)

    Object ArvFakeInterface

    Signals from GObject:
      notify (GParam)
    """
    @staticmethod
    def get_instance() -> Interface: ...

class FakeInterfaceClass(GObject.GPointer):
    """
    :Constructors:

    ::

        FakeInterfaceClass()
    """

    parent_class: InterfaceClass = ...

class FakeStream(Stream, Gio.Initable):
    """
    :Constructors:

    ::

        FakeStream(**properties)

    Object ArvFakeStream

    Signals from ArvStream:
      new-buffer ()

    Properties from ArvStream:
      emit-signals -> gboolean: Emit signals
        Emit signals
      device -> ArvDevice: Paret device
        A ArvDevice parent object
      callback -> gpointer: Stream callback
        Optional user callback
      callback-data -> gpointer: Stream callback data
        Optional user callback data
      destroy-notify -> gpointer: Destroy notify
        Optional destroy notify

    Signals from GObject:
      notify (GParam)
    """
    class Props(Stream.Props):
        callback: None
        callback_data: None
        destroy_notify: None
        device: Device
        emit_signals: bool

    props: Props = ...
    def __init__(
        self,
        *,
        callback: None = ...,
        callback_data: None = ...,
        destroy_notify: None = ...,
        device: Device = ...,
        emit_signals: bool = ...,
    ) -> None: ...

class FakeStreamClass(GObject.GPointer):
    """
    :Constructors:

    ::

        FakeStreamClass()
    """

    parent_class: StreamClass = ...

class Gc(DomDocument):
    """
    :Constructors:

    ::

        Gc(**properties)
        new(device:Aravis.Device, xml=None, size:int) -> Aravis.Gc
        p_value_indexed_node_new() -> Aravis.GcNode

    Object ArvGc

    Signals from GObject:
      notify (GParam)
    """
    def get_access_check_policy(self) -> AccessCheckPolicy: ...
    def get_buffer(self) -> Buffer: ...
    def get_device(self) -> Device: ...
    def get_node(self, name: str) -> GcNode: ...
    def get_range_check_policy(self) -> RangeCheckPolicy: ...
    def get_register_cache_policy(self) -> RegisterCachePolicy: ...
    @staticmethod
    def invalidator_has_changed(self: GcInvalidatorNode) -> bool: ...
    @classmethod
    def new(cls, device: Device, xml: None, size: int) -> Gc: ...
    @classmethod
    def p_value_indexed_node_new(cls) -> Gc: ...
    def register_feature_node(self, node: GcFeatureNode) -> None: ...
    def set_access_check_policy(self, policy: AccessCheckPolicy) -> None: ...
    def set_buffer(self, buffer: Buffer) -> None: ...
    def set_range_check_policy(self, policy: RangeCheckPolicy) -> None: ...
    def set_register_cache_policy(self, policy: RegisterCachePolicy) -> None: ...

class GcBoolean(GcFeatureNode):
    """
    :Constructors:

    ::

        GcBoolean(**properties)
        new() -> Aravis.GcNode

    Object ArvGcBoolean

    Signals from GObject:
      notify (GParam)
    """
    def get_value(self) -> bool: ...
    @classmethod
    def new(cls) -> GcBoolean: ...
    def set_value(self, v_boolean: bool) -> None: ...

class GcBooleanClass(GObject.GPointer):
    """
    :Constructors:

    ::

        GcBooleanClass()
    """

    parent_class: GcFeatureNodeClass = ...

class GcCategory(GcFeatureNode):
    """
    :Constructors:

    ::

        GcCategory(**properties)
        new() -> Aravis.GcNode

    Object ArvGcCategory

    Signals from GObject:
      notify (GParam)
    """
    def get_features(self) -> list[str]: ...
    @classmethod
    def new(cls) -> GcCategory: ...

class GcCategoryClass(GObject.GPointer):
    """
    :Constructors:

    ::

        GcCategoryClass()
    """

    parent_class: GcFeatureNodeClass = ...

class GcClass(GObject.GPointer):
    """
    :Constructors:

    ::

        GcClass()
    """

    parent_class: DomDocumentClass = ...

class GcCommand(GcFeatureNode):
    """
    :Constructors:

    ::

        GcCommand(**properties)
        new() -> Aravis.GcNode

    Object ArvGcCommand

    Signals from GObject:
      notify (GParam)
    """
    def execute(self) -> None: ...
    @classmethod
    def new(cls) -> GcCommand: ...

class GcCommandClass(GObject.GPointer):
    """
    :Constructors:

    ::

        GcCommandClass()
    """

    parent_class: GcFeatureNodeClass = ...

class GcConverter(GcFeatureNode):
    """
    :Constructors:

    ::

        GcConverter(**properties)

    Object ArvGcConverter

    Signals from GObject:
      notify (GParam)
    """

    parent_instance: GcFeatureNode = ...

class GcConverterClass(GObject.GPointer):
    """
    :Constructors:

    ::

        GcConverterClass()
    """

    parent_class: GcFeatureNodeClass = ...

class GcConverterNode(GcConverter, GcFloat):
    """
    :Constructors:

    ::

        GcConverterNode(**properties)
        new() -> Aravis.GcNode

    Object ArvGcConverterNode

    Signals from GObject:
      notify (GParam)
    """
    @classmethod
    def new(cls) -> GcConverterNode: ...

class GcConverterNodeClass(GObject.GPointer):
    """
    :Constructors:

    ::

        GcConverterNodeClass()
    """

    parent_class: GcConverterClass = ...

class GcEnumEntry(GcFeatureNode):
    """
    :Constructors:

    ::

        GcEnumEntry(**properties)
        new() -> Aravis.GcNode

    Object ArvGcEnumEntry

    Signals from GObject:
      notify (GParam)
    """
    def get_value(self) -> int: ...
    @classmethod
    def new(cls) -> GcEnumEntry: ...

class GcEnumEntryClass(GObject.GPointer):
    """
    :Constructors:

    ::

        GcEnumEntryClass()
    """

    parent_class: GcFeatureNodeClass = ...

class GcEnumeration(GcFeatureNode, GcInteger, GcSelector, GcString):
    """
    :Constructors:

    ::

        GcEnumeration(**properties)
        new() -> Aravis.GcNode

    Object ArvGcEnumeration

    Signals from GObject:
      notify (GParam)
    """
    def dup_available_display_names(self) -> list[str]: ...
    def dup_available_int_values(self) -> list[int]: ...
    def dup_available_string_values(self) -> list[str]: ...
    def get_entries(self) -> list[GcFeatureNode]: ...
    def get_int_value(self) -> int: ...
    def get_string_value(self) -> str: ...
    @classmethod
    def new(cls) -> GcEnumeration: ...
    def set_int_value(self, value: int) -> bool: ...
    def set_string_value(self, value: str) -> bool: ...

class GcEnumerationClass(GObject.GPointer):
    """
    :Constructors:

    ::

        GcEnumerationClass()
    """

    parent_class: GcFeatureNodeClass = ...

class GcFeatureNode(GcNode):
    """
    :Constructors:

    ::

        GcFeatureNode(**properties)

    Object ArvGcFeatureNode

    Signals from GObject:
      notify (GParam)
    """

    parent_instance: GcNode = ...
    def do_get_access_mode(self) -> GcAccessMode: ...
    def get_actual_access_mode(self) -> GcAccessMode: ...
    def get_description(self) -> str: ...
    def get_display_name(self) -> str: ...
    def get_imposed_access_mode(self) -> GcAccessMode: ...
    def get_name(self) -> str: ...
    def get_name_space(self) -> GcNameSpace: ...
    def get_tooltip(self) -> str: ...
    def get_value_as_string(self) -> str: ...
    def get_visibility(self) -> GcVisibility: ...
    def is_available(self) -> bool: ...
    def is_implemented(self) -> bool: ...
    def is_locked(self) -> bool: ...
    def set_value_from_string(self, string: str) -> None: ...

class GcFeatureNodeClass(GObject.GPointer):
    """
    :Constructors:

    ::

        GcFeatureNodeClass()
    """

    parent_class: GcNodeClass = ...
    get_linked_feature: None = ...
    get_access_mode: typing.Callable[[GcFeatureNode], GcAccessMode] = ...
    default_access_mode: GcAccessMode = ...

class GcFloat(GObject.GInterface):
    """
    Interface ArvGcFloat

    Signals from GObject:
      notify (GParam)
    """
    def get_display_notation(self) -> GcDisplayNotation: ...
    def get_display_precision(self) -> int: ...
    def get_inc(self) -> float: ...
    def get_max(self) -> float: ...
    def get_min(self) -> float: ...
    def get_representation(self) -> GcRepresentation: ...
    def get_unit(self) -> str: ...
    def get_value(self) -> float: ...
    def impose_max(self, maximum: float) -> None: ...
    def impose_min(self, minimum: float) -> None: ...
    def set_value(self, value: float) -> None: ...

class GcFloatInterface(GObject.GPointer):
    """
    :Constructors:

    ::

        GcFloatInterface()
    """

    parent: GObject.TypeInterface = ...
    get_value: typing.Callable[[GcFloat], float] = ...
    set_value: typing.Callable[[GcFloat, float], None] = ...
    get_min: typing.Callable[[GcFloat], float] = ...
    get_max: typing.Callable[[GcFloat], float] = ...
    get_inc: typing.Callable[[GcFloat], float] = ...
    get_representation: typing.Callable[[GcFloat], GcRepresentation] = ...
    get_display_notation: typing.Callable[[GcFloat], GcDisplayNotation] = ...
    get_display_precision: typing.Callable[[GcFloat], int] = ...
    get_unit: typing.Callable[[GcFloat], str] = ...
    impose_min: typing.Callable[[GcFloat, float], None] = ...
    impose_max: typing.Callable[[GcFloat, float], None] = ...

class GcFloatNode(GcFeatureNode, GcFloat):
    """
    :Constructors:

    ::

        GcFloatNode(**properties)
        new() -> Aravis.GcNode

    Object ArvGcFloatNode

    Signals from GObject:
      notify (GParam)
    """
    @classmethod
    def new(cls) -> GcFloatNode: ...

class GcFloatNodeClass(GObject.GPointer):
    """
    :Constructors:

    ::

        GcFloatNodeClass()
    """

    parent_class: GcFeatureNodeClass = ...

class GcFloatRegNode(GcRegisterNode, GcFloat, GcRegister):
    """
    :Constructors:

    ::

        GcFloatRegNode(**properties)
        new() -> Aravis.GcNode

    Object ArvGcFloatRegNode

    Signals from GObject:
      notify (GParam)
    """

    parent_instance: GcRegisterNode = ...
    @classmethod
    def new(cls) -> GcFloatRegNode: ...

class GcFloatRegNodeClass(GObject.GPointer):
    """
    :Constructors:

    ::

        GcFloatRegNodeClass()
    """

    parent_class: GcRegisterNodeClass = ...

class GcGroupNode(GcFeatureNode):
    """
    :Constructors:

    ::

        GcGroupNode(**properties)
        new() -> Aravis.GcNode

    Object ArvGcGroupNode

    Signals from GObject:
      notify (GParam)
    """
    @classmethod
    def new(cls) -> GcGroupNode: ...

class GcGroupNodeClass(GObject.GPointer):
    """
    :Constructors:

    ::

        GcGroupNodeClass()
    """

    parent_class: GcFeatureNodeClass = ...

class GcIndexNode(GcPropertyNode):
    """
    :Constructors:

    ::

        GcIndexNode(**properties)
        new() -> Aravis.GcNode

    Object ArvGcIndexNode

    Properties from ArvGcPropertyNode:
      node-type -> ArvGcPropertyNodeType: Node type
        Actual node type

    Signals from GObject:
      notify (GParam)
    """
    class Props(GcPropertyNode.Props):
        node_type: GcPropertyNodeType

    props: Props = ...
    def __init__(self, *, node_type: GcPropertyNodeType = ...) -> None: ...
    def get_index(self, default_offset: int) -> int: ...
    @classmethod
    def new(cls) -> GcIndexNode: ...

class GcIndexNodeClass(GObject.GPointer):
    """
    :Constructors:

    ::

        GcIndexNodeClass()
    """

    parent_class: GcPropertyNodeClass = ...

class GcIntConverterNode(GcConverter, GcInteger):
    """
    :Constructors:

    ::

        GcIntConverterNode(**properties)
        new() -> Aravis.GcNode

    Object ArvGcIntConverterNode

    Signals from GObject:
      notify (GParam)
    """
    @classmethod
    def new(cls) -> GcIntConverterNode: ...

class GcIntConverterNodeClass(GObject.GPointer):
    """
    :Constructors:

    ::

        GcIntConverterNodeClass()
    """

    parent_class: GcConverterClass = ...

class GcIntRegNode(GcRegisterNode, GcInteger, GcRegister, GcSelector):
    """
    :Constructors:

    ::

        GcIntRegNode(**properties)
        new() -> Aravis.GcNode

    Object ArvGcIntRegNode

    Signals from GObject:
      notify (GParam)
    """

    parent_instance: GcRegisterNode = ...
    @classmethod
    def new(cls) -> GcIntRegNode: ...

class GcIntRegNodeClass(GObject.GPointer):
    """
    :Constructors:

    ::

        GcIntRegNodeClass()
    """

    parent_class: GcRegisterNodeClass = ...

class GcIntSwissKnifeNode(GcSwissKnife, GcInteger):
    """
    :Constructors:

    ::

        GcIntSwissKnifeNode(**properties)
        new() -> Aravis.GcNode

    Object ArvGcIntSwissKnifeNode

    Signals from GObject:
      notify (GParam)
    """

    parent_instance: GcSwissKnife = ...
    @classmethod
    def new(cls) -> GcIntSwissKnifeNode: ...

class GcIntSwissKnifeNodeClass(GObject.GPointer):
    """
    :Constructors:

    ::

        GcIntSwissKnifeNodeClass()
    """

    parent_class: GcSwissKnifeClass = ...

class GcInteger(GObject.GInterface):
    """
    Interface ArvGcInteger

    Signals from GObject:
      notify (GParam)
    """
    def get_inc(self) -> int: ...
    def get_max(self) -> int: ...
    def get_min(self) -> int: ...
    def get_representation(self) -> GcRepresentation: ...
    def get_unit(self) -> str: ...
    def get_value(self) -> int: ...
    def impose_max(self, maximum: int) -> None: ...
    def impose_min(self, minimum: int) -> None: ...
    def set_value(self, value: int) -> None: ...

class GcIntegerInterface(GObject.GPointer):
    """
    :Constructors:

    ::

        GcIntegerInterface()
    """

    parent: GObject.TypeInterface = ...
    get_value: typing.Callable[[GcInteger], int] = ...
    set_value: typing.Callable[[GcInteger, int], None] = ...
    get_min: typing.Callable[[GcInteger], int] = ...
    get_max: typing.Callable[[GcInteger], int] = ...
    get_inc: typing.Callable[[GcInteger], int] = ...
    get_representation: typing.Callable[[GcInteger], GcRepresentation] = ...
    get_unit: typing.Callable[[GcInteger], str] = ...
    impose_min: typing.Callable[[GcInteger, int], None] = ...
    impose_max: typing.Callable[[GcInteger, int], None] = ...

class GcIntegerNode(GcFeatureNode, GcInteger, GcSelector):
    """
    :Constructors:

    ::

        GcIntegerNode(**properties)
        new() -> Aravis.GcNode

    Object ArvGcIntegerNode

    Signals from GObject:
      notify (GParam)
    """
    @classmethod
    def new(cls) -> GcIntegerNode: ...

class GcIntegerNodeClass(GObject.GPointer):
    """
    :Constructors:

    ::

        GcIntegerNodeClass()
    """

    parent_class: GcFeatureNodeClass = ...

class GcInvalidatorNode(GcPropertyNode):
    """
    :Constructors:

    ::

        GcInvalidatorNode(**properties)
        new() -> Aravis.GcNode

    Object ArvGcInvalidatorNode

    Properties from ArvGcPropertyNode:
      node-type -> ArvGcPropertyNodeType: Node type
        Actual node type

    Signals from GObject:
      notify (GParam)
    """
    class Props(GcPropertyNode.Props):
        node_type: GcPropertyNodeType

    props: Props = ...
    def __init__(self, *, node_type: GcPropertyNodeType = ...) -> None: ...
    @classmethod
    def new(cls) -> GcInvalidatorNode: ...

class GcInvalidatorNodeClass(GObject.GPointer):
    """
    :Constructors:

    ::

        GcInvalidatorNodeClass()
    """

    parent_class: GcPropertyNodeClass = ...

class GcMaskedIntRegNode(GcRegisterNode, GcInteger, GcRegister, GcSelector):
    """
    :Constructors:

    ::

        GcMaskedIntRegNode(**properties)
        new() -> Aravis.GcNode

    Object ArvGcMaskedIntRegNode

    Signals from GObject:
      notify (GParam)
    """

    parent_instance: GcRegisterNode = ...
    @classmethod
    def new(cls) -> GcMaskedIntRegNode: ...

class GcMaskedIntRegNodeClass(GObject.GPointer):
    """
    :Constructors:

    ::

        GcMaskedIntRegNodeClass()
    """

    parent_class: GcRegisterNodeClass = ...

class GcNode(DomElement):
    """
    :Constructors:

    ::

        GcNode(**properties)

    Object ArvGcNode

    Signals from GObject:
      notify (GParam)
    """

    parent_instance: DomElement = ...
    def get_genicam(self) -> Gc: ...

class GcNodeClass(GObject.GPointer):
    """
    :Constructors:

    ::

        GcNodeClass()
    """

    parent_class: DomElementClass = ...

class GcPort(GcFeatureNode):
    """
    :Constructors:

    ::

        GcPort(**properties)
        new() -> Aravis.GcNode

    Object ArvGcPort

    Signals from GObject:
      notify (GParam)
    """
    @classmethod
    def new(cls) -> GcPort: ...
    def read(self, buffer: None, address: int, length: int) -> None: ...
    def write(self, buffer: None, address: int, length: int) -> None: ...

class GcPortClass(GObject.GPointer):
    """
    :Constructors:

    ::

        GcPortClass()
    """

    parent_class: GcFeatureNodeClass = ...

class GcPropertyNode(GcNode):
    """
    :Constructors:

    ::

        GcPropertyNode(**properties)
        new_access_mode() -> Aravis.GcNode
        new_address() -> Aravis.GcNode
        new_bit() -> Aravis.GcNode
        new_cachable() -> Aravis.GcNode
        new_chunk_id() -> Aravis.GcNode
        new_command_value() -> Aravis.GcNode
        new_constant() -> Aravis.GcNode
        new_description() -> Aravis.GcNode
        new_display_name() -> Aravis.GcNode
        new_display_notation() -> Aravis.GcNode
        new_display_precision() -> Aravis.GcNode
        new_endianness() -> Aravis.GcNode
        new_event_id() -> Aravis.GcNode
        new_expression() -> Aravis.GcNode
        new_formula() -> Aravis.GcNode
        new_formula_from() -> Aravis.GcNode
        new_formula_to() -> Aravis.GcNode
        new_imposed_access_mode() -> Aravis.GcNode
        new_increment() -> Aravis.GcNode
        new_is_deprecated() -> Aravis.GcNode
        new_is_linear() -> Aravis.GcNode
        new_length() -> Aravis.GcNode
        new_lsb() -> Aravis.GcNode
        new_maximum() -> Aravis.GcNode
        new_minimum() -> Aravis.GcNode
        new_msb() -> Aravis.GcNode
        new_off_value() -> Aravis.GcNode
        new_on_value() -> Aravis.GcNode
        new_p_address() -> Aravis.GcNode
        new_p_alias() -> Aravis.GcNode
        new_p_cast_alias() -> Aravis.GcNode
        new_p_command_value() -> Aravis.GcNode
        new_p_feature() -> Aravis.GcNode
        new_p_increment() -> Aravis.GcNode
        new_p_is_available() -> Aravis.GcNode
        new_p_is_implemented() -> Aravis.GcNode
        new_p_is_locked() -> Aravis.GcNode
        new_p_length() -> Aravis.GcNode
        new_p_maximum() -> Aravis.GcNode
        new_p_minimum() -> Aravis.GcNode
        new_p_port() -> Aravis.GcNode
        new_p_selected() -> Aravis.GcNode
        new_p_value() -> Aravis.GcNode
        new_p_value_default() -> Aravis.GcNode
        new_p_variable() -> Aravis.GcNode
        new_polling_time() -> Aravis.GcNode
        new_representation() -> Aravis.GcNode
        new_sign() -> Aravis.GcNode
        new_slope() -> Aravis.GcNode
        new_streamable() -> Aravis.GcNode
        new_tooltip() -> Aravis.GcNode
        new_unit() -> Aravis.GcNode
        new_value() -> Aravis.GcNode
        new_value_default() -> Aravis.GcNode
        new_visibility() -> Aravis.GcNode

    Object ArvGcPropertyNode

    Properties from ArvGcPropertyNode:
      node-type -> ArvGcPropertyNodeType: Node type
        Actual node type

    Signals from GObject:
      notify (GParam)
    """
    class Props(GcNode.Props):
        node_type: GcPropertyNodeType

    props: Props = ...
    parent_instance: GcNode = ...
    def __init__(self, *, node_type: GcPropertyNodeType = ...) -> None: ...
    def get_access_mode(self, default_value: GcAccessMode) -> GcAccessMode: ...
    def get_cachable(self, default_value: GcCachable) -> GcCachable: ...
    def get_display_notation(
        self, default_value: GcDisplayNotation
    ) -> GcDisplayNotation: ...
    def get_display_precision(self, default_value: int) -> int: ...
    def get_double(self) -> float: ...
    def get_endianness(self, default_value: int) -> int: ...
    def get_int64(self) -> int: ...
    def get_linked_node(self) -> GcNode: ...
    def get_lsb(self, default_value: int) -> int: ...
    def get_msb(self, default_value: int) -> int: ...
    def get_name(self) -> str: ...
    def get_node_type(self) -> GcPropertyNodeType: ...
    def get_representation(
        self, default_value: GcRepresentation
    ) -> GcRepresentation: ...
    def get_sign(self, default_value: GcSignedness) -> GcSignedness: ...
    def get_streamable(self, default_value: GcStreamable) -> GcStreamable: ...
    def get_string(self) -> str: ...
    def get_visibility(self, default_value: GcVisibility) -> GcVisibility: ...
    @classmethod
    def new_access_mode(cls) -> GcPropertyNode: ...
    @classmethod
    def new_address(cls) -> GcPropertyNode: ...
    @classmethod
    def new_bit(cls) -> GcPropertyNode: ...
    @classmethod
    def new_cachable(cls) -> GcPropertyNode: ...
    @classmethod
    def new_chunk_id(cls) -> GcPropertyNode: ...
    @classmethod
    def new_command_value(cls) -> GcPropertyNode: ...
    @classmethod
    def new_constant(cls) -> GcPropertyNode: ...
    @classmethod
    def new_description(cls) -> GcPropertyNode: ...
    @classmethod
    def new_display_name(cls) -> GcPropertyNode: ...
    @classmethod
    def new_display_notation(cls) -> GcPropertyNode: ...
    @classmethod
    def new_display_precision(cls) -> GcPropertyNode: ...
    @classmethod
    def new_endianness(cls) -> GcPropertyNode: ...
    @classmethod
    def new_event_id(cls) -> GcPropertyNode: ...
    @classmethod
    def new_expression(cls) -> GcPropertyNode: ...
    @classmethod
    def new_formula(cls) -> GcPropertyNode: ...
    @classmethod
    def new_formula_from(cls) -> GcPropertyNode: ...
    @classmethod
    def new_formula_to(cls) -> GcPropertyNode: ...
    @classmethod
    def new_imposed_access_mode(cls) -> GcPropertyNode: ...
    @classmethod
    def new_increment(cls) -> GcPropertyNode: ...
    @classmethod
    def new_is_deprecated(cls) -> GcPropertyNode: ...
    @classmethod
    def new_is_linear(cls) -> GcPropertyNode: ...
    @classmethod
    def new_length(cls) -> GcPropertyNode: ...
    @classmethod
    def new_lsb(cls) -> GcPropertyNode: ...
    @classmethod
    def new_maximum(cls) -> GcPropertyNode: ...
    @classmethod
    def new_minimum(cls) -> GcPropertyNode: ...
    @classmethod
    def new_msb(cls) -> GcPropertyNode: ...
    @classmethod
    def new_off_value(cls) -> GcPropertyNode: ...
    @classmethod
    def new_on_value(cls) -> GcPropertyNode: ...
    @classmethod
    def new_p_address(cls) -> GcPropertyNode: ...
    @classmethod
    def new_p_alias(cls) -> GcPropertyNode: ...
    @classmethod
    def new_p_cast_alias(cls) -> GcPropertyNode: ...
    @classmethod
    def new_p_command_value(cls) -> GcPropertyNode: ...
    @classmethod
    def new_p_feature(cls) -> GcPropertyNode: ...
    @classmethod
    def new_p_increment(cls) -> GcPropertyNode: ...
    @classmethod
    def new_p_is_available(cls) -> GcPropertyNode: ...
    @classmethod
    def new_p_is_implemented(cls) -> GcPropertyNode: ...
    @classmethod
    def new_p_is_locked(cls) -> GcPropertyNode: ...
    @classmethod
    def new_p_length(cls) -> GcPropertyNode: ...
    @classmethod
    def new_p_maximum(cls) -> GcPropertyNode: ...
    @classmethod
    def new_p_minimum(cls) -> GcPropertyNode: ...
    @classmethod
    def new_p_port(cls) -> GcPropertyNode: ...
    @classmethod
    def new_p_selected(cls) -> GcPropertyNode: ...
    @classmethod
    def new_p_value(cls) -> GcPropertyNode: ...
    @classmethod
    def new_p_value_default(cls) -> GcPropertyNode: ...
    @classmethod
    def new_p_variable(cls) -> GcPropertyNode: ...
    @classmethod
    def new_polling_time(cls) -> GcPropertyNode: ...
    @classmethod
    def new_representation(cls) -> GcPropertyNode: ...
    @classmethod
    def new_sign(cls) -> GcPropertyNode: ...
    @classmethod
    def new_slope(cls) -> GcPropertyNode: ...
    @classmethod
    def new_streamable(cls) -> GcPropertyNode: ...
    @classmethod
    def new_tooltip(cls) -> GcPropertyNode: ...
    @classmethod
    def new_unit(cls) -> GcPropertyNode: ...
    @classmethod
    def new_value(cls) -> GcPropertyNode: ...
    @classmethod
    def new_value_default(cls) -> GcPropertyNode: ...
    @classmethod
    def new_visibility(cls) -> GcPropertyNode: ...
    def set_double(self, v_double: float) -> None: ...
    def set_int64(self, v_int64: int) -> None: ...
    def set_string(self, string: str) -> None: ...

class GcPropertyNodeClass(GObject.GPointer):
    """
    :Constructors:

    ::

        GcPropertyNodeClass()
    """

    parent_class: GcNodeClass = ...

class GcRegister(GObject.GInterface):
    """
    Interface ArvGcRegister

    Signals from GObject:
      notify (GParam)
    """
    def dup(self) -> int: ...
    def get(self, buffer: None, length: int) -> None: ...
    def get_address(self) -> int: ...
    def get_length(self) -> int: ...
    def set(self, buffer: None, length: int) -> None: ...

class GcRegisterDescriptionNode(GcFeatureNode):
    """
    :Constructors:

    ::

        GcRegisterDescriptionNode(**properties)
        new() -> Aravis.GcNode

    Object ArvGcRegisterDescriptionNode

    Signals from GObject:
      notify (GParam)
    """
    def check_schema_version(
        self, required_major: int, required_minor: int, required_subminor: int
    ) -> bool: ...
    def compare_schema_version(self, major: int, minor: int, subminor: int) -> int: ...
    def get_major_version(self) -> int: ...
    def get_minor_version(self) -> int: ...
    def get_model_name(self) -> str: ...
    def get_schema_major_version(self) -> int: ...
    def get_schema_minor_version(self) -> int: ...
    def get_schema_subminor_version(self) -> int: ...
    def get_subminor_version(self) -> int: ...
    def get_vendor_name(self) -> str: ...
    @classmethod
    def new(cls) -> GcRegisterDescriptionNode: ...

class GcRegisterDescriptionNodeClass(GObject.GPointer):
    """
    :Constructors:

    ::

        GcRegisterDescriptionNodeClass()
    """

    parent_class: GcFeatureNodeClass = ...

class GcRegisterInterface(GObject.GPointer):
    """
    :Constructors:

    ::

        GcRegisterInterface()
    """

    parent: GObject.TypeInterface = ...
    get: typing.Callable[[GcRegister, None, int], None] = ...
    set: typing.Callable[[GcRegister, None, int], None] = ...
    get_address: typing.Callable[[GcRegister], int] = ...
    get_length: typing.Callable[[GcRegister], int] = ...

class GcRegisterNode(GcFeatureNode, GcRegister):
    """
    :Constructors:

    ::

        GcRegisterNode(**properties)
        new() -> Aravis.GcNode

    Object ArvGcRegisterNode

    Signals from GObject:
      notify (GParam)
    """

    parent_instance: GcFeatureNode = ...
    @classmethod
    def new(cls) -> GcRegisterNode: ...

class GcRegisterNodeClass(GObject.GPointer):
    """
    :Constructors:

    ::

        GcRegisterNodeClass()
    """

    parent_class: GcFeatureNodeClass = ...
    default_cachable: GcCachable = ...

class GcSelector(GObject.GInterface):
    """
    Interface ArvGcSelector

    Signals from GObject:
      notify (GParam)
    """
    def get_selected_features(self) -> list[GcFeatureNode]: ...
    def is_selector(self) -> bool: ...

class GcSelectorInterface(GObject.GPointer):
    """
    :Constructors:

    ::

        GcSelectorInterface()
    """

    parent: GObject.TypeInterface = ...
    get_selected_features: typing.Callable[[GcSelector], list[GcFeatureNode]] = ...

class GcString(GObject.GInterface):
    """
    Interface ArvGcString

    Signals from GObject:
      notify (GParam)
    """
    def get_max_length(self) -> int: ...
    def get_value(self) -> str: ...
    def set_value(self, value: str) -> None: ...

class GcStringInterface(GObject.GPointer):
    """
    :Constructors:

    ::

        GcStringInterface()
    """

    parent: GObject.TypeInterface = ...
    get_value: typing.Callable[[GcString], str] = ...
    set_value: typing.Callable[[GcString, str], None] = ...
    get_max_length: typing.Callable[[GcString], int] = ...

class GcStringNode(GcFeatureNode, GcString):
    """
    :Constructors:

    ::

        GcStringNode(**properties)
        new() -> Aravis.GcNode

    Object ArvGcStringNode

    Signals from GObject:
      notify (GParam)
    """
    @classmethod
    def new(cls) -> GcStringNode: ...

class GcStringNodeClass(GObject.GPointer):
    """
    :Constructors:

    ::

        GcStringNodeClass()
    """

    parent_class: GcFeatureNodeClass = ...

class GcStringRegNode(GcRegisterNode, GcRegister, GcString):
    """
    :Constructors:

    ::

        GcStringRegNode(**properties)
        new() -> Aravis.GcNode

    Object ArvGcStringRegNode

    Signals from GObject:
      notify (GParam)
    """

    parent_instance: GcRegisterNode = ...
    @classmethod
    def new(cls) -> GcStringRegNode: ...

class GcStringRegNodeClass(GObject.GPointer):
    """
    :Constructors:

    ::

        GcStringRegNodeClass()
    """

    parent_class: GcRegisterNodeClass = ...

class GcStructEntryNode(GcFeatureNode, GcInteger, GcRegister):
    """
    :Constructors:

    ::

        GcStructEntryNode(**properties)
        new() -> Aravis.GcNode

    Object ArvGcStructEntryNode

    Signals from GObject:
      notify (GParam)
    """
    @classmethod
    def new(cls) -> GcStructEntryNode: ...

class GcStructEntryNodeClass(GObject.GPointer):
    """
    :Constructors:

    ::

        GcStructEntryNodeClass()
    """

    parent_class: GcFeatureNodeClass = ...

class GcStructRegNode(GcRegisterNode, GcRegister):
    """
    :Constructors:

    ::

        GcStructRegNode(**properties)
        new() -> Aravis.GcNode

    Object ArvGcStructRegNode

    Signals from GObject:
      notify (GParam)
    """

    parent_instance: GcRegisterNode = ...
    @classmethod
    def new(cls) -> GcStructRegNode: ...

class GcStructRegNodeClass(GObject.GPointer):
    """
    :Constructors:

    ::

        GcStructRegNodeClass()
    """

    parent_class: GcRegisterNodeClass = ...

class GcSwissKnife(GcFeatureNode):
    """
    :Constructors:

    ::

        GcSwissKnife(**properties)

    Object ArvGcSwissKnife

    Signals from GObject:
      notify (GParam)
    """

    parent_instance: GcFeatureNode = ...

class GcSwissKnifeClass(GObject.GPointer):
    """
    :Constructors:

    ::

        GcSwissKnifeClass()
    """

    parent_class: GcFeatureNodeClass = ...

class GcSwissKnifeNode(GcSwissKnife, GcFloat):
    """
    :Constructors:

    ::

        GcSwissKnifeNode(**properties)
        new() -> Aravis.GcNode

    Object ArvGcSwissKnifeNode

    Signals from GObject:
      notify (GParam)
    """

    parent_instance: GcSwissKnife = ...
    @classmethod
    def new(cls) -> GcSwissKnifeNode: ...

class GcSwissKnifeNodeClass(GObject.GPointer):
    """
    :Constructors:

    ::

        GcSwissKnifeNodeClass()
    """

    parent_class: GcSwissKnifeClass = ...

class GcValueIndexedNode(GcPropertyNode):
    """
    :Constructors:

    ::

        GcValueIndexedNode(**properties)
        new() -> Aravis.GcNode

    Object ArvGcValueIndexedNode

    Properties from ArvGcPropertyNode:
      node-type -> ArvGcPropertyNodeType: Node type
        Actual node type

    Signals from GObject:
      notify (GParam)
    """
    class Props(GcPropertyNode.Props):
        node_type: GcPropertyNodeType

    props: Props = ...
    def __init__(self, *, node_type: GcPropertyNodeType = ...) -> None: ...
    def get_index(self) -> int: ...
    @classmethod
    def new(cls) -> GcValueIndexedNode: ...

class GcValueIndexedNodeClass(GObject.GPointer):
    """
    :Constructors:

    ::

        GcValueIndexedNodeClass()
    """

    parent_class: GcPropertyNodeClass = ...

class GvDevice(Device, Gio.Initable):
    """
    :Constructors:

    ::

        GvDevice(**properties)
        new(interface_address:Gio.InetAddress, device_address:Gio.InetAddress) -> Aravis.Device

    Object ArvGvDevice

    Properties from ArvGvDevice:
      interface-address -> GInetAddress: Interface address
        The address of the interface connected to the device
      device-address -> GInetAddress: Device address
        The device address
      packet-size-adjustment -> ArvGvPacketSizeAdjustment: Packet size adjustment
        Packet size adjustment option

    Signals from ArvDevice:
      control-lost ()

    Signals from GObject:
      notify (GParam)
    """
    class Props(Device.Props):
        packet_size_adjustment: GvPacketSizeAdjustment
        device_address: Gio.InetAddress
        interface_address: Gio.InetAddress

    props: Props = ...
    def __init__(
        self,
        *,
        device_address: Gio.InetAddress = ...,
        interface_address: Gio.InetAddress = ...,
        packet_size_adjustment: GvPacketSizeAdjustment = ...,
    ) -> None: ...
    def auto_packet_size(self) -> int: ...
    def get_current_ip(
        self,
    ) -> typing.Tuple[bool, Gio.InetAddress, Gio.InetAddressMask, Gio.InetAddress]: ...
    def get_device_address(self) -> Gio.SocketAddress: ...
    def get_interface_address(self) -> Gio.SocketAddress: ...
    def get_ip_configuration_mode(self) -> GvIpConfigurationMode: ...
    def get_packet_size(self) -> int: ...
    def get_persistent_ip(
        self,
    ) -> typing.Tuple[bool, Gio.InetAddress, Gio.InetAddressMask, Gio.InetAddress]: ...
    def get_stream_options(self) -> GvStreamOption: ...
    def get_timestamp_tick_frequency(self) -> int: ...
    def is_controller(self) -> bool: ...
    def leave_control(self) -> bool: ...
    @classmethod
    def new(
        cls, interface_address: Gio.InetAddress, device_address: Gio.InetAddress
    ) -> GvDevice: ...
    def set_ip_configuration_mode(self, mode: GvIpConfigurationMode) -> bool: ...
    def set_packet_size(self, packet_size: int) -> None: ...
    def set_packet_size_adjustment(
        self, adjustment: GvPacketSizeAdjustment
    ) -> None: ...
    def set_persistent_ip(
        self,
        ip: Gio.InetAddress | None = None,
        mask: Gio.InetAddressMask | None = None,
        gateway: Gio.InetAddress | None = None,
    ) -> bool: ...
    def set_persistent_ip_from_string(
        self,
        ip: str | None = None,
        mask: str | None = None,
        gateway: str | None = None,
    ) -> bool: ...
    def set_stream_options(self, options: GvStreamOption) -> None: ...
    def take_control(self) -> bool: ...

class GvDeviceClass(GObject.GPointer):
    """
    :Constructors:

    ::

        GvDeviceClass()
    """

    parent_class: DeviceClass = ...

class GvFakeCamera(GObject.Object):
    """
    :Constructors:

    ::

        GvFakeCamera(**properties)
        new(interface_name:str=None, serial_number:str=None) -> Aravis.GvFakeCamera
        new_full(interface_name:str=None, serial_number:str=None, genicam_filename:str=None) -> Aravis.GvFakeCamera

    Object ArvGvFakeCamera

    Properties from ArvGvFakeCamera:
      interface-name -> gchararray: Interface name
        Interface name
      serial-number -> gchararray: Serial number
        Serial number
      genicam-filename -> gchararray: Genicam filename
        Genicam filename
      gvsp-lost-ratio -> gdouble: GVSP lost packet ratio
        GVSP lost packet ratio

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        genicam_filename: str
        gvsp_lost_ratio: float
        interface_name: str
        serial_number: str

    props: Props = ...
    def __init__(
        self,
        *,
        genicam_filename: str = ...,
        gvsp_lost_ratio: float = ...,
        interface_name: str = ...,
        serial_number: str = ...,
    ) -> None: ...
    def get_fake_camera(self) -> FakeCamera: ...
    def is_running(self) -> bool: ...
    @classmethod
    def new(
        cls,
        interface_name: str | None = None,
        serial_number: str | None = None,
    ) -> GvFakeCamera: ...
    @classmethod
    def new_full(
        cls,
        interface_name: str | None = None,
        serial_number: str | None = None,
        genicam_filename: str | None = None,
    ) -> GvFakeCamera: ...

class GvFakeCameraClass(GObject.GPointer):
    """
    :Constructors:

    ::

        GvFakeCameraClass()
    """

    parent_class: GObject.ObjectClass = ...

class GvInterface(Interface):
    """
    :Constructors:

    ::

        GvInterface(**properties)

    Object ArvGvInterface

    Signals from GObject:
      notify (GParam)
    """
    @staticmethod
    def dup_discovery_interface_name() -> str: ...
    @staticmethod
    def get_instance() -> Interface: ...
    @staticmethod
    def set_discovery_interface_name(discovery_interface: str) -> None: ...

class GvInterfaceClass(GObject.GPointer):
    """
    :Constructors:

    ::

        GvInterfaceClass()
    """

    parent_class: InterfaceClass = ...

class GvStream(Stream, Gio.Initable):
    """
    :Constructors:

    ::

        GvStream(**properties)

    Object ArvGvStream

    Properties from ArvGvStream:
      socket-buffer -> ArvGvStreamSocketBuffer: Socket buffer
        Socket buffer behaviour
      socket-buffer-size -> gint: Socket buffer size
        Socket buffer size, in bytes
      packet-resend -> ArvGvStreamPacketResend: Packet resend
        Packet resend behaviour
      packet-request-ratio -> gdouble: Packet request ratio
        Packet resend request limit as a percentage of frame packet number
      initial-packet-timeout -> guint: Initial packet timeout
        Initial packet timeout, in µs
      packet-timeout -> guint: Packet timeout
        Packet timeout, in µs
      frame-retention -> guint: Frame retention
        Packet retention, in µs

    Signals from ArvStream:
      new-buffer ()

    Properties from ArvStream:
      emit-signals -> gboolean: Emit signals
        Emit signals
      device -> ArvDevice: Paret device
        A ArvDevice parent object
      callback -> gpointer: Stream callback
        Optional user callback
      callback-data -> gpointer: Stream callback data
        Optional user callback data
      destroy-notify -> gpointer: Destroy notify
        Optional destroy notify

    Signals from GObject:
      notify (GParam)
    """
    class Props(Stream.Props):
        frame_retention: int
        initial_packet_timeout: int
        packet_request_ratio: float
        packet_resend: GvStreamPacketResend
        packet_timeout: int
        socket_buffer: GvStreamSocketBuffer
        socket_buffer_size: int
        callback: None
        callback_data: None
        destroy_notify: None
        device: Device
        emit_signals: bool

    props: Props = ...
    def __init__(
        self,
        *,
        frame_retention: int = ...,
        initial_packet_timeout: int = ...,
        packet_request_ratio: float = ...,
        packet_resend: GvStreamPacketResend = ...,
        packet_timeout: int = ...,
        socket_buffer: GvStreamSocketBuffer = ...,
        socket_buffer_size: int = ...,
        callback: None = ...,
        callback_data: None = ...,
        destroy_notify: None = ...,
        device: Device = ...,
        emit_signals: bool = ...,
    ) -> None: ...
    def get_port(self) -> int: ...
    def get_statistics(self) -> typing.Tuple[int, int]: ...

class GvStreamClass(GObject.GPointer):
    """
    :Constructors:

    ::

        GvStreamClass()
    """

    parent_class: StreamClass = ...

class Interface(GObject.Object):
    """
    :Constructors:

    ::

        Interface(**properties)

    Object ArvInterface

    Signals from GObject:
      notify (GParam)
    """

    parent_instance: GObject.Object = ...
    def do_open_device(self, device_id: str | None = None) -> Device: ...
    def get_device_address(self, index: int) -> str: ...
    def get_device_id(self, index: int) -> str: ...
    def get_device_manufacturer_info(self, index: int) -> str: ...
    def get_device_model(self, index: int) -> str: ...
    def get_device_physical_id(self, index: int) -> str: ...
    def get_device_protocol(self, index: int) -> str: ...
    def get_device_serial_nbr(self, index: int) -> str: ...
    def get_device_vendor(self, index: int) -> str: ...
    def get_n_devices(self) -> int: ...
    def open_device(self, device_id: str | None = None) -> Device: ...
    def update_device_list(self) -> None: ...

class InterfaceClass(GObject.GPointer):
    """
    :Constructors:

    ::

        InterfaceClass()
    """

    parent_class: GObject.ObjectClass = ...
    update_device_list: None = ...
    open_device: typing.Callable[[Interface, str | None], Device] = ...
    protocol: str = ...

class Stream(GObject.Object, Gio.Initable):
    """
    :Constructors:

    ::

        Stream(**properties)

    Object ArvStream

    Signals from ArvStream:
      new-buffer ()

    Properties from ArvStream:
      emit-signals -> gboolean: Emit signals
        Emit signals
      device -> ArvDevice: Paret device
        A ArvDevice parent object
      callback -> gpointer: Stream callback
        Optional user callback
      callback-data -> gpointer: Stream callback data
        Optional user callback data
      destroy-notify -> gpointer: Destroy notify
        Optional destroy notify

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        callback: None
        callback_data: None
        destroy_notify: None
        device: Device
        emit_signals: bool

    props: Props = ...
    parent_instance: GObject.Object = ...
    def __init__(
        self,
        *,
        callback: None = ...,
        callback_data: None = ...,
        destroy_notify: None = ...,
        device: Device = ...,
        emit_signals: bool = ...,
    ) -> None: ...
    def do_new_buffer(self) -> None: ...
    def do_start_thread(self) -> None: ...
    def do_stop_thread(self) -> None: ...
    def get_emit_signals(self) -> bool: ...
    def get_info_double(self, id: int) -> float: ...
    def get_info_double_by_name(self, name: str) -> float: ...
    def get_info_name(self, id: int) -> str: ...
    def get_info_type(self, id: int) -> typing.Type[typing.Any]: ...
    def get_info_uint64(self, id: int) -> int: ...
    def get_info_uint64_by_name(self, name: str) -> int: ...
    def get_n_buffers(self) -> typing.Tuple[int, int]: ...
    def get_n_infos(self) -> int: ...
    def get_statistics(self) -> typing.Tuple[int, int, int]: ...
    def pop_buffer(self) -> Buffer: ...
    def push_buffer(self, buffer: Buffer) -> None: ...
    def set_emit_signals(self, emit_signals: bool) -> None: ...
    def start_thread(self) -> None: ...
    def stop_thread(self, delete_buffers: bool) -> int: ...
    def timeout_pop_buffer(self, timeout: int) -> Buffer: ...
    def try_pop_buffer(self) -> Buffer: ...

class StreamClass(GObject.GPointer):
    """
    :Constructors:

    ::

        StreamClass()
    """

    parent_class: GObject.ObjectClass = ...
    start_thread: typing.Callable[[Stream], None] = ...
    stop_thread: typing.Callable[[Stream], None] = ...
    new_buffer: typing.Callable[[Stream], None] = ...

class UvDevice(Device, Gio.Initable):
    """
    :Constructors:

    ::

        UvDevice(**properties)
        new(vendor:str, product:str, serial_number:str) -> Aravis.Device
        new_from_guid(guid:str) -> Aravis.Device

    Object ArvUvDevice

    Properties from ArvUvDevice:
      vendor -> gchararray: Vendor
        USB3 device vendor string
      product -> gchararray: Product
        USB3 device product string
      serial-number -> gchararray: Serial number
        USB3 device serial number
      guid -> gchararray: GUID
        USB3 device GUID

    Signals from ArvDevice:
      control-lost ()

    Signals from GObject:
      notify (GParam)
    """
    class Props(Device.Props):
        guid: str
        product: str
        serial_number: str
        vendor: str

    props: Props = ...
    def __init__(
        self,
        *,
        guid: str = ...,
        product: str = ...,
        serial_number: str = ...,
        vendor: str = ...,
    ) -> None: ...
    @classmethod
    def new(cls, vendor: str, product: str, serial_number: str) -> UvDevice: ...
    @classmethod
    def new_from_guid(cls, guid: str) -> UvDevice: ...
    def set_usb_mode(self, usb_mode: UvUsbMode) -> None: ...

class UvDeviceClass(GObject.GPointer):
    """
    :Constructors:

    ::

        UvDeviceClass()
    """

    parent_class: DeviceClass = ...

class UvInterface(Interface):
    """
    :Constructors:

    ::

        UvInterface(**properties)

    Object ArvUvInterface

    Signals from GObject:
      notify (GParam)
    """
    @staticmethod
    def get_instance() -> Interface: ...

class UvInterfaceClass(GObject.GPointer):
    """
    :Constructors:

    ::

        UvInterfaceClass()
    """

    parent_class: InterfaceClass = ...

class UvStream(Stream, Gio.Initable):
    """
    :Constructors:

    ::

        UvStream(**properties)

    Object ArvUvStream

    Properties from ArvUvStream:
      usb-mode -> ArvUvUsbMode: USB mode
        USB device I/O mode

    Signals from ArvStream:
      new-buffer ()

    Properties from ArvStream:
      emit-signals -> gboolean: Emit signals
        Emit signals
      device -> ArvDevice: Paret device
        A ArvDevice parent object
      callback -> gpointer: Stream callback
        Optional user callback
      callback-data -> gpointer: Stream callback data
        Optional user callback data
      destroy-notify -> gpointer: Destroy notify
        Optional destroy notify

    Signals from GObject:
      notify (GParam)
    """
    class Props(Stream.Props):
        callback: None
        callback_data: None
        destroy_notify: None
        device: Device
        emit_signals: bool
        usb_mode: UvUsbMode

    props: Props = ...
    def __init__(
        self,
        *,
        usb_mode: UvUsbMode = ...,
        callback: None = ...,
        callback_data: None = ...,
        destroy_notify: None = ...,
        device: Device = ...,
        emit_signals: bool = ...,
    ) -> None: ...

class UvStreamClass(GObject.GPointer):
    """
    :Constructors:

    ::

        UvStreamClass()
    """

    parent_class: StreamClass = ...

class XmlSchema(GObject.Object):
    """
    :Constructors:

    ::

        XmlSchema(**properties)
        new_from_file(file:Gio.File) -> Aravis.XmlSchema
        new_from_memory(buffer:str, size:int) -> Aravis.XmlSchema
        new_from_path(path:str) -> Aravis.XmlSchema

    Object ArvXmlSchema

    Signals from GObject:
      notify (GParam)
    """
    @classmethod
    def new_from_file(cls, file: Gio.File) -> XmlSchema: ...
    @classmethod
    def new_from_memory(cls, buffer: str, size: int) -> XmlSchema: ...
    @classmethod
    def new_from_path(cls, path: str) -> XmlSchema: ...
    def validate(self, xml: None, size: int, line: int, column: int) -> bool: ...

class XmlSchemaClass(GObject.GPointer):
    """
    :Constructors:

    ::

        XmlSchemaClass()
    """

    parent_class: GObject.ObjectClass = ...

class Zip(GObject.GPointer): ...
class ZipFile(GObject.GPointer): ...

class GvInterfaceFlags(GObject.GFlags):
    ACK = 1

class GvStreamOption(GObject.GFlags):
    NONE = 0
    PACKET_SOCKET_DISABLED = 1

class AccessCheckPolicy(GObject.GEnum):
    DEFAULT = 0
    DISABLE = 0
    ENABLE = 1

class AcquisitionMode(GObject.GEnum):
    CONTINUOUS = 0
    MULTI_FRAME = 2
    SINGLE_FRAME = 1
    @staticmethod
    def from_string(string: str) -> AcquisitionMode: ...
    @staticmethod
    def to_string(value: AcquisitionMode) -> str: ...

class Auto(GObject.GEnum):
    CONTINUOUS = 2
    OFF = 0
    ONCE = 1
    @staticmethod
    def from_string(string: str) -> Auto: ...
    @staticmethod
    def to_string(value: Auto) -> str: ...

class BufferPartDataType(GObject.GEnum):
    CHUNK_DATA = 10
    CONFIDENCE_MAP = 9
    DEVICE_SPECIFIC = 32768
    JPEG = 11
    JPEG2000 = 12
    UNKNOWN = -1

class BufferPayloadType(GObject.GEnum):
    CHUNK_DATA = 4
    EXTENDED_CHUNK_DATA = 5
    FILE = 3
    GENDC_COMPONENT_DATA = 12
    GENDC_CONTAINER = 11
    H264 = 8
    IMAGE = 1
    JPEG = 6
    JPEG2000 = 7
    MULTIPART = 10
    MULTIZONE_IMAGE = 9
    NO_DATA = 0
    RAWDATA = 2
    UNKNOWN = -1

class BufferStatus(GObject.GEnum):
    ABORTED = 7
    CLEARED = 1
    FILLING = 6
    MISSING_PACKETS = 3
    PAYLOAD_NOT_SUPPORTED = 8
    SIZE_MISMATCH = 5
    SUCCESS = 0
    TIMEOUT = 2
    UNKNOWN = -1
    WRONG_PACKET_ID = 4

class ChunkParserError(GObject.GEnum):
    BUFFER_NOT_FOUND = 1
    CHUNK_NOT_FOUND = 2
    INVALID_FEATURE_TYPE = 0
    @staticmethod
    def quark() -> int: ...

class ComponentSelectionFlags(GObject.GEnum):
    DISABLE = 2
    ENABLE = 1
    ENABLE_ALL = 4
    EXCLUSIVE_ENABLE = 3
    NONE = 0

class DeviceError(GObject.GEnum):
    FEATURE_NOT_FOUND = 1
    GENICAM_NOT_FOUND = 8
    INVALID_PARAMETER = 7
    NOT_CONNECTED = 2
    NOT_CONTROLLER = 10
    NOT_FOUND = 6
    NO_STREAM_CHANNEL = 9
    PROTOCOL_ERROR = 3
    PROTOCOL_ERROR_ACCESS_DENIED = 17
    PROTOCOL_ERROR_BAD_ALIGNMENT = 16
    PROTOCOL_ERROR_BUSY = 18
    PROTOCOL_ERROR_INVALID_ADDRESS = 14
    PROTOCOL_ERROR_INVALID_PARAMETER = 13
    PROTOCOL_ERROR_NOT_IMPLEMENTED = 12
    PROTOCOL_ERROR_WRITE_PROTECT = 15
    TIMEOUT = 5
    TRANSFER_ERROR = 4
    UNKNOWN = 11
    WRONG_FEATURE = 0
    @staticmethod
    def quark() -> int: ...

class DomNodeType(GObject.GEnum):
    ATTRIBUTE_NODE = 2
    CDATA_SECTION_NODE = 4
    COMMENT_NODE = 8
    DOCUMENT_FRAGMENT_NODE = 11
    DOCUMENT_NODE = 9
    DOCUMENT_TYPE_NODE = 10
    ELEMENT_NODE = 1
    ENTITY_NODE = 6
    ENTITY_REFERENCE_NODE = 5
    NOTATION_NODE = 12
    PROCESSING_INSTRUCTION_NODE = 7
    TEXT_NODE = 3

class ExposureMode(GObject.GEnum):
    OFF = 0
    TIMED = 1
    TRIGGER_CONTROLLED = 3
    TRIGGER_WIDTH = 2
    @staticmethod
    def from_string(string: str) -> ExposureMode: ...
    @staticmethod
    def to_string(value: ExposureMode) -> str: ...

class GcAccessMode(GObject.GEnum):
    RO = 0
    RW = 2
    UNDEFINED = -1
    WO = 1
    @staticmethod
    def from_string(string: str) -> GcAccessMode: ...
    @staticmethod
    def to_string(value: GcAccessMode) -> str: ...

class GcCachable(GObject.GEnum):
    NO_CACHE = 0
    UNDEFINED = -1
    WRITE_AROUND = 2
    WRITE_THROUGH = 1

class GcDisplayNotation(GObject.GEnum):
    AUTOMATIC = 0
    FIXED = 1
    SCIENTIFIC = 2
    UNDEFINED = -1

class GcError(GObject.GEnum):
    EMPTY_ENUMERATION = 3
    ENUM_ENTRY_NOT_FOUND = 8
    GET_AS_STRING_UNDEFINED = 12
    INVALID_BIT_RANGE = 13
    INVALID_LENGTH = 9
    INVALID_PVALUE = 2
    INVALID_SYNTAX = 14
    NODE_NOT_FOUND = 7
    NO_DEVICE_SET = 5
    NO_EVENT_IMPLEMENTATION = 6
    OUT_OF_RANGE = 4
    PROPERTY_NOT_DEFINED = 0
    PVALUE_NOT_DEFINED = 1
    READ_ONLY = 10
    SET_FROM_STRING_UNDEFINED = 11
    @staticmethod
    def quark() -> int: ...

class GcIsLinear(GObject.GEnum):
    NO = 0
    UNDEFINED = -1
    YES = 1

class GcNameSpace(GObject.GEnum):
    CUSTOM = 1
    STANDARD = 0
    UNDEFINED = -1

class GcPropertyNodeType(GObject.GEnum):
    ACCESS_MODE = 24
    ADDRESS = 2
    BIT = 32
    CACHABLE = 26
    CHUNK_ID = 34
    COMMAND_VALUE = 33
    CONSTANT = 23
    DESCRIPTION = 3
    DISPLAY_NAME = 6
    DISPLAY_NOTATION = 13
    DISPLAY_PRECISION = 14
    ENDIANNESS = 28
    EVENT_ID = 35
    EXPRESSION = 22
    FORMULA = 19
    FORMULA_FROM = 21
    FORMULA_TO = 20
    IMPOSED_ACCESS_MODE = 25
    INCREMENT = 10
    IS_DEPRECATED = 39
    IS_LINEAR = 11
    LENGTH = 18
    LSB = 30
    MAXIMUM = 8
    MINIMUM = 7
    MSB = 31
    OFF_VALUE = 17
    ON_VALUE = 16
    POLLING_TIME = 27
    P_ADDRESS = 1003
    P_ALIAS = 1019
    P_CAST_ALIAS = 1020
    P_COMMAND_VALUE = 1016
    P_FEATURE = 1001
    P_INCREMENT = 1010
    P_INDEX = 1011
    P_INVALIDATOR = 1015
    P_IS_AVAILABLE = 1006
    P_IS_IMPLEMENTED = 1004
    P_IS_LOCKED = 1005
    P_LENGTH = 1012
    P_MAXIMUM = 1009
    P_MINIMUM = 1008
    P_PORT = 1013
    P_SELECTED = 1007
    P_UNKNONW = 1000
    P_VALUE = 1002
    P_VALUE_DEFAULT = 1018
    P_VALUE_INDEXED = 1017
    P_VARIABLE = 1014
    REPRESENTATION = 12
    SIGN = 29
    SLOPE = 9
    STREAMABLE = 38
    TOOLTIP = 5
    UNIT = 15
    UNKNOWN = 0
    VALUE = 1
    VALUE_DEFAULT = 37
    VALUE_INDEXED = 36
    VISIBILITY = 4

class GcRepresentation(GObject.GEnum):
    BOOLEAN = 2
    HEX_NUMBER = 4
    IPV4_ADDRESS = 5
    LINEAR = 0
    LOGARITHMIC = 1
    MAC_ADDRESS = 6
    PURE_NUMBER = 3
    UNDEFINED = -1

class GcSignedness(GObject.GEnum):
    SIGNED = 0
    UNDEFINED = -1
    UNSIGNED = 1

class GcStreamable(GObject.GEnum):
    NO = 0
    UNDEFINED = -1
    YES = 1

class GcVisibility(GObject.GEnum):
    BEGINNER = 3
    EXPERT = 2
    GURU = 1
    INVISIBLE = 0
    UNDEFINED = -1

class GvIpConfigurationMode(GObject.GEnum):
    DHCP = 2
    FORCE_IP = 4
    LLA = 3
    NONE = 0
    PERSISTENT_IP = 1

class GvPacketSizeAdjustment(GObject.GEnum):
    ALWAYS = 4
    DEFAULT = 1
    NEVER = 0
    ONCE = 3
    ON_FAILURE = 2
    ON_FAILURE_ONCE = 1

class GvStreamPacketResend(GObject.GEnum):
    ALWAYS = 1
    NEVER = 0

class GvStreamSocketBuffer(GObject.GEnum):
    AUTO = 1
    FIXED = 0

class RangeCheckPolicy(GObject.GEnum):
    DEBUG = 2
    DEFAULT = 0
    DISABLE = 0
    ENABLE = 1

class RegisterCachePolicy(GObject.GEnum):
    DEBUG = 2
    DEFAULT = 0
    DISABLE = 0
    ENABLE = 1

class StreamCallbackType(GObject.GEnum):
    BUFFER_DONE = 3
    EXIT = 1
    INIT = 0
    START_BUFFER = 2

class UvUsbMode(GObject.GEnum):
    ASYNC = 1
    DEFAULT = 1
    SYNC = 0

class XmlSchemaError(GObject.GEnum):
    STRUCTURE = 0
    @staticmethod
    def quark() -> int: ...
