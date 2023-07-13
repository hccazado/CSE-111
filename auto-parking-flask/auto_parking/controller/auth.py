import functools, uuid

from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for

from werkzeug.security import check_password_hash, generate_password_hash

from ..dao import dao

blue_print = Blueprint("auth", __name__, url_prefix="/auth")

def new_user(user = {}):
    """calls DAO new_user for inserting a new user into the system.
    Parameter: user - dictionary with data to be inserted into Firebase
    Return: boolean"""
    
    if user["user"] == None or user["email"] == None or user["hash"] == None or user == {}:
        
        return False
        
    else:
        
        return dao.new_user(user) 

def user_login(username = "", pwd = None):
    """returns a user if found and passwrod matches."""
    
    if username == None or pwd == None:
        
        return False
    
    elif len(username) < 3:
        
        return False
    
    else:
    
        users = dao.get_users()
        
        if users == {}:
            
            return False
        
        for key in users:

            if users[key]["user"] == username:

                if pwd_check(pwd, users[key]["hash"]):

                    return key
                
        return False

def pwd_check(pwd = None, db_hash = None):
    """verifies a password and user sotred hash.
    parameters: pwd: password typed in login form
                hash: stored hash in db
    returns: boolean"""
    
    if pwd == None or db_hash == None:
        
        return False

    if check_password_hash(db_hash, pwd):
        
        return True
    
    else:

        return False
    
def login_required(view):
    """Verifies that there's a DB user node key stored in session and redirects to login page if there's no session"""
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        
        if not "node_user" in session:
            
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view
    
@blue_print.route("/register", methods=("GET","POST"))

def register():
    """Creates a new client"""
    if request.method == "POST":

        user = request.form["user"]

        email = request.form["email"]

        phone = request.form["phone"]

        pwd = request.form["pwd"]
        
        error = None

        if not user or not email or not pwd or not phone:
            
            error = "One or more required fields are missing."
        
        if error == None:

            user_data = {
                "user": user,
                "email": email,
                "phone": phone,
                "hash": generate_password_hash(pwd)
            }
 
            if new_user(user_data):
                
                return redirect(url_for("auth.login"))
            
            else:
                
                error = "An error has ocurred creating the user!"

        flash(error)

    elif request.method == "GET":

        return render_template("auth/register.html")

@blue_print.route("/login", methods=("GET","POST"))

def login():
    """Checks HTTP request method, validates provided data and execute login"""

    if request.method == "POST":

        user = request.form["user"]
        
        pwd = request.form["pwd"]
                
        error = None

        if not user:
            
            error = "A User is required to login!"

        elif not pwd:

            error = "A Password is required!"

        if error == None:

            session.clear()

            login = user_login(user, pwd)

            if login:

                session["node_user"] = login

                return redirect(url_for("parking.index"))
            
            else:
                error = "Wrong user or password!"
            
        flash(error)
        
    return render_template("auth/login.html")
        
@blue_print.route("/logout")
    

def logout():
    """end user session"""
    session.pop("node_user", None)
    
    return redirect(url_for("auth.login"))

        
