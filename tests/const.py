""" The commons const for all tests """

from homeassistant.components.climate.const import (  # pylint: disable=unused-import
    PRESET_BOOST,
    PRESET_COMFORT,
    PRESET_ECO,
    PRESET_NONE,
    PRESET_ACTIVITY,
)

from custom_components.versatile_thermostat.const import *  # pylint: disable=wildcard-import, unused-wildcard-import

MOCK_TH_OVER_SWITCH_USER_CONFIG = {
    CONF_THERMOSTAT_TYPE: CONF_THERMOSTAT_SWITCH,
}

MOCK_TH_OVER_SWITCH_MAIN_CONFIG = {
    CONF_NAME: "TheOverSwitchMockName",
    CONF_TEMP_SENSOR: "sensor.mock_temp_sensor",
    CONF_CYCLE_MIN: 5,
    CONF_DEVICE_POWER: 1,
    # CONF_USE_WINDOW_FEATURE: True,
    # CONF_USE_MOTION_FEATURE: True,
    # CONF_USE_POWER_FEATURE: True,
    # CONF_USE_PRESENCE_FEATURE: True,
    CONF_USE_MAIN_CENTRAL_CONFIG: True,
}

MOCK_TH_OVER_4SWITCH_USER_CONFIG = {
    CONF_NAME: "TheOver4SwitchMockName",
    CONF_THERMOSTAT_TYPE: CONF_THERMOSTAT_SWITCH,
    CONF_TEMP_SENSOR: "sensor.mock_temp_sensor",
    CONF_EXTERNAL_TEMP_SENSOR: "sensor.mock_ext_temp_sensor",
    CONF_CYCLE_MIN: 8,
    CONF_TEMP_MIN: 15,
    CONF_TEMP_MAX: 30,
    CONF_STEP_TEMPERATURE: 0.1,
    CONF_DEVICE_POWER: 1,
    CONF_USE_WINDOW_FEATURE: True,
    CONF_USE_MOTION_FEATURE: True,
    CONF_USE_POWER_FEATURE: True,
    CONF_USE_PRESENCE_FEATURE: True,
}

MOCK_TH_OVER_CLIMATE_USER_CONFIG = {
    CONF_THERMOSTAT_TYPE: CONF_THERMOSTAT_CLIMATE,
}


MOCK_TH_OVER_CLIMATE_MAIN_CONFIG = {
    CONF_NAME: "TheOverClimateMockName",
    CONF_TEMP_SENSOR: "sensor.mock_temp_sensor",
    CONF_CYCLE_MIN: 5,
    CONF_DEVICE_POWER: 1,
    CONF_USE_MAIN_CENTRAL_CONFIG: False,
    CONF_USE_CENTRAL_MODE: True,
    # Keep default values which are False
}

MOCK_TH_OVER_CLIMATE_CENTRAL_MAIN_CONFIG = {
    CONF_EXTERNAL_TEMP_SENSOR: "sensor.mock_ext_temp_sensor",
    CONF_TEMP_MIN: 15,
    CONF_TEMP_MAX: 30,
    CONF_STEP_TEMPERATURE: 0.1,
    # Keep default values which are False
}

MOCK_TH_OVER_SWITCH_CENTRAL_MAIN_CONFIG = {
    CONF_EXTERNAL_TEMP_SENSOR: "sensor.mock_ext_temp_sensor",
    CONF_TEMP_MIN: 15,
    CONF_TEMP_MAX: 30,
    CONF_STEP_TEMPERATURE: 0.1,
    # Keep default values which are False
}

MOCK_TH_OVER_SWITCH_TYPE_CONFIG = {
    CONF_UNDERLYING_LIST: ["switch.mock_switch"],
    CONF_HEATER_KEEP_ALIVE: 0,
    CONF_PROP_FUNCTION: PROPORTIONAL_FUNCTION_TPI,
    CONF_AC_MODE: False,
    CONF_INVERSE_SWITCH: False,
}

MOCK_TH_OVER_SWITCH_AC_TYPE_CONFIG = {
    CONF_UNDERLYING_LIST: ["switch.mock_air_conditioner"],
    CONF_PROP_FUNCTION: PROPORTIONAL_FUNCTION_TPI,
    CONF_AC_MODE: True,
    CONF_INVERSE_SWITCH: False,
}

MOCK_TH_OVER_4SWITCH_TYPE_CONFIG = {
    CONF_UNDERLYING_LIST: [
        "switch.mock_4switch0",
        "switch.mock_4switch1",
        "switch.mock_4switch2",
        "switch.mock_4switch3",
    ],
    CONF_HEATER_KEEP_ALIVE: 0,
    CONF_PROP_FUNCTION: PROPORTIONAL_FUNCTION_TPI,
    CONF_AC_MODE: False,
    CONF_INVERSE_SWITCH: False,
}

MOCK_TH_OVER_SWITCH_TPI_CONFIG = {
    CONF_TPI_COEF_INT: 0.3,
    CONF_TPI_COEF_EXT: 0.1,
}

MOCK_TH_OVER_CLIMATE_TYPE_CONFIG = {
    CONF_UNDERLYING_LIST: ["climate.mock_climate"],
    CONF_AC_MODE: False,
    CONF_AUTO_REGULATION_MODE: CONF_AUTO_REGULATION_STRONG,
    CONF_AUTO_REGULATION_DTEMP: 0.5,
    CONF_AUTO_REGULATION_PERIOD_MIN: 2,
    CONF_AUTO_FAN_MODE: CONF_AUTO_FAN_HIGH,
    CONF_AUTO_REGULATION_USE_DEVICE_TEMP: False,
}

