DOMAIN = "get_euda_data"
DATA_KEY = DOMAIN

# Configuration definitions
DEFAULT_DEBUG = False
CONF_BRAND = "brand"
CONF_VEHICLE = "vehicle"
CONF_INSTRUMENTS = "instruments"
CONF_DEBUG = "debug"
CONF_LOGPREFIX = "log_prefix"

# Service definitions

UPDATE_CALLBACK = "update_callback"
DATA = "data"
UNDO_UPDATE_LISTENER = "undo_update_listener"

SIGNAL_STATE_UPDATED = f"{DOMAIN}.updated"

MIN_SCAN_INTERVAL = 120
DEFAULT_SCAN_INTERVAL = 600

PLATFORMS = {
    "sensor": "sensor",
    "binary_sensor": "binary_sensor",
    #"lock": "lock",
    #"device_tracker": "device_tracker",
    #"switch": "switch",
    #"button": "button",
    #"climate": "climate",
    #"number": "number",
}
