"""
function main()
    print menu
    choice = get_input(">>> ").upper()
    while choice != Q
        outcome = function validate_choice(choice)
        print(outcome)
        print(MENU)
        choice = get_input(">>> ").upper()
    print("Thank you.")

function get_input(string)
    choice = input(string)
    return choice

function validate_choice(choice)
    if choice == C
        celsius = get_input("Celsius: ")
        fahrenheit = int(celsius) * 9 / 5 + 32  # converting Celsius to Fahrenheit
        return f"Result: {fahrenheit:.2f} F"
    else if choice == F
        fahrenheit = get_input("Fahrenheit: ")
        celsius = 5 / 9 * (int(fahrenheit) - 32)  # converting Fahrenheit to Celsius
        return f"Result: {celsius:.2f} C"
    else
        return "Invalid option"


function main()
"""
MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
def main():
    print(MENU)
    choice = get_input(">>> ").upper()
    while choice != "Q":
        outcome = validate_choice(choice)
        print(outcome)
        print(MENU)
        choice = get_input(">>> ").upper()
    print("Thank you.")
def get_input(string):
    choice = input(string)
    return choice

def validate_choice(choice):
    if choice == "C":
        celsius = get_input("Celsius: ")
        fahrenheit = int(celsius) * 9 / 5 + 32  # converting Celsius to Fahrenheit
        return f"Result: {fahrenheit:.2f} F"
    elif choice == "F":
        fahrenheit = get_input("Fahrenheit: ")
        celsius = 5 / 9 * (int(fahrenheit) - 32)  # converting Fahrenheit to Celsius
        return f"Result: {celsius:.2f} C"
    else:
        return "Invalid option"


main()