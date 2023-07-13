import functools

from datetime import datetime, timedelta

from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for

from .auth import login_required

from ..dao import dao

global vehicle

blue_print = Blueprint("parking", __name__, url_prefix="/parking")

def new_parking(new_vehicle):
    """calls Dao new parking to store a new parked vehicle
    Parameter: new_vehicle - a dictionary with new parking data
    Return: boolean"""
    
    if new_vehicle["plate"] == None or  not new_vehicle["plate"] or new_vehicle["user"] == None or not new_vehicle["user"]:
        
        return False
    
    return dao.new_parking(new_vehicle)
    
def compute_parked_time(start_time, finish_time):
    """Computes total time that a vehicle remained parked.
    Parameter: start_time: datetime object whith starting parked time
               finish_time: datetime object whith finishing parked time, current time.
    Return: amounf of time a vehicle remained parked"""
    
    initial_time = datetime.strptime(start_time, "%d/%m/%y - %H:%M")
    
    finish_time = datetime.strptime(finish_time, "%d/%m/%y - %H:%M")
    
    total_time = finish_time - initial_time
    
    return total_time

def get_user_vehicles(node_user):
    """gets a list of vehicles
    parameter: user_node - user firebase node key
    return: list of user vehicles
    """
    vehicles = dao.get_vehicles()

    user_vehicles = []

    for key in vehicles:
        
        if vehicles[key]["user"] == node_user:

            vehicles[key]["key"] = key

            user_vehicles.append(vehicles[key])

    return user_vehicles

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

def get_active_parking(user_node, plate):
    """gets a user active vehicle
    parameter: user_node - user firebase node key
               plate - vehicle's license plate
    return: a dictionary
    """
    vehicles = get_user_vehicles(user_node)

    for vehicle in vehicles:

        if vehicle["plate"] == plate and vehicle["active"] == True:

            current_dt = current_time()

            total_time = compute_parked_time(vehicle["parking_time"], current_dt)

            payment_amount = compute_parking_rate(vehicle["rate"], total_time)

            return [vehicle["key"],
                    vehicle["user"], 
                    vehicle["plate"],
                    vehicle["parking_time"],
                    vehicle["rate"],
                    vehicle["client"],
                    vehicle["phone"],
                    current_dt,
                    total_time,
                    payment_amount]
    
    return []
        
def finish_vehicle_parking(node_vehicle, vehicle):
    """Finish a vehicle parking. Calls model controller and updates corresponding node.
    Parameter: node_vehicle - firebase child node key string
               vehicle - dictionary with updated vehicle parking info
               
    return: Boolean returned from model controller"""
    
    result = dao.update_vehicle(node_vehicle, vehicle)
    
    return result
        
def current_time():
    """return the current date and time formated as: weekday month day hour:minute:seconds year
    Parameters: none
    Returns: formated current date and time"""
    
    current_dt = datetime.now().strftime("%d/%m/%y - %H:%M")
    
    return current_dt

@blue_print.route("/") 
@login_required

def index():
    """loads the main app page. A session is required."""
    return render_template("app/index.html")

@blue_print.route("/new", methods=("GET","POST"))
@login_required

def new():
    """Inserts a new vehicle's register into user database"""
    
    if request.method=="GET":
        return render_template("app/vehicle.html")
    
    else:
        plate = request.form["plate"].upper()
        
        rate = request.form["rate"]
        
        client = request.form["client"]
        
        phone = request.form["phone"]

        parking_time = current_time()

        error = None

        if not plate:
            error = "A license plate is requrired!"

        elif not rate:
            error ="A Parking rate is required!"

        if error == None:

            new_vehicle = {
                "user": session["node_user"],
                "plate":plate,
                "rate":rate,
                "client": client,
                "phone": phone,
                "parking_time": parking_time,
                "active": True
            }

            if new_parking(new_vehicle):
                
                return redirect(url_for("parking.index"))
            
            else:
                
                error = "An error has ocurred!"

        else:

            flash(error)

            return render_template("app/vehicle.html")

@blue_print.route("/finish", methods=("GET", "POST"))
@login_required

def finish_search():
    """Gets vehicle's license plate, search for the active vehicle 
    returning a view with parking data and total cost."""
    
    if request.method == "GET":

        return render_template("app/finish_search.html")
    
    else:
        plate = request.form["plate"].upper()

        vehicle = get_active_parking(session["node_user"], plate)

        if len(vehicle) > 0:

            return redirect(url_for("parking.finish", vehicle_plate=plate))
        
        else: 

            error = "The informed license plate doesn't have an active parking."

            flash(error)

            return render_template("app/finish_search.html")
    
@blue_print.route("/finish/<vehicle_plate>", methods=("GET", "POST"))
@login_required

def finish(vehicle_plate):
    """Gets the URI plate endpoint as parameter then displays 
    parking details from this specific vehicle from logged in user"""
    
    global vehicle

    if request.method == "GET":

        plate = vehicle_plate

        vehicle = get_active_parking(session["node_user"], plate)

        return render_template("app/finish.html", vehicle = vehicle)
    
    elif request.method == "POST":

        updt_vehicle = {
            "user": vehicle[1],
            "plate": vehicle[2],
            "parking_time": vehicle[3],
            "finished_parking": str(current_time()),
            "stayed_time": str(vehicle[8]),
            "rate": vehicle[4],
            "client": vehicle[5],
            "phone": vehicle[6],
            "payment": vehicle[9],
            "active": False
            }
        
        if finish_vehicle_parking(vehicle[0], updt_vehicle):
            
            return redirect(url_for("parking.index"))
        
        else:
            
            error = "An error has ocurred!"

            flash(error)

            return render_template("app/finish_search.html")
                    

