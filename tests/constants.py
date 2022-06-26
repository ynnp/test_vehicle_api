""" Constants for vehicle api
"""
HOST = "http://localhost"
PORT = 8099

SIGNALS_ENDPOINT = "signals"
PINS_ENDPOINT = "pins"
UPDATE_ALL_PINS_ENDPOINT = "update_pins"
UPDATE_ONE_PIN_ENDPOINT = "update_pin"

GEAR_PIN_ID_1 = 1
GEAR_PIN_ID_2 = 2
ACC_PEDAL_PIN_ID = 3
BRAKE_PEDAL_PIN_ID = 4
BATTERY_PIN_ID = 5

GEAR_SIGNAL_ID = 1
ACC_PEDAL_SIGNAL_ID = 2
BRAKE_PEDAL_SIGNAL_ID = 3
REQ_TORQUE_SIGNAL_ID = 4
BATTERY_SIGNAL_ID = 5

BATTERY_STATE_READY = "Ready"
BATTERY_STATE_NOT_READY = "NotReady"
BATTERY_STATE_ERROR = "Error"
BATTERY_STATE_PINS = {BATTERY_STATE_READY: {'min': 400,
                                            'max': 800},
                      BATTERY_STATE_NOT_READY: {'min': 0,
                                                'max': 400},
                      BATTERY_STATE_ERROR: {'min': 0,
                                            'max': 800}
                     }

BRAKE_PEDAL_STATE_ERROR = "Error"
BRAKE_PEDAL_STATE_PRESSED = "Pressed"
BRAKE_PEDAL_STATE_RELEASED = "Released"
BRAKE_PEDAL_STATE_PINS = {BRAKE_PEDAL_STATE_ERROR: {'min': 1,
                                                    'max': 3},
                          BRAKE_PEDAL_STATE_PRESSED: {'min': 1,
                                                      'max': 2},
                          BRAKE_PEDAL_STATE_RELEASED: {'min': 2,
                                                       'max': 3}
                         }

GEAR_POSITION_PARK = "Park"
GEAR_POSITION_NEUTRAL = "Neutral"
GEAR_POSITION_REVERSE = "Reverse"
GEAR_POSITION_DRIVE = "Drive"
GEAR_POSITION_PINS = {GEAR_POSITION_PARK: {'pin_1': 0.67,
                                           'pin_2': 3.12},
                      GEAR_POSITION_NEUTRAL: {'pin_1': 1.48,
                                              'pin_2': 2.28},
                      GEAR_POSITION_REVERSE: {'pin_1': 2.28,
                                              'pin_2': 1.48},
                      GEAR_POSITION_DRIVE: {'pin_1': 3.12,
                                            'pin_2': 0.67}
                     }

ACC_PEDAL_POS_ERROR = "Error"
ACC_PEDAL_POS_0 = "0 %"
ACC_PEDAL_POS_30 = "30 %"
ACC_PEDAL_POS_50 = "50 %"
ACC_PEDAL_POS_100 = "100 %"
ACC_PEDAL_POS_PINS = {ACC_PEDAL_POS_ERROR: {'min': 1,
                                            'max': 3.5},
                      ACC_PEDAL_POS_0: {'min': 1,
                                        'max': 2},
                      ACC_PEDAL_POS_30: {'min': 2,
                                         'max': 2.5},
                      ACC_PEDAL_POS_50: {'min': 2.5,
                                         'max': 3},
                      ACC_PEDAL_POS_100: {'min': 3,
                                          'max': 3.5}
                     }

REQ_TORQUE_STATES = {ACC_PEDAL_POS_ERROR: 0,
                     ACC_PEDAL_POS_0: 0,
                     ACC_PEDAL_POS_30: 3000,
                     ACC_PEDAL_POS_50: 5000,
                     ACC_PEDAL_POS_100: 10000}
