"""Super Auto Parking is a BYUI - CSE111 course final project.
Writing by Heitor Cazado. """

import tkinter as tk
from tkinter import Frame, Label, Button, Entry
import math
import datetime

def main ():
    """Main function will generate program's main GUI widget with tkinter.
    """
    #creating GUI root level
    root = tk.Tk()

    #creating main frame
    frm_main = Frame(root)
    frm_main.master.title("Super Auto Parking")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)
    
    popuplate_main_frame(frm_main)
    
    root.mainloop()

def popuplate_main_frame(frm_main):
    """Populate program's main frame with its widgets
    Parameter: frm-main - a tkinter frame object
    Return: nothing"""

    #widgets variables
    lbl_welcome = Label(frm_main, text="Welcome to Super Auto Parking App")
    lbl_license = Label(frm_main, text="License Plate:")
    lbl_cost_msg = Label(frm_main, text="Debt :")
    lbl_price = Label(frm_main, width=2)
    
    ent_license = Entry(frm_main)

    btn_park = Button(frm_main, text="Park")
    btn_clr = Button(frm_main, text="Clear")

    #Placing widgets
    lbl_welcome.grid(row=0, column=0, columnspan=4)
    lbl_license.grid(row=1, column=0, padx=3, pady=3)
    ent_license.grid(row=1, column=1, padx=3, pady=3)
    lbl_cost_msg.grid(row=2, column=0, columnspan=3, padx=3, pady=3)
    lbl_price.grid(row=2, column=1, padx=3, pady=3)

    btn_park.grid(row=3, column=0, padx=3, pady=3)



if __name__ == "__main__":
    main()


