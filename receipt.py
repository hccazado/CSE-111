#Program written by Heitor Cazado for CSE-111 BYU-I Prove assignment W9-W10
#This program open and reads the entries from a "products.csv" file into a 
#compound dictionary, and the product numbers are used as keys. 
#Finally the program will open and read a "request.csv", skip the first line which 
#contains column headings, then will search into the products dictionary the items from this file.

import csv
from datetime import datetime

#Default Variables
PRODUCT_NUMBER_IDX = 0
PRODUCT_NAME_IDX = 1
PRODUCT_PRICE_IDX = 2
FILENAME = "products.csv"

REQUEST_PROD_ID = 0
REQUEST_QTY = 1

TAX_RATE = 0.06

STORE = "Tatakua - South's Groceries"

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """

    products_dictionary = {}

    #Opening the file in with open block for auto closing the file aft its reading
    try:
        with open(filename, "rt") as file:
            #reading the file with python's builtin module csv
            reader = csv.reader(file)
            #skipping file's first line since it contains column headings
            next(reader)
            #iterating each line of the file
            for line in reader:
                key = line[PRODUCT_NUMBER_IDX]

                products_dictionary[key] = line
            
            return products_dictionary
    #File not found exception
    except FileNotFoundError as file_err:
        print("Error: missing file")
        print(file_err)
        
def sale_tax (subtotal):
    """compute a sale tax based on provided tax rate.
    Parameters:
    subtotal: amount bought
    tax: current tax rate
    
    Returns: amount of tax"""
    
    return subtotal * TAX_RATE

def compute_total(subtotal, tax):
    """compute sale's total.
    Parameters:
    subtotal: amount bought
    tax: tax for the sale
    
    Returns: purchase total value"""
    
    return (subtotal+tax)

def current_time():
    """return the current date and time formated as: weekday month day hour:minute:seconds year
    Parameters: none
    Returns: formated current date and time"""
    
    current_dt = datetime.now().strftime("%c")
    return current_dt
    
def discount_day(subtotal):
    """return total of discount if purchase day is Tuesday of Wednesday.
    Parameters:
    subtotal: purchase's subtotal amount
    
    Returns:
    amount of discount"""
    
    #getting current weekday as number in text format
    weekday = datetime.now().strftime("%w")
    
    #verifying weekday for Tuesday and wednesday numbers respectively
    if weekday == "2" or weekday == "3":
        #computing a 10% off discount on subtotal
        discount = subtotal * 0.1

        return discount
    
    else:
        return 0
    
def invite_survey(total):
    """Prints an invitation for the customer who purchased 50 or more dollars to complete an online survey.
    Parameters:
    total: purchase total amount
    returns: nothing
    """
    
    if total >= 50:
        print("\nWe are willing to hear about your experience buying with us. Please, participate from our online survey.")
        print("https://www.byupathway.org/")
        
        

def main():
    products_dict = read_dictionary(FILENAME, PRODUCT_NUMBER_IDX)
    num_items = 0
    subtotal = 0.0
    sales_tax = 0.0
    total = 0.0
    discount = 0.0
    formated_time = current_time()

    print(f"{STORE:^40}")
    print()

    try:
        with open("request.csv", "rt") as request_file:
            reader = csv.reader(request_file)
            #skipping first line since it correponds to column headings
            next(reader)
            
            #reading each file's line with csv reader
            for line in reader:
            #getting number of requested product and quantity of the requested product
                req_product = line[PRODUCT_NUMBER_IDX]
                req_quantity = int(line[REQUEST_QTY])

                #retrieving values for current requested product from products_dict        
                cur_product = products_dict[req_product]
                
                #retrieving name and price from returned product
                name = cur_product[PRODUCT_NAME_IDX]
                price = float(cur_product[PRODUCT_PRICE_IDX])
                
                #adding current item to subtotal account
                subtotal += req_quantity * price
                
                #incrementing quantity of purchased items
                num_items += req_quantity
                
                #printing requested item, quantity and price per unit
                print(f"{name:15}: Req. Qty: {req_quantity:3} @ {price}US$")
            
            #computing any available discount
            discount = discount_day(subtotal)
            
            #verifying if any discount was applied
            if discount > 0: 
                #getting sale's tax
                sales_tax = sale_tax((subtotal - discount))
                #computing sale total amount
                total = compute_total((subtotal - discount), sales_tax)
                
                print()
                print(f"Number of Items: {num_items:<20}")
                print(f"Subtotal: {subtotal:^20.2f}")
                print(f"Discount: {discount:^19.2f}")
                print(f"Sales Tax: {sales_tax:>10.2f}")
                print(f"Total: {total:>15.2f}")
                print()
                print(f"Thank you for buying at {STORE}")
                print(formated_time)
                
                invite_survey(total)
            
            else:
                #getting sale's tax
                sales_tax = sale_tax(subtotal)
                #computing sale total amount
                total = compute_total(subtotal, sales_tax)
                
                print()
                print(f"Number of Items: {num_items:<20}")
                print(f"Subtotal: {subtotal:^20.2f}")
                print(f"Sales Tax: {sales_tax:>10.2f}")
                print(f"Total: {total:>15.2f}")
                print()
                print(f"Thank you for buying at {STORE}")
                print(formated_time)
                
                invite_survey(total)
                
    #requested product key not found on products dictionary
    except KeyError as key_err:
        print(f"Error: unknown product ID: {key_err} in the request.csv file")
        
    #request.csv file not found on current working directory
    except FileNotFoundError as file_err:
        print("Error: missing file")
        print(file_err)



if __name__ == "__main__":
    main()