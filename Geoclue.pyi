from __future__ import annotations

_namespace: str = ...
_version: str = ...

def client_interface_info(*args, **kwargs): ...
def client_override_properties(*args, **kwargs): ...
def location_interface_info(*args, **kwargs): ...
def location_override_properties(*args, **kwargs): ...
def manager_interface_info(*args, **kwargs): ...
def manager_override_properties(*args, **kwargs): ...

class Client:
    def call_start(*args, **kwargs): ...
    def call_start_finish(*args, **kwargs): ...
    def call_start_sync(*args, **kwargs): ...
    def call_stop(*args, **kwargs): ...
    def call_stop_finish(*args, **kwargs): ...
    def call_stop_sync(*args, **kwargs): ...
    def complete_start(*args, **kwargs): ...
    def complete_stop(*args, **kwargs): ...
    def emit_location_updated(*args, **kwargs): ...
    def interface_info(*args, **kwargs): ...
    def override_properties(*args, **kwargs): ...

class ClientProxy:
    def create(*args, **kwargs): ...
    def create_finish(*args, **kwargs): ...
    def create_full(*args, **kwargs): ...
    def create_full_finish(*args, **kwargs): ...
    def create_full_sync(*args, **kwargs): ...
    def create_sync(*args, **kwargs): ...

class ClientSkeleton:
    def new(*args, **kwargs): ...

class Location:
    def interface_info(*args, **kwargs): ...
    def override_properties(*args, **kwargs): ...

class LocationProxy: ...

class LocationSkeleton:
    def new(*args, **kwargs): ...

class Manager:
    def call_add_agent(*args, **kwargs): ...
    def call_add_agent_finish(*args, **kwargs): ...
    def call_add_agent_sync(*args, **kwargs): ...
    def call_create_client(*args, **kwargs): ...
    def call_create_client_finish(*args, **kwargs): ...
    def call_create_client_sync(*args, **kwargs): ...
    def call_delete_client(*args, **kwargs): ...
    def call_delete_client_finish(*args, **kwargs): ...
    def call_delete_client_sync(*args, **kwargs): ...
    def call_get_client(*args, **kwargs): ...
    def call_get_client_finish(*args, **kwargs): ...
    def call_get_client_sync(*args, **kwargs): ...
    def complete_add_agent(*args, **kwargs): ...
    def complete_create_client(*args, **kwargs): ...
    def complete_delete_client(*args, **kwargs): ...
    def complete_get_client(*args, **kwargs): ...
    def interface_info(*args, **kwargs): ...
    def override_properties(*args, **kwargs): ...

class ManagerProxy: ...

class ManagerSkeleton:
    def new(*args, **kwargs): ...

class Simple:
    parent = ...
    priv = ...

    def get_client(*args, **kwargs): ...
    def get_location(*args, **kwargs): ...
    def new(*args, **kwargs): ...
    def new_sync(*args, **kwargs): ...
    def new_with_thresholds(*args, **kwargs): ...
    def new_with_thresholds_finish(*args, **kwargs): ...
    def new_with_thresholds_sync(*args, **kwargs): ...

class ClientProxyCreateFlags(GObject.GFlags):
    AUTO_DELETE = ...
    NONE = ...

class AccuracyLevel(GObject.GEnum):
    CITY = ...
    COUNTRY = ...
    EXACT = ...
    NEIGHBORHOOD = ...
    NONE = ...
    STREET = ...
