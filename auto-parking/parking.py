"""Super Auto Parking is a BYUI - CSE111 course final project.
Writing by Heitor Cazado. """

import tkinter as tk
from tkinter import Frame, Label, Button, Entry, ttk
import math
import datetime
import controller

def main ():
    """Main function will generate program's main GUI widget with tkinter.
    """
    #creating GUI root level
    root = tk.Tk()

    #creating main frame with minimal geometry size
    root.minsize(500,300)

    #Setting app title
    root.title("Super Auto Parking")

    #Definiing tab control
    frm_notebook = ttk.Notebook(root)
    frm_notebook.pack(pady=5, expand=True)

    frm_new_parking = Frame(frm_notebook,width=500, height=280)
    frm_finish_parking = Frame(frm_notebook,width=500, height=280)
    frm_update_parking = Frame(frm_notebook,width=500, height=280)

    frm_new_parking.pack(pady=10, padx=10, fill="both", expand=True)
    frm_finish_parking.pack(fill="both", expand=True)
    frm_update_parking.pack(fill="both", expand=True)

    frm_notebook.add(frm_new_parking,text="New Parking")
    frm_notebook.add(frm_finish_parking,text="Finish Parking")
    frm_notebook.add(frm_update_parking, text="Update Parking")

    
    popuplate_new_parking_frame(frm_new_parking)
    populate_finish_parking_frame(frm_finish_parking)
    
    root.mainloop()

def popuplate_new_parking_frame(frm_new_parking):
    """Populate program's New Parking notebook's frame with its widgets
    Parameter: frm_new_parking: A tkinter Frame object
    Return: nothing"""

    #widgets variables
    #lbl_welcome = Label(frm_main, text="Welcome to Super Auto Parking App")
    lbl_plate = Label(frm_new_parking, text="License Plate:")
    lbl_price = Label(frm_new_parking, text="Value /Hour:")
    lbl_operation_result = Label(frm_new_parking, padx=4)
    ent_price = Entry(frm_new_parking)
    ent_plate = Entry(frm_new_parking)


    btn_park = Button(frm_new_parking, text="Park Car", state="disabled")
    btn_clr = Button(frm_new_parking, text="Clear")

    #Placing widgets
    #lbl_welcome.grid(row=0, column=0, columnspan=4)
    lbl_plate.grid(row=1, column=0, padx=3, pady=3)
    ent_plate.grid(row=1, column=1, padx=3, pady=3)
    lbl_price.grid(row=2, column=0, padx=3, pady=3)
    ent_price.grid(row=2, column=1, padx=3, pady=3)
    lbl_operation_result.grid(row=4, column=0, columnspan=3)

    btn_park.grid(row=5, column=0, padx=3, pady=3)
    btn_clr.grid(row=5, column=1, padx=3, pady=3)

    ent_price.insert(0,"10.00")

    #btn park functions

    def clear():
        "Clean entry widgets and disable Park Car Button"
        ent_plate.delete(0, "end")
        ent_price.delete(0, "end")
        ent_price.insert(0, "10.00")
        disable_park()
    
    def verify_plate(event):
        plate = ent_plate.get()
        if len(plate)<7:
            btn_park.configure(state="disabled")
            ent_plate.configure(background="pale violet red")
            lbl_operation_result.config(text="Very Short Plate", foreground="maroon")
        else:
            btn_park.configure(state="normal")
            ent_plate.configure(background="lightgreen")
            lbl_operation_result.config(text="")

    def disable_park():
        """Disable Park Car button"""
        btn_park.configure(state="disabled")

    def park():
        """Gets vehicle's license plate, and call model module to store new's parked car data
        """
        plate = ent_plate.get()
        price = ent_price.get()
        result = controller.new_parking(plate, price)
        lbl_operation_result.config(text=result)
        clear()


    ent_plate.bind("<KeyRelease>", verify_plate)

    btn_park.config(command = park)
    btn_clr.config(command = clear)

def populate_finish_parking_frame(frm_finish_parking):
    """Populate program's New Parking notebook's frame with its widgets
    Parameter: frm_finish_parking: A tkinter Frame object
    Return: nothing"""

    #defining widgets for Finish parking frame
    lbl_key_msg = Label(frm_finish_parking, text="Parking key:", padx=5, pady=5)
    lbl_key = Label(frm_finish_parking, padx=3)
    lbl_plate = Label(frm_finish_parking, text="License Plate to finish:")
    lbl_cost_msg = Label(frm_finish_parking, text="Parking Rate/Hour:")
    lbl_rate = Label(frm_finish_parking, padx=3, foreground="red")
    lbl_sep = Label(frm_finish_parking, text=" - ")
    lbl_duration_msg = Label(frm_finish_parking, text="Vehicle Parked From/To:")
    lbl_start_time = Label(frm_finish_parking, padx=3)
    lbl_finish_time = Label(frm_finish_parking, padx=3)
    lbl_operation_result = Label(frm_finish_parking, padx=4, foreground="maroon")

    ent_plate = Entry(frm_finish_parking)

    btn_search = Button(frm_finish_parking, text="Search Vehicle", state="disabled")
    btn_finish = Button(frm_finish_parking, text="Finish Parking", state="disabled")

    #placing Finish Parking widgets in frame's grid
    lbl_key_msg.grid(row=1, column=0, padx=2, pady=2)
    lbl_key.grid(row=1, column=1, padx=2, pady=2)
    lbl_plate.grid(row=0, column=0, padx=2, pady=2)
    ent_plate.grid(row=0, column=2, padx=2, pady=2)
    btn_search.grid(row=0, column=3, padx=2, pady=2)

    lbl_duration_msg.grid(row=2, column=0, padx=1,pady=1)
    lbl_start_time.grid(row=2, column=1, padx=1, pady=1)
    lbl_sep.grid(row=2, column=2, padx=1, pady=1)
    lbl_finish_time.grid(row=2, column=3, padx=1, pady=1)

    lbl_cost_msg.grid(row=3, column=0, padx=3, pady=3)
    lbl_rate.grid(row=3,column=1, padx=3, pady=3)
    
    lbl_operation_result.grid(row=5, column=0, padx=3, pady=3)

    btn_finish.grid(row=5, column=3, padx=2, pady=2)

    #functions for this frame
    def clear():
        """Clearing time labels, rate label, entry plate, and disabling buttons"""
        ent_plate.delete(0, "end")
        lbl_rate.configure(text="")
        lbl_start_time.configure(text="")
        lbl_finish_time.configure(text="")
        btn_finish.configure(state="disabled")
        btn_search.configure(state="disabled")

    def check_plate(event):
        plate = ent_plate.get()
        
        if len(plate) < 7:
            ent_plate.configure(background="pale violet red")
            lbl_operation_result.configure(text="Very Short Plate")
        
        else:
            ent_plate.configure(background="light green")
            lbl_operation_result.configure(text="")
            btn_search.configure(state="active")
        
    def search_parked_vehicle():
        plate = ent_plate.get()
        result = controller.search_parked_vehicle(plate)
        clear()
        if len(result) == 0:
            lbl_operation_result.configure(text="No active parking found for this plate")
        
        else:
            lbl_key.configure(text=result[0])
            ent_plate.insert(0, result[1])
            lbl_start_time.configure(text=result[2])
            lbl_finish_time.configure(text=result[3])
            lbl_rate.configure(text=result[4])    


    ent_plate.bind("<KeyRelease>", check_plate)

    btn_search.configure(command=search_parked_vehicle)





if __name__ == "__main__":
    main()


