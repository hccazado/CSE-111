# Each value in the people dictionary is a list. These
# are the indexes of the elements in those lists.
NAME_INDEX = 0
GENDER_INDEX = 1
BIRTH_YEAR_INDEX = 2
DEATH_YEAR_INDEX = 3

# Each value in the marriages dictionary is a list.
# These are the indexes of the elements in those lists.
HUSBAND_KEY_INDEX = 0
WIFE_KEY_INDEX = 1
WEDDING_YEAR_INDEX = 2


def main():
    people_dict = {
        # Each item in the people dictionary is a key value pair.
        # Each key is a unique identifier that begins with the
        # letter "P". Each value is a list of data about a person.
        # Each item in the dictionary is in this format:
        # person_key: [name, gender, birth_year, death_year]
        "P143": ["Lola Park", "F", 1663, 1706],
        "P338": ["Savanna Foster", "F", 1674, 1723],
        "P201": ["Tiffany Hughes", "F", 1689, 1747],
        "P203": ["Ignacio Torres", "M", 1693, 1758],
        "P128": ["Yasmin Li", "F", 1701, 1716],
        "P342": ["Trent Ross", "M", 1705, 1757],
        "P202": ["Samyukta Nguyen", "M", 1717, 1774],
        "P132": ["Joel Johnson", "M", 1724, 1800],
        "P445": ["Whitney Nelson", "F", 1757, 1823],
        "P318": ["Khalid Ali", "M", 1759, 1814],
        "P317": ["Davina Patel", "F", 1775, 1860],
        "P313": ["Enzo Ruiz", "M", 1782, 1782],
        "P475": ["Lauren Smith", "F", 1800, 1802],
        "P455": ["Lucas Ross", "M", 1800, 1853],
        "P435": ["Jamal Gray", "M", 1810, 1831],
        "P204": ["Fatima Soares", "F", 1812, 1898],
        "P206": ["Ephraim Foster", "M", 1831, 1885],
        "P500": ["Peter Price", "M", 1832, 1878],
        "P207": ["Rosalina Jimenez", "F", 1875, 1956],
        "P425": ["Rachel Johnson", "F", 1876, 1940],
        "P121": ["Vanessa Bennet", "F", 1880, 1960],
        "P152": ["Jose Castillo", "M", 1884, 1931],
        "P205": ["Liam Myers", "M", 1902, 1950],
        "P465": ["Isabella Lopez", "F", 1907, 1959],
        "P168": ["Megan Anderson", "F", 1909, 1945]
    }

    marriages_dict = {
        # Each item in the marriages dictionary is a key value pair.
        # Each key is a unique identifier that begins with the
        # letter "M". Each value is a list of data about a marriage.
        # Each item in the dictionary is in this format:
        # marriage_key: [husband_key, wife_key, wedding_year]
        "M48": ["P203", "P201", 1711],
        "M45": ["P342", "P338", 1722],
        "M36": ["P203", "P201", 1724],
        "M47": ["P202", "P445", 1774],
        "M21": ["P132", "P445", 1775],
        "M59": ["P132", "P317", 1792],
        "M63": ["P318", "P445", 1804],
        "M12": ["P318", "P317", 1808],
        "M54": ["P435", "P204", 1830],
        "M34": ["P455", "P204", 1853],
        "M55": ["P500", "P317", 1859],
        "M52": ["P206", "P204", 1875],
        "M78": ["P152", "P121", 1905],
        "M50": ["P152", "P425", 1917],
        "M64": ["P205", "P465", 1925],
        "M62": ["P152", "P207", 1925],
        "M70": ["P152", "P168", 1928]
    }

    # Call the print_death_age function to print
    # each person's name and age at death.
    print_death_age(people_dict)

    # Print a blank line.
    print()

    # Call the count_genders function to count
    # and print the number of males and females.
    count_genders(people_dict)

    # Print a blank line.
    print()

    # Call the print_marriages function to print
    # human readable data about the marriages.
    print_marriages(marriages_dict, people_dict)
    
    print()
    
    count_marriages(people_dict, marriages_dict)


