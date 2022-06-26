""" Tests for Vehicle system
"""
import constants as cs
import vehicle_api

import pytest
import random
import requests


def teardown_function(function):
    requests.post(vehicle_api.get_update_pins_url(pin_id=cs.BATTERY_PIN_ID), data={'Voltage': 0})


# tests 1, 2, 3, 4
@pytest.mark.parametrize("state", [cs.GEAR_POSITION_PARK, cs.GEAR_POSITION_NEUTRAL, 
                                   cs.GEAR_POSITION_REVERSE, cs.GEAR_POSITION_DRIVE])
def test_check_gear_position_signal(state):
    """ Test to check gear position state
    """
    battery_state = vehicle_api.set_battery_state(cs.BATTERY_STATE_READY)
    assert battery_state == cs.BATTERY_STATE_READY
    brake_pedal_state = vehicle_api.set_brake_pedal_state(cs.BRAKE_PEDAL_STATE_PRESSED)
    assert brake_pedal_state == cs.BRAKE_PEDAL_STATE_PRESSED
    acc_pedal_state = vehicle_api.set_acc_pedal_state(cs.ACC_PEDAL_POS_0)
    assert acc_pedal_state == cs.ACC_PEDAL_POS_0
    
    gear_state = vehicle_api.set_gear_state(state)
    assert gear_state == state
    
    
# tests 8, 12, 13, 14
@pytest.mark.parametrize("state, voltage", [(cs.BATTERY_STATE_NOT_READY, None),
                                            (cs.BATTERY_STATE_ERROR, -1),
                                            (cs.BATTERY_STATE_ERROR, 801),
                                            (cs.BATTERY_STATE_ERROR, 0)])
def test_switch_battery_state_while_driving(state, voltage):
    """ Test to check the battery state after switching it while driving
    """
    battery_state = vehicle_api.set_battery_state(cs.BATTERY_STATE_READY)
    assert battery_state == cs.BATTERY_STATE_READY
    brake_pedal_state = vehicle_api.set_brake_pedal_state(cs.BRAKE_PEDAL_STATE_PRESSED)
    assert brake_pedal_state == cs.BRAKE_PEDAL_STATE_PRESSED
    acc_pedal_state = vehicle_api.set_acc_pedal_state(cs.ACC_PEDAL_POS_0)
    assert acc_pedal_state == cs.ACC_PEDAL_POS_0
    gear_state = vehicle_api.set_gear_state(cs.GEAR_POSITION_DRIVE)
    assert gear_state == cs.GEAR_POSITION_DRIVE
    
    new_battery_state = vehicle_api.set_battery_state(state, voltage) 
    assert new_battery_state == state
   

# test 10
def test_press_brake_pedal_while_battery_not_ready():
    """ Test to check brake pedal state after switching battery state to not ready
    """
    battery_state = vehicle_api.set_battery_state(cs.BATTERY_STATE_READY)
    assert battery_state == cs.BATTERY_STATE_READY
    brake_pedal_state = vehicle_api.set_brake_pedal_state(cs.BRAKE_PEDAL_STATE_PRESSED)
    assert brake_pedal_state == cs.BRAKE_PEDAL_STATE_PRESSED
    acc_pedal_state = vehicle_api.set_acc_pedal_state(cs.ACC_PEDAL_POS_0)
    assert acc_pedal_state == cs.ACC_PEDAL_POS_0
    gear_state = vehicle_api.set_gear_state(cs.GEAR_POSITION_DRIVE)
    assert gear_state == cs.GEAR_POSITION_DRIVE
    
    brake_pedal_state = vehicle_api.set_brake_pedal_state(cs.BRAKE_PEDAL_STATE_RELEASED)
    assert brake_pedal_state == cs.BRAKE_PEDAL_STATE_RELEASED
    battery_state = vehicle_api.set_battery_state(cs.BATTERY_STATE_NOT_READY) 
    assert battery_state == cs.BATTERY_STATE_NOT_READY
    
    new_brake_pedal_state = vehicle_api.set_brake_pedal_state(cs.BRAKE_PEDAL_STATE_PRESSED)
    assert new_brake_pedal_state == cs.BRAKE_PEDAL_STATE_PRESSED
    
    
# test 11
def test_press_acc_pedal_while_battery_not_ready():
    """ Test to check acc pedal state after switching battery state to not ready
    """
    battery_state = vehicle_api.set_battery_state(cs.BATTERY_STATE_READY)
    assert battery_state == cs.BATTERY_STATE_READY
    brake_pedal_state = vehicle_api.set_brake_pedal_state(cs.BRAKE_PEDAL_STATE_PRESSED)
    assert brake_pedal_state == cs.BRAKE_PEDAL_STATE_PRESSED
    acc_pedal_state = vehicle_api.set_acc_pedal_state(cs.ACC_PEDAL_POS_0)
    assert acc_pedal_state == cs.ACC_PEDAL_POS_0
    gear_state = vehicle_api.set_gear_state(cs.GEAR_POSITION_DRIVE)
    assert gear_state == cs.GEAR_POSITION_DRIVE
    
    brake_pedal_state = vehicle_api.set_brake_pedal_state(cs.BRAKE_PEDAL_STATE_RELEASED)
    assert brake_pedal_state == cs.BRAKE_PEDAL_STATE_RELEASED
    battery_state = vehicle_api.set_battery_state(cs.BATTERY_STATE_NOT_READY) 
    assert battery_state == cs.BATTERY_STATE_NOT_READY
    
    new_acc_pedal_state = vehicle_api.set_acc_pedal_state(cs.ACC_PEDAL_POS_50)
    assert new_acc_pedal_state == cs.ACC_PEDAL_POS_50
    
    
# tests 29, 30
@pytest.mark.parametrize("gear_state, acc_pedal_state", [(cs.GEAR_POSITION_DRIVE, cs.ACC_PEDAL_POS_30),
                                                         (cs.GEAR_POSITION_REVERSE, cs.ACC_PEDAL_POS_50)])
def test_check_req_torque_while_brake_pedal_and_acc_pedal_pressed(gear_state, acc_pedal_state):
    """ Test to check req torque state while brake pedal and acc pedal are both pressed
    """
    battery_state = vehicle_api.set_battery_state(cs.BATTERY_STATE_READY)
    assert battery_state == cs.BATTERY_STATE_READY
    brake_pedal_state = vehicle_api.set_brake_pedal_state(cs.BRAKE_PEDAL_STATE_PRESSED)
    assert brake_pedal_state == cs.BRAKE_PEDAL_STATE_PRESSED
    acc_pedal_state = vehicle_api.set_acc_pedal_state(cs.ACC_PEDAL_POS_0)
    assert acc_pedal_state == cs.ACC_PEDAL_POS_0
    current_gear_state = vehicle_api.set_gear_state(gear_state)
    assert current_gear_state == gear_state
    
    current_acc_pedal_state = vehicle_api.set_acc_pedal_state(acc_pedal_state)
    assert current_acc_pedal_state == acc_pedal_state
    
    req_torque_state = vehicle_api.get_req_torque_state()
    assert req_torque_state == "0 Nm"
    