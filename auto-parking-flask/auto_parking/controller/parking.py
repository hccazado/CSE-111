import functools

from datetime import datetime

from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for

from werkzeug.security import check_password_hash, generate_password_hash

from .auth import login_required

from ..dao import dao

blue_print = Blueprint("parking", __name__, url_prefix="/parking")

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

def new():
    """Inserts a new vehicle's register into user database"""
    
    if request.method=="GET":
        return render_template("app/vehicle.html")
    
    else:
        plate = request.form["plate"]
        
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
                "user": session["user_node"],
                "plate":plate,
                "rate":rate,
                "client": client,
                "phone": phone,
                "parking_time": parking_time,
                "active": True
            }

            if dao.new_parking(new_vehicle):
                
                return redirect(url_for("index"))
