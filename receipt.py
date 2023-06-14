#Program written by Heitor Cazado for CSE-111 BYU-I Prove assignment W9-W10
#This program open and reads the entries from a "products.csv" file into a 
#compound dictionary, and the product numbers are used as keys. 
#Finally the program will open and read a "request.csv", skip the first line which 
#contains column headings, then will search into the products dictionary the items from this file.

import csv

#Default Variables
PRODUCT_NUMBER_IDX = 0
PRODUCT_NAME_IDX = 1
PRODUCT_PRICE_IDX = 2
FILENAME = "products.csv"

REQUEST_PROD_ID = 0
REQUEST_QTY = 1

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
    with open(filename, "rt") as file:
        #reading the file with python's builtin module csv
        reader = csv.reader(file)

        #iterating each line of the file
        for line in reader:
            key = line[PRODUCT_NUMBER_IDX]

            products_dictionary[key] = line

    return products_dictionary

def main():
    products_dict = read_dictionary(FILENAME, PRODUCT_NUMBER_IDX)

    print(products_dict)

    with open("request.csv", "rt") as request_file:
        reader = csv.reader(request_file)
        #skipping first line since it correponds to column headings
        next(reader)
        
        #reading each file's line with csv reader
        for line in reader:
           #getting number of requested product and quantity of the requested product
           req_product = line[PRODUCT_NUMBER_IDX]
           req_quantity = line[REQUEST_QTY]

           #retrieving values for current requested product from products_dict        
           cur_product = products_dict[req_product]
           
           #retrieving name and price from returned product
           name = cur_product[PRODUCT_NAME_IDX]
           price = cur_product[PRODUCT_PRICE_IDX]

           print(f"Product: {name:15} - Req. Qty: {req_quantity:3} - Price: {price}")




if __name__ == "__main__":
    main()