import csv


# Each row in the pupils.csv file contains three elements.
# These are the indexes of the elements in each row.
GIVEN_NAME_INDEX = 0
SURNAME_INDEX = 1
BIRTHDATE_INDEX = 2


def read_compound_list(filename):
    """Read the text from a CSV file into a compound list.
    The compound list will contain small lists. Each small
    list will contain the data from one row of the CSV file.

    Parameter
        filename: the name of the CSV file to read.
    Return: the compound list
    """
    # Create an empty list.
    compound_list = []

    # Open the CSV file for reading.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(csv_file)

        # The first line of the CSV file contains column headings
        # and not a student's I-Number and name, so this statement
        # skips the first line of the CSV file.
        next(reader)

        # Process each row in the CSV file.
        for row in reader:

            # Append the current row at the end of the compound list.
            compound_list.append(row)

    return compound_list

def print_list(new_list):
    """Receives a list as paramater and print each line in a new line"""
    
    for item in new_list:
        print(item)
        


        
def main():
    sort_age = lambda person: person[BIRTHDATE_INDEX]
    
    sort_name = lambda person: person[GIVEN_NAME_INDEX]
    
    sort_birth_month_day = lambda person: str(person[BIRTHDATE_INDEX][5:10])
    
    try:
    
        pupils_list = read_compound_list("pupils.csv")
        
        print_list(pupils_list)
        
        print("List sorted by age, oldest to youngest\n")
        
        sorted_pupils = sorted(pupils_list, key=sort_age)
        
        print_list(sorted_pupils)
        
        print("Sorting pupils by given name\n")
        
        sorted_pupils = sorted(pupils_list, key=sort_name)
        
        print_list(sorted_pupils)
        
        print("Sorting pupils by month and day of birth\n")
        
        sorted_pupils = sorted(pupils_list, key=sort_birth_month_day)
        
        print_list(sorted_pupils)
    
    except(FileNotFoundError, PermissionError) as error:
        print(type(error).__name__, error, sep=":")
        
    

if __name__ =="__main__":
    main()