MOCK_TH_OVER_CLIMATE_TYPE_USE_DEVICE_TEMP_CONFIG = {
    CONF_UNDERLYING_LIST: ["climate.mock_climate"],
    CONF_AC_MODE: False,
    CONF_AUTO_REGULATION_MODE: CONF_AUTO_REGULATION_STRONG,
    CONF_AUTO_REGULATION_DTEMP: 0.1,
    CONF_AUTO_REGULATION_PERIOD_MIN: 2,
    CONF_AUTO_FAN_MODE: CONF_AUTO_FAN_HIGH,
    CONF_AUTO_REGULATION_USE_DEVICE_TEMP: True,
}

MOCK_TH_OVER_CLIMATE_TYPE_NOT_REGULATED_CONFIG = {
    CONF_UNDERLYING_LIST: ["climate.mock_climate"],
    CONF_AC_MODE: False,
    CONF_AUTO_REGULATION_MODE: CONF_AUTO_REGULATION_NONE,
}

MOCK_TH_OVER_CLIMATE_TYPE_AC_CONFIG = {
    CONF_UNDERLYING_LIST: ["climate.mock_climate"],
    CONF_AC_MODE: True,
    CONF_AUTO_REGULATION_MODE: CONF_AUTO_REGULATION_STRONG,
    CONF_AUTO_REGULATION_DTEMP: 0.5,
    CONF_AUTO_REGULATION_PERIOD_MIN: 1,
}

# TODO remove this later
MOCK_PRESETS_CONFIG = {
    PRESET_FROST_PROTECTION + PRESET_TEMP_SUFFIX: 7,
    PRESET_ECO + PRESET_TEMP_SUFFIX: 16,
    PRESET_COMFORT + PRESET_TEMP_SUFFIX: 17,
    PRESET_BOOST + PRESET_TEMP_SUFFIX: 18,
}

# TODO remove this later
MOCK_PRESETS_AC_CONFIG = {
    PRESET_FROST_PROTECTION + PRESET_TEMP_SUFFIX: 7,
    PRESET_ECO + PRESET_TEMP_SUFFIX: 17,
    PRESET_COMFORT + PRESET_TEMP_SUFFIX: 19,
    PRESET_BOOST + PRESET_TEMP_SUFFIX: 20,
    PRESET_ECO + PRESET_AC_SUFFIX + PRESET_TEMP_SUFFIX: 25,
    PRESET_COMFORT + PRESET_AC_SUFFIX + PRESET_TEMP_SUFFIX: 23,
    PRESET_BOOST + PRESET_AC_SUFFIX + PRESET_TEMP_SUFFIX: 21,
}

MOCK_WINDOW_CONFIG = {
    CONF_WINDOW_SENSOR: "binary_sensor.window_sensor",
    # Not used normally only for tests to avoid rewrite all tests
    CONF_WINDOW_DELAY: 10,
}

MOCK_WINDOW_DELAY_CONFIG = {
    CONF_WINDOW_DELAY: 10,
}

MOCK_WINDOW_AUTO_CONFIG = {
    CONF_WINDOW_AUTO_OPEN_THRESHOLD: 1.0,
    CONF_WINDOW_AUTO_CLOSE_THRESHOLD: 0.0,
    CONF_WINDOW_AUTO_MAX_DURATION: 5.0,
    CONF_WINDOW_ACTION: CONF_WINDOW_FAN_ONLY,
}

MOCK_MOTION_CONFIG = {
    CONF_MOTION_SENSOR: "input_boolean.motion_sensor",
    CONF_MOTION_DELAY: 10,
    CONF_MOTION_OFF_DELAY: 30,
    CONF_MOTION_PRESET: PRESET_COMFORT,
    CONF_NO_MOTION_PRESET: PRESET_ECO,
}

MOCK_POWER_CONFIG = {
    CONF_POWER_SENSOR: "sensor.power_sensor",
    CONF_MAX_POWER_SENSOR: "sensor.power_max_sensor",
    CONF_PRESET_POWER: 10,
}

MOCK_PRESENCE_CONFIG = {
    CONF_PRESENCE_SENSOR: "person.presence_sensor",
}

MOCK_PRESENCE_AC_CONFIG = {
    CONF_PRESENCE_SENSOR: "person.presence_sensor",
}

MOCK_ADVANCED_CONFIG = {
    CONF_MINIMAL_ACTIVATION_DELAY: 10,
    CONF_SAFETY_DELAY_MIN: 5,
    CONF_SAFETY_MIN_ON_PERCENT: 0.4,
    CONF_SAFETY_DEFAULT_ON_PERCENT: 0.3,
}

MOCK_DEFAULT_FEATURE_CONFIG = {
    CONF_USE_WINDOW_FEATURE: False,
    CONF_USE_MOTION_FEATURE: False,
    CONF_USE_POWER_FEATURE: False,
    CONF_USE_PRESENCE_FEATURE: False,
}

MOCK_DEFAULT_CENTRAL_CONFIG = {
    CONF_USE_MAIN_CENTRAL_CONFIG: False,
    CONF_USE_TPI_CENTRAL_CONFIG: False,
    CONF_USE_PRESETS_CENTRAL_CONFIG: False,
    CONF_USE_WINDOW_CENTRAL_CONFIG: False,
    CONF_USE_MOTION_CENTRAL_CONFIG: False,
    CONF_USE_POWER_CENTRAL_CONFIG: False,
    CONF_USE_PRESENCE_CENTRAL_CONFIG: False,
    CONF_USE_ADVANCED_CENTRAL_CONFIG: False,
}
