"""Auto Parking - DAO Module"""

import firebase_admin
from firebase_admin import db, exceptions
import os

#path = "C:/auto-parking" if os.name =="nt" else "/home/auto-parking"

credential = firebase_admin.credentials.Certificate('./CSE-111/auto-parking/auto-parking-71c54.json')

db_url = "https://auto-parking-71c54-default-rtdb.firebaseio.com/"

default_app = firebase_admin.initialize_app(credential ,{"databaseURL": db_url})

db_ref = db.reference("/")

def new_parking(parking_data):
    """Push a new parking entry to Firebase. 
    Parameter: parking_data - A dictionary with vehicle's license plate, parking rate parking time.
    Returns:  Boolean"""
    
    parked_vehicles = db_ref.child("parked-vehicles")
    
    try:
            
        parked_vehicles.push(parking_data)
        
        return True
    
    except exceptions.FirebaseError as fire_error:
        
        print(fire_error.http_response, fire_error.cause)
        
        return False
    
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

#Informing correct file to execute
if __name__ == "__main__":
    print("Try starting 'Parking.py' file")