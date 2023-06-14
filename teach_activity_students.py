#DEFAULT VARIABLES
import csv

ILEARN_INDEX = 0
FILENAME = "students.csv"
NAME_INDEX = 1

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
    
    students_list = {}
        
    with open(filename) as file:
        
        #opening a reader with csv
        reader = csv.reader(file)
        
        next(reader)
        
        for row in reader:
            key = row[0]
            students_list[key] = row
            
    return students_list

def search_student(students, ilearn):
        
    ilearn = ilearn.replace("-", "")
        
    ilearn = ilearn.replace(".", "")
    
    if len(ilearn) > 11: 
        return "Invalid I-Learn. Too many digits"
    
    elif len(ilearn) < 9: 
        return "Invalid I-learn. Too few digits"
    
                
    if ilearn in students:
        name = students[ilearn]
        
        name = name[NAME_INDEX]
        
        return name
    
    else: 
        return "No Such Student"
    
def main():
    students_list = read_dictionary(FILENAME, ILEARN_INDEX)
    
    search = input("Type an I-Learn number (XX-XX-XXXX): ")
    
    result = search_student(students_list, search)
    
    print(result)
    

if __name__ == "__main__":
    main()