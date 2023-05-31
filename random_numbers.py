#Teach team activity for W7. working with lists. And practicing pass by reference 
#and pass by value

import random

def append_random_numbers(numbers_list, quantity = 1):
    """Append random numbers into the referred numbers list.
    Parameter:
        numbers_list: A list of numbers where the function will append the random number
        quantity: defines how many times a random number will be append into the referred list
    Return: nothing."""
    i=0
    while i < quantity:
        new_number = random.uniform(10,90)
        new_number = round(new_number,1)
        numbers_list.append(new_number)
        i += 1
    
def append_random_words (words_list, quantity = 1):
    """Append random words into the referred words list.
    Parameter:
        words_list: A list of words where the function will append the random choose word
        quantity: defines how many times a random word will be append into the referred list
    Return: nothing."""
    
    words = ["love", "God", "heaven", "attonement", "church", "friend", "cloud", "head", "hand", "eye"]
    for _ in range(quantity):
        random_word = random.choice(words)
        words_list.append(random_word)

def main():
    numbers = [16.2, 75.1, 52.3]
    words = []
    print(numbers)
    append_random_numbers(numbers)
    print (numbers)
    
    append_random_numbers(numbers,2)
    print(numbers)
    
    append_random_words(words)
    print(words)
    append_random_words(words, 3)
    print(words)
    

if __name__ == "__main__":
    main()