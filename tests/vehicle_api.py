""" File with vehicle api functions
"""
import constants as cs

import random
import requests


def get_signal_url(signal_id):
    """ Function to build URL for getting signal by id
    
    :param signal_id: signal id to get
    :type signal_id: int
    :returns: URL for getting signal
    :rtype: str
    """
    url = "{host}:{port}/api/{signals}/{signal_id}".format(host=cs.HOST, port=cs.PORT, signals=cs.SIGNALS_ENDPOINT,
                                                           signal_id=signal_id)
    
    return url
   
    
def get_update_pins_url(pin_id=None):
    """ Function to build URL for updating multiple pins or single pin by id
    
    :param pin_id: pin id to update
    :type pin_id: int
    :returns: URL for updating pin(s)
    :rtype: str
    """
    if pin_id:
        url = "{host}:{port}/api/{pins}/{pin_id}/{update}".format(host=cs.HOST, port=cs.PORT, pins=cs.PINS_ENDPOINT,
                                                                  pin_id=pin_id, update=cs.UPDATE_ONE_PIN_ENDPOINT)
    else:
        url = "{host}:{port}/api/{pins}/{update}".format(host=cs.HOST, port=cs.PORT, pins=cs.PINS_ENDPOINT, 
                                                         update=cs.UPDATE_ALL_PINS_ENDPOINT)
    
    return url


def build_dict_for_updating_pins(pins, voltage):
    """ Function to build dict for updating pins
    
    :param pins: pin ids to update
    :type pins: list
    :param voltage: desired voltage for each pin
    :type voltage: list
    :returns: dict for updating pins 
    :rtype: dict
    """
    pins_dict = {'Pins': []}
    for pin_id, vltg in zip(pins, voltage):
        pins_dict["Pins"].append({'PinId': pin_id, 'Voltage': vltg})
    
    return pins_dict
    

def set_battery_state(state, voltage=None):
    """ Function to set battery to desired state
    
    :param state: desired battery state
    :type state: str
    :param voltage: desired voltage
    :param voltage: int
    :returns: updated battery state
    :rtype: str
    """
    if voltage is None:
        voltage = random.randint(cs.BATTERY_STATE_PINS[state]["min"] + 1, 
                                 cs.BATTERY_STATE_PINS[state]["max"])
    
    requests.post(get_update_pins_url(pin_id=cs.BATTERY_PIN_ID), data={'Voltage': voltage})
    battery_state = requests.get(get_signal_url(cs.BATTERY_SIGNAL_ID)).json()
    
    return battery_state["Value"]
    
    
def set_brake_pedal_state(state, voltage=None):
    """ Function to set brake pedal to desired state
    
    :param state: desired brake pedal state
    :type state: str
    :param voltage: desired voltage
    :param voltage: float
    :returns: updated brake pedal state
    :rtype: str
    """
    if voltage is None:
        voltage = round(random.uniform(cs.BRAKE_PEDAL_STATE_PINS[state]["min"], 
                                       cs.BRAKE_PEDAL_STATE_PINS[state]["max"]),
                        2)
    
    requests.post(get_update_pins_url(pin_id=cs.BRAKE_PEDAL_PIN_ID), data={'Voltage': voltage})
    brake_pedal_state = requests.get(get_signal_url(cs.BRAKE_PEDAL_SIGNAL_ID)).json()
    
    return brake_pedal_state["Value"]
    
    
def set_acc_pedal_state(state, voltage=None):
    """ Function to set acceleration pedal to desired state
    
    :param state: desired acc pedal state
    :type state: str
    :param voltage: desired voltage
    :param voltage: float
    :returns: updated acc pedal state
    :rtype: str
    """
    if voltage is None:
        voltage = round(random.uniform(cs.ACC_PEDAL_POS_PINS[state]["min"], 
                                       cs.ACC_PEDAL_POS_PINS[state]["max"]),
                        2)
    
    requests.post(get_update_pins_url(pin_id=cs.ACC_PEDAL_PIN_ID), data={'Voltage': voltage})
    acc_pedal_state = requests.get(get_signal_url(cs.ACC_PEDAL_SIGNAL_ID)).json()
    
    return acc_pedal_state["Value"]
    
    
def set_gear_state(state):
    """ Function to set gear to desired state
    
    :param state: desired gear state
    :type state: str
    :returns: updated gear state
    :rtype: str
    """
    data = build_dict_for_updating_pins([cs.GEAR_PIN_ID_1, cs.GEAR_PIN_ID_2], 
                                        [cs.GEAR_POSITION_PINS[state]["pin_1"], cs.GEAR_POSITION_PINS[state]["pin_2"]])
    requests.post(get_update_pins_url(), json=data)
    gear_state = requests.get(get_signal_url(cs.GEAR_SIGNAL_ID)).json()
    
    return gear_state["Value"]
    
    
def get_req_torque_state():
    """ Function to get req torque state
    
    :param: None
    :returns: current req torque state
    :rtype: str
    """
    req_torque_state = requests.get(get_signal_url(cs.REQ_TORQUE_SIGNAL_ID)).json()
    
    return req_torque_state["Value"]
