"""Auto Parking Flask - Test module"""

import json
from pytest import approx
import pytest
from auto_parking.controller import parking as controller
from auto_parking.dao import dao as model
from auto_parking.controller import auth
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash

node_user = None

test_vehicle = {
        "user": None,
        "plate":"AAA-1111",
        "rate":"0.99",
        "parking_time": controller.current_time(),
        "client": "Test",
        "phone": "123456",
        "active": True
    }

#Testing autentication auth's module functions

def test_new_user():
    """verifies that the new_user function from auth module is performing well and not accepting 
    username, email and hash as None (which represents left blank on the web form)
    """
    
    user_1 = {
        "user": None,
        "email":"test@email.com",
        "hash": str(generate_password_hash("123456"))
    }
        
    user_2 = {
        "user": "Tes".upper(),
        "email": None,
        "hash": generate_password_hash("123456")
    }
    
    user_3 = {
        "user": "Test".upper(),
        "email": "test@email.com",
        "hash": None
    }
    
    user_4 = {
        "user": "Test".upper(),
        "email": "test@email.com",
        "hash": generate_password_hash("123456")
    }
    
    assert auth.new_user(user_1) is False
    
    assert auth.new_user(user_2) is False
    
    assert auth.new_user(user_3) is False
    
    assert auth.new_user(user_4) is True
    
def test_pwd_check():
    """verifies that pwd_check from auth module is performing well."""
    
    pwd_hash = "pbkdf2:sha256:600000$cDmtYyQuB2WJ6RV4$4c36c783953159bd5c039a23ca1bf83826b1184c3bcc618c0d17773b8f97db4b"
    
    pwd = "123456"
    
    assert auth.pwd_check(pwd) is False
    
    assert auth.pwd_check(db_hash= pwd_hash) is False
    
    assert auth.pwd_check(pwd, pwd_hash) is True
    
def test_get_user():
    """Test function get_ser from auth module. and get firebase key for the test user previously created"""
    
    user = "TEST"
    pwd= "123456"
    
    global node_user
    
    assert auth.user_login(None, pwd) is False
    
    assert auth.user_login(user, "") is False
    
    assert auth.user_login(user) is False
    
    node_user = auth.user_login(user, pwd)
    
    assert  type(node_user) == str

    test_vehicle["user"] = node_user
    

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
    
    result = controller.new_parking(test_vehicle)
    
    assert type(result) is bool
    
    if result:
        vehicle = controller.get_active_parking(node_user, test_vehicle["plate"])
        
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
    
def test_get_user_vehicles():
    """verifies that get_user_vehicles function returns a list of cars from the logged user."""
    
    result = controller.get_user_vehicles(node_user)
    
    assert type(result) is list
    
def test_deleteremove_user():
    """verifies that dao delete_user function is performing well."""
        
    removal = model.delete_user(node_user)
    
    assert removal is True

    
# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
