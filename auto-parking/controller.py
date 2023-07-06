"""Parkin Auto - Controller Module"""

import math
from datetime import datetime, timedelta
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
    """Create a dictonary with new parking information to be stored in Firebase.
    Parameter: plate - vehicle license plate
               price - a float with"""
               
    time = current_time()
    
    parked_car = {
        "plate": plate.upper(),
        "parked_time": time,
        "price": price,
        "active": True
    }
    
    result = dao.new_parking(parked_car)

    if result:
        
        return "Vehicle succesfully parked"
    
    else:
        
        return "Something Went Wrong!"
    

def get_vehicles():
    """return a dictionary of parked vehicles with nested dictionaries
    Parameter: plate - vehicle license plate
    Return: Parking details"""

    dao_vehicles = dao.get_vehicles()

    return dao_vehicles
    

def search_parked_vehicle(plate):
    """Search for a informed plate and active parked vehicle
    Parameter: plate - vehicle license plate
    Return: Parking details"""

    plate = plate.strip().upper()

    vehicles = get_vehicles()
    
    for key in vehicles:
        if vehicles[key]["plate"] == plate and vehicles[key]["active"] == True:
            
            current_dt = current_time()
            
            total_time = compute_parked_time(vehicles[key]["parked_time"], current_dt)
            
            payment_amount = compute_parking_rate(vehicles[key]["price"], total_time)
            
            return [key, 
                    vehicles[key]["plate"],
                    vehicles[key]["parked_time"],
                    total_time,
                    vehicles[key]["price"],
                    payment_amount]
    else:
        return []
        
def compute_parked_time(start_time, finish_time):
    """Computes total time that a vehicle remained parked.
    Parameter: start_time: datetime object whith starting parked time
               finish_time: datetime object whith finishing parked time, current time.
    Return: amounf of time a vehicle remained parked"""
    
    initial_time = datetime.strptime(start_time, "%d/%m/%y - %H:%M")
    
    finish_time = datetime.strptime(finish_time, "%d/%m/%y - %H:%M")
    
    total_time = finish_time - initial_time
    
    return total_time

def compute_parking_rate(rate, total_time):
    """Computes total rate according to vehicle's parked time.
    Parameter: rate: float number with vehicle's applied rate
               total_time: datetime object with vehicle's parked time
    Return: value of required payment"""
    
    hours = total_time / timedelta(hours=1)
    
    if hours <= 8:
        
        return round((float(hours) * float(rate)), 2)
    
    elif hours > 8:
        
        periods = hours/8
        
        return round((float(periods) * 5.0 * float(rate)), 2)
    
def finish_vehicle_parking(key, vehicle):
    """Finish a vehicle parking. Calls model controller and updates corresponding node.
    Parameter: key - firebase child node key string
               vehicle - dictionary with updated vehicle parking info
               
    return: Boolean returned from model controller"""
    
    result = dao.update_vehicle(key, vehicle)
    
    return result

def all_parked_vehicles():
    """Retrieves entire Firebase parked-vehicles list. 
    returns: list of license plates to view"""
    
    dao_vehicles = get_vehicles()
    
    plates = []
    
    for key in dao_vehicles:
        
        plates.append(dao_vehicles[key]["plate"])
        
    return plates

def all_active_vehicles():
    """Retrieves entire Firebase parked-vehicles list. 
    returns: list of active parked license plates to view"""
    
    dao_vehicles = get_vehicles()
    
    plates = []
    
    for key in dao_vehicles:
        
        if dao_vehicles[key]["active"] == True:
            
            plates.append(dao_vehicles[key]["plate"])
        
    return plates

#Informing correct file to execute
if __name__ == "__main__":
    print("Try starting 'Parking.py' file")