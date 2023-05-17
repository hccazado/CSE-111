#Team activity. The application should receive the subtotal,
#and get the day of the week, if it's case of being Tuesday or Wednesday
#the program mus apply 10% of discount on customer's subtotal.

from datetime import datetime

current_time = datetime.now()
day = current_time.weekday()
print(day)

subtotal = float(input("Type the subtotal: "))

if day == 1 or day == 2:
    
    if subtotal >= 50:
        discount =  subtotal * 10/100
        tax = (subtotal - discount) * 6 /100
        total = subtotal - discount + tax
        print(f"Your total with {discount} of discount, plus 6% of taxes is US$ {total:0.2f}")
        
        
    else:
        difference = 50 - subtotal
        print(f"You need to buy more ${difference:0.2f} in order to receive the discount")
    
tax = subtotal * 6 /100
total = subtotal + tax
print(f"Your total with 6% of taxes is US$ {total:0.2f}")