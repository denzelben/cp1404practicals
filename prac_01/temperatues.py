"""
print menu
get choice on uppercase
while choice != Q
    if choice == C
        get celsius
        fahrenheit = celsius * 9 / 5 + 32
        print(f"Result: {fahrenheit:.2f} F")
    else if choice == F
        get fahrenheit
        celsius = 5 / 9 * (fahrenheit - 32)
        print(f"Result: {celsius:.2f} C")
    else
        print("Invalid option")
    print menu
    get choice on uppercase
print("Thank you.")
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9 / 5 + 32  # converting Celsius to Fahrenheit
        print(f"Result: {fahrenheit:.2f} F")
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit : "))
        celsius = 5 / 9 * (fahrenheit - 32)  # converting Fahrenheit to Celsius
        print(f"Result: {celsius:.2f} C")
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")