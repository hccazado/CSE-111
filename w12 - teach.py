"""Teach team activity for W12 from BYU-I, CSE-111 course. This program generates a basic GUI
and will accept numbers entry for calculating the area of a circle."""

import tkinter as tk
from tkinter import Frame, Label, Button, Entry
import math

def main():
    """main function generates the GUI, and call reponsible function for populating program's main window.
    """
    #create a instance of tkinter top-level object
    root = tk.Tk()

    #creating the main frame(window)
    frm_main = Frame(root)

    frm_main.master.title("Area of a circle")

    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)
    
    populate_main_window(frm_main)

    #starting the loop of tkinter that processes user events
    #those events are key presses and mouse button clicks
    root.mainloop()

#Naming convention:
# frm: a frame (window) widget
# lbl: a label widget that displays text for the user to see
# ent: an entry widget where a user will type text or numbers
# btn: a button widget that the user will click

def populate_main_window(frm_main):
    """Populate the correspondent components(widgets) in place into this program's window.
    Parameter: frm_main - The main frame(window) 
    Return: nothing"""
    
    #create label for circle radius
    lbl_radius = Label(frm_main, text="Circle radius in cm (3.2)")
    
    #create entry for the radius
    ent_rad = Entry(frm_main)
    
    #labels for result
    lbl_unit = Label(frm_main, text="Cm")
    lbl_unit_res = Label(frm_main, text="Cm2")
    lbl_res_txt = Label(frm_main, text="Circle's area is: ")
    lbl_res_value = Label(frm_main, width=3)
    
    #creating a clear button
    btn_clear = Button(frm_main, text="Clear")
    
    #layout all elements in a grid
    lbl_radius.grid(row=0, column=0, padx=3, pady=3)
    ent_rad.grid(   row=0, column=1, padx=3, pady=3)
    lbl_unit.grid(  row=0, column=2, padx=3, pady=3)
    lbl_res_txt.grid(row=1, column=0, padx=3, pady=3)
    lbl_res_value.grid(row=1, column=1, padx=3, pady=3)
    lbl_unit_res.grid( row=1, column=2, padx=3, pady=3)
    
    btn_clear.grid(row=2, column=0, columnspan=4, padx=3, pady=3, sticky="w")
    
    def areaCalculate(event):
        """Calculates the are of the circle every time a key is pressed"""
        try:
            radius = float(ent_rad.get())
            
            area = math.pi * pow(radius, 2)
            area = round(area, 2)
            lbl_res_value.config(text=area)
        except ValueError as error:
            #print(type(error).__name__)
            lbl_res_value.config(text="Error")


    def clear():
        btn_clear.focus()
        ent_rad.delete(0, 'end')
        lbl_res_value.config(text="")
        ent_rad.focus()
        
    
    ent_rad.bind("<KeyRelease>", areaCalculate)
    
    ent_rad.focus()

    btn_clear.config(command=clear)
    

if __name__ == "__main__":
    main()


