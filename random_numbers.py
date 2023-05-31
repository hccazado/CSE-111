#Teach team activity for W7. working with lists. And practicing pass by reference 
#and pass by value

import random

def append_random_numbers(numbers_list, quantity = 1):
    i=0
    while i < quantity:
        new_number = random.uniform(10,90)
        new_number = round(new_number,1)
        numbers_list.append(new_number)
        i += 1
    
def append_random_words (words_list, quantity = 1):
    i = 0
    words = ["love", "God", "heaven", "attonement", "church", "friend", "cloud", "head", "hand", "eye"]
    while i < quantity:
        random_word = random.choice(words)
        words_list.append(random_word)
        i += 1

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
    

if "__main__" == "__main__":
    main()