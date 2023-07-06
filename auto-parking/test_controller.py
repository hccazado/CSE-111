"""Parking Auto - Test module"""

from pytest import approx
import pytest
import controller
import model
from datetime import datetime, timedelta

test_vehicle = {
        "plate":"AAA-1111",
        "price":"0.99",
        "parking_time": controller.current_time()
    }

def test_current_time():
    """Verifies that the current_time function returns a string object with current time and current time"""
    
    string_time = controller.current_time()
    
    current_time = datetime.now().strftime("%d/%m/%y - %H:%M")
    
    assert type(string_time) is str
    
    assert string_time == current_time
    
def test_get_vehicles():
    """Verifies that the get_vehicles function returns a dictionary object"""
    
    result = model.get_vehicles()
    
    assert type(result) is dict
    
def test_new_parking():
    """Verifies that the new_parking function returns a boolean after pushing an element to Firebase.
    A successfull new parking will trigger and test search_parked_vehicle function, then will call model 
    controller delete_vehicle function to delete the thereof inserted test vehicle"""
    
    result = controller.new_parking(test_vehicle["plate"], test_vehicle["price"])
    
    assert type(result) is bool
    
    if result:
        vehicle = controller.search_parked_vehicle(test_vehicle["plate"])
        
        assert type(vehicle) is list
        
        key = vehicle[0]
        
        assert type(key) is str
        
        delete = model.delete_vehicle(key)
        
        assert delete is True

def test_compute_parking_rate():
    """verifies that compute_parking_rate function is returning a valid and accurate parking value.
    This function will also test compute_parked_time function."""
    
    start_time = "01/07/23 - 12:00"
    
    finish_time = "01/07/23 - 15:00"
    
    parking_time = controller.compute_parked_time(start_time, finish_time)
    
    result = controller.compute_parking_rate(2.0, parking_time)
    
    assert type(parking_time) is timedelta
    
    assert type(result) is float
    
    assert result == 6.0
    
def test_all_parked_vehicles():
    """verifies that all_parked_vehicles function returns a list"""
    
    result = controller.all_parked_vehicles()
    
    assert type(result) is list
    
def test_all_active_vehicles():
    """verifies that all_active_vehicles function returns a list"""
    
    result = controller.all_parked_vehicles()
    
    assert type(result) is list

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
