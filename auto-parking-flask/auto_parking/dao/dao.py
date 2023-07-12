"""Auto Parking Flask - DAO Module"""

import firebase_admin
from firebase_admin import db, exceptions
import os

#path = "C:/auto-parking" if os.name =="nt" else "/home/auto-parking"

credential = firebase_admin.credentials.Certificate('parking-flask-firebase-adminsdk.json')

db_url = "https://parking-flask-default-rtdb.firebaseio.com/"

default_app = firebase_admin.initialize_app(credential ,{"databaseURL": db_url})

db_ref = db.reference("/")

def new_parking(parking_data):
    """Push a new parking entry to Firebase. 
    Parameter: parking_data - A dictionary with vehicle's license plate, parking rate parking time.
    Returns:  Boolean"""
    
    parked_vehicles = db_ref.child("parked-vehicles")
    
    if "plate" in parking_data:
    
        try:
                
            parked_vehicles.push(parking_data)
            
            return True
        
        except exceptions.FirebaseError as fire_error:
            
            print(fire_error.http_response, fire_error.cause)
            
            return False
    
    else:
        
        return False
    
def new_user(user_data):
    """Push a new user entry to Firebase. 
    Parameter: userg_data - A dictionary with user's name, email, phone, password.
    Returns:  Boolean"""
    
    users = db_ref.child("users")
    
    try:
            
        users.push(user_data)
        
        return True
    
    except exceptions.FirebaseError as fire_error:
        
        print(fire_error.http_response, fire_error.cause)
        
        return False
    
def get_users():
    """Get a json with all users stored in Firebase.
    Returns: a dictionary"""
    
    registered_users = db_ref.child("users")

    try:
        users = registered_users.get()
        
        return users
    
    except exceptions.FirebaseError as fire_error:
        
        print(fire_error.http_response, fire_error.cause)
        
        return {}
    
def get_vehicles():
    """Get a json with all the vehicles stored in Firebase.
    Returns: a dictionary"""
    
    parked_vehicles = db_ref.child("parked-vehicles")

    try:
        vehicles = parked_vehicles.get()
        
        return vehicles
    
    except exceptions.FirebaseError as fire_error:
        
        print(fire_error.http_response, fire_error.cause)
        
        return {}
    
def update_vehicle(key, vehicle):
    """Update specific stored vehicle in Firebase.
    Returns: Boolean"""
    
    parked_vehicles = db_ref.child("parked-vehicles")
    
    vehicle_node = parked_vehicles.child(key)
    
    try:
        
        vehicle_node.update(vehicle)
        
        return True
    
    except exceptions.FirebaseError as fire_error:
        
        print(fire_error.http_response, fire_error.cause)
        
        return False
    
def delete_vehicle(key):
    """Deletes a specific node. 
    returns: boolean
    
    -> This function is only used in test_controller file."""
    
    parked_vehicles = db_ref.child("parked-vehicles")
    
    vehicle_node = parked_vehicles.child(key)
    
    try: 
        
        vehicle_node.delete()
        
        return True
    
    except exceptions.FirebaseError as fire_error:
        
        print(fire_error.http_response, fire_error.cause)
        
        return False

#Informing correct file to execute
if __name__ == "__main__":
    print("Try starting 'Parking.py' file")