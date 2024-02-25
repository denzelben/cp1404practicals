"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

"""
get sales
while sales >= 0
    if sales < 1000
        bonus = sales * 0.1
    else
        bonus = sales * 0.15
    print bonus
    get sales
do next thing
"""

MINIMUM_SALES = 0
BONUS_THRESHOLD = 1000
BONUS_UNDER_THRESHOLD_MULTIPLIER = 0.1
BONUS_ABOVE_THRESHOLD_MULTIPLIER = 0.15

sales = float(input("Enter sales: $"))
while sales >= MINIMUM_SALES:
    if sales < BONUS_THRESHOLD:
        bonus = sales * BONUS_UNDER_THRESHOLD_MULTIPLIER
    else:
        bonus = sales * BONUS_ABOVE_THRESHOLD_MULTIPLIER
    print(int(bonus))
    sales = float(input("Enter sales: $"))
