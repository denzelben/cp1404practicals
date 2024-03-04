"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""

"""
function main()
    incomes = empty list
    get total_months
    
    for month in range from 1 to total_months + 1
        get income as float
        incomes.append(income)
    function print_report(incomes, total_months)
    
function print_report(incomes, total_months)
    print("\nIncome Report\n-------------")
    total = 0
    for month in range from 1 to total_months + 1
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))

function main()
"""

def main():
    """Display income report for incomes over a given number of total_months."""
    incomes = []
    total_months = int(input("How many months? "))

    for month in range(1, total_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)
    print_report(incomes, total_months)


def print_report(incomes, total_months):
    #prints report
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, total_months + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()