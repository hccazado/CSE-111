#This python program is a practice of invoking Python 
# built-in functions, and functions from standard Python module.

import math
items = int(input("Type the number of manufactured items: "))
packing = int(input("Type the number of items that the user will pack per box: "))

boxes = items / packing

boxes = math.ceil(boxes)

print(f"For {items} items, packing {packing} in each box, you will need {boxes} boxes.")

