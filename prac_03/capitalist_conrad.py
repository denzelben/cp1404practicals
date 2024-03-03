"""
import random library
out_file = open(FILENAME, write only)

price = 10
day = 0
print(f"Starting price: ${price:,.2f}", file=out_file)

while 0.01 <= price <= 1000
    price_change = 0
    day += 1
    if random.randint(1,2) == 1
        price_change = random.uniform(0,0.1)
    else
        price_change = random.uniform(-0.05, 0)

    price *= (1 + price_change)
    print(f"On day {day} price is: ${price:,.2f}", file=out_file)

out_file.close()
"""


import random

MAX_INCREASE = 0.1
MAX_DECREASE = 0.05
MIN_PRICE = 0.01
MAX_PRICE = 1000.0
INITIAL_PRICE = 10.0
FILENAME = "stock_output.txt"

out_file = open(FILENAME, 'w')

price = INITIAL_PRICE
day = 0
print(f"Starting price: ${price:,.2f}", file=out_file)

while MIN_PRICE <= price <= MAX_PRICE:
    price_change = 0
    day += 1
    if random.randint(1, 2) == 1:
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)
    print(f"On day {day} price is: ${price:,.2f}", file=out_file)

out_file.close()