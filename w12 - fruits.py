def main():
    try:
        # Create and print a list named fruit.
        fruit_list = ["pear", "banana", "apple", "mango"]
        print(f"original: {fruit_list}")
        
        #reverse and print fruits list.
        fruit_list.reverse()
        print(f"Reverse: {fruit_list}")
        
        #add orange at the end of the list
        fruit_list.append("orange")
        print(f"added orange: {fruit_list}")
        
        #finding apple and inserting cherry before
        #using lambda
        #fruit_index = lambda fruits, fruit : fruits.index(fruit)
        #fruit_list.insert(fruit_index(fruit_list, "apple"), "cherry")
        
        #normal way
        frt_idx = fruit_list.index("apple")
        fruit_list.insert(frt_idx, "cherry")
        print(f"cherry before apple: {fruit_list}")
        
        #removing banana from the list
        fruit_list.remove("banana")
        print(f"banana removed: {fruit_list}")
        
        #poping list's last element
        fruit_list.pop()
        print(f"poping last element: {fruit_list}")
        
        #sorting fruits list
        fruit_list.sort()
        print(f"sorted list: {fruit_list}")
        
        #cleaning the list
        fruit_list.clear()
        print(f"cleared list: {fruit_list}")
        
        print("Bye!")
    except IndexError as e:
        print(type(e).__name__, e, sep=": ")
if __name__ == "__main__":
    main()