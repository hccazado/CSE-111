import functools

from datetime import datetime, timedelta

from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for

from .auth import login_required

from ..dao import dao

from ..controller import parking

global vehicle

blue_print = Blueprint("summary", __name__, url_prefix="/summary")

@blue_print.route("/")
@login_required

def index():
    """Display all client's vehicles"""

    vehicles = parking.get_user_vehicles(session["node_user"])

    return render_template("app/summary.html", vehicles=vehicles)

