#This program will read the text file provinces.txt 
#on its same folder. Following, the program will remove
#the first and last element from the returned list. Also,
#the program will replace all occurrences of "AB" with "Alberta".
#The program will also count and print the number of elements "Albberta".

from collections import Counter

#DEFAULT VARIABLES
FILENAME = "provinces.txt"
OCCURRENCE = "AB"
NEW_VALUE = "Alberta"

def get_list_from_file (filename):
    """Read all the lines from the file into a new list
    Parameters:
    filename: name of the file which will be readed
    
    Return:
    A list with file's entries"""
    
    provinces_list = []
    
    #Opening the informed file with "with open" this way the file is automatically closed
    with open("provinces.txt") as file:
        #adding each line of the file at the of provinces_list
        for line in file:
            #strip the line (cleans charactes such as like "\n" at the of the line)
            clean_line = line.strip()
            
            provinces_list.append(clean_line)
            
        else:
            print("Reading file done.")
            
    return provinces_list

def remove_first_entry (provinces):
    """Removes the first entry from parameter's list
    Parameters:
    provinces: A list with Canadian provinces
    Returns: Nothing since the parameter provinces list is passed through reference
    """
    
    provinces.pop(0)
    
def remove_last_entry (provinces):
    """Removes the last entry from parameter's list
    Parameters:
    provinces: A list with Canadian provinces
    Returns: Nothing since the parameter provinces list is passed through reference
    """
    
    #without parameter, the method pop has -1 as default value which indicates the index of the last item
    provinces.pop()
    
def replace_occurrence (provinces, occurence, new_value):
    """Looks for the occurrence in the provided list then replace the occurrence with the new_value
    Parameters:
    provinces: A list with Canadian provinces
    occurence: The occurance which will be replaced new value
    new_value: The new value that will replace the informed occurrence
    Returns: Nothing since the parameter provinces list is passed through reference
    """
    
    #iterating through each element, and using i as index to accees current element and replace its value as necessary
    for i in range(len(provinces)):
        if provinces[i] == occurence:
            provinces[i] = new_value
            
def get_occurrences (provinces, occurrence):
    """returns how many a times a occurrence is found in the passed list
    Parameters:
    provinces: A list with Canadian provinces
    occurence: The occurrence that will be looked for
    Returns: total times the occurrence has been found on the list"""
    
    #counting the occurance of each element using Collections module   
    counting = Counter(provinces)
    
    #counting2 = 0
    #counting the occurrence in traditional way
    #for i in range(len(provinces)):
    #    if provinces[i] == "Alberta":
    #        counting2 += 1

    #return counting2 
    
    #this list method also works
    #counting2 = provinces.count(occurrence)
    
    #returning the value of the dictionary for the key occurrence
    return counting[occurrence]
    
    
    
def main ():
    """Main function that will execute if file is executed rather than imported into a testing procedure"""
    
    #obtaining the list of provinces
    canadian_provinces = get_list_from_file(FILENAME)
    
    #removing first element from the list
    remove_first_entry(canadian_provinces)
    
    #removing last element from the list
    remove_last_entry(canadian_provinces)
    
    #replacing occurences of AB with Alberta
    replace_occurrence(canadian_provinces, OCCURRENCE, NEW_VALUE)
    
    occurrences = get_occurrences(canadian_provinces, "Alberta")
    
    print (canadian_provinces)
    
    print(f"Alberta occurs {occurrences} times")
    
    
#Executing the main function in case the program is being executed rather than imported
if __name__ == "__main__":
    main()
    
    
    