"""
get number_of_items
while number_of_items < 1
    print("Invalid number of items!")
    get number_of_items

for i in range of number_of_items
    get price
    total_price += price

if total_price > 100
    total_price = total_price * 0.9

print(f"Total price for {number_of_items} is ${total_price:.2f}")
"""

MINIMUM_ITEMS = 1
DISCOUNT_THRESHOLD = 100
DISCOUNT = 0.9
total_price = 0

number_of_items = int(input("Number of items: "))
while number_of_items < MINIMUM_ITEMS:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

for i in range(number_of_items):
    price = float(input("Price of item: "))
    total_price += price

if total_price > DISCOUNT_THRESHOLD:
    total_price = total_price * DISCOUNT

print(f"Total price for {number_of_items} is ${total_price:.2f}")