def print_death_age(people_dict):
    """For each person in the people dictionary,
    print the person's name and age at death.

    Parameter
        people_dict: a dictionary that contains data about people
            Each item in the dictionary is in this format:
            person_key: [name, gender, birth_year, death_year]
    Return: nothing
    """
    
    print("Ages at death:")
    
    for key, values in people_dict.items():
        
        p_name = values[NAME_INDEX]
        p_yob = values[BIRTH_YEAR_INDEX] 
        p_age_of_death = values[DEATH_YEAR_INDEX] - p_yob
        
        print(f"{p_name:16}: Birth: {p_yob} - {p_age_of_death} years")    


def count_genders(people_dict):
    """Count and print the number of males
    and females in the people dictionary.

    Parameter
        people_dict: a dictionary that contains data about people
            Each item in the dictionary is in this format:
            person_key: [name, gender, birth_year, death_year]
    Return: nothing
    """
    
    #Defining and starting a counter for each gender
    male = 0
    female = 0
    
    #Iterating the entire dictionary
    for key, values in people_dict.items():
        gender = values[GENDER_INDEX]
        
        if gender == "M":
            male += 1
            
        else:
            female += 1
        
    print("==========================")
    print(f"Female: {female} \nMale:   {male}")
    print("==========================")
    
        
def print_marriages(marriages_dict, people_dict):
    """For each marriage in the marriages dictionary, print
    the husband's name, his age at wedding, the wedding year,
    the wife's name, and her age at wedding.

    Parameters
        marriages_dict: a dictionary that contains data about
            marriages. Each item in the dictionary is in this format:
            marriage_key: [husband_key, wife_key, wedding_year]
        people_dict: a dictionary that contains data about people
            Each item in the dictionary is in this format:
            person_key: [name, gender, birth_year, death_year]
    Return: nothing
    """
    
    marriages_count = []
    
    for key, values in marriages_dict.items():
        marriage_data = values
        HUSBAND_ID = values[HUSBAND_KEY_INDEX]
        WIFE_ID = values[WIFE_KEY_INDEX]
        husband_data = people_dict[HUSBAND_ID]
        wife_data = people_dict[WIFE_ID]

        husband_marriage_age = marriage_data[WEDDING_YEAR_INDEX] - husband_data[BIRTH_YEAR_INDEX]
        husband_name = husband_data[NAME_INDEX]
        
        wife_marriage_age = marriage_data[WEDDING_YEAR_INDEX] - wife_data[BIRTH_YEAR_INDEX]
        wife_name = wife_data[NAME_INDEX]
        
        marriage_year = marriage_data[WEDDING_YEAR_INDEX]
        
        print(f"Marriage Year: {marriage_year} - Husband: {husband_name:15} age: {husband_marriage_age}. Wife: {wife_name:15} age: {wife_marriage_age}")
    

def count_marriages(people_dict, marriages_dict):
    """Add a new column into people dictionary, which will contain
    the number of marriages of each person. then will print the name
    of each person and its own counter of marriages
    Parameters:
    people_dict: People dictionary
    marriages_dict: marriages dictionary which will provide the times of each person marriage"""
    
    print("Marriage counter")
    
    #adding a new parameter into the list of values of each item of people dictionary
    for key, values_list in people_dict.items():
        values_list.append(0)
        
    MARRIAGE_COUNT_INDEX = 4
    
    #iterrating each entry of marriage dictionary to increment the number of marriages of each married person
    #getting the id of the current husband to increment its marriage counter
    for key, values_list in marriages_dict.items():
        husband_key = values_list[HUSBAND_KEY_INDEX]
        wife_key = values_list[WIFE_KEY_INDEX]
        
        #incrementing the marriage counter into each person of the marriage dictionary (husbands)
        husband_values = people_dict[husband_key]
        husband_values[MARRIAGE_COUNT_INDEX] += 1
        
        #incrementing the marriage counter of each wife in the marriage dictionary
        wife_values = people_dict[wife_key]
        wife_values[MARRIAGE_COUNT_INDEX] += 1
    
    #Printing name and marriage counter for each person of the people dictionary
    for key, person_values in people_dict.items():
        name = person_values[NAME_INDEX]
        marriages = person_values[MARRIAGE_COUNT_INDEX]
        
        print(f"Name: {name:15}, Marriages: {marriages}")
    
    

# If this file was executed like this:
# > python teach_solution.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()
