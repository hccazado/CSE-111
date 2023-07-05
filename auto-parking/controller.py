"""Parkin Auto - Controller Module"""

import math
from datetime import datetime
import model as dao
import json
from json import JSONDecodeError

def current_time():
    """return the current date and time formated as: weekday month day hour:minute:seconds year
    Parameters: none
    Returns: formated current date and time"""
    
    current_dt = datetime.now().strftime("%d/%m/%y - %H:%M")
    return current_dt

def new_parking(plate, price):
    time = current_time()
    
    parked_car= {
        "plate": plate.upper(),
        "parked_time": time,
        "price": price,
        "active": True
    }

    parked_car = json.dumps(parked_car)
    
    result = dao.new_parking(parked_car)

    if result:
        return "Vehicle succesfully parked"
    else:
        return "Something Went Wrong!"
    

def get_vehicles():
    """return the list of parked vehicles converted to nested dictionaries
    Parameter: plate - vehicle license plate
    Return: Parking details"""

    dao_vehicles = dao.get_vehicles()

    #iterating dictionary and converting string item into a nested dictionary
    try:
        for key in dao_vehicles:
            dao_vehicles[key] = json.loads(dao_vehicles[key])

        return dao_vehicles
    
    except JSONDecodeError as error:
        print(error)
    
    

def search_parked_vehicle(plate):
    """Search for a informed plate and active parked vehicle
    Parameter: plate - vehicle license plate
    Return: Parking details"""

    plate = plate.strip().upper()

    vehicles = get_vehicles()
    
    for key in vehicles:
        if vehicles[key]["plate"] == plate and vehicles[key]["active"] == True:
            current_dt = current_time()
            return [key, 
                    vehicles[key]["plate"],
                    vehicles[key]["parked_time"],
                    current_dt,
                    vehicles[key]["price"]]
        else:
            return []
    
if __name__ == "__main__":
    print("Try starting 'Parking.py' file")