"""
function main()
    print menu
    choice = function get_input("Choice: ").upper()
    while choice != Q
        if choice == G
            score = int(function get_input("Score: ")
        else if choice == P
            grade = function check_score(score)
            print(grade)
        else if choice == S
            for i in range of score
                print("*", end='')
            print()
        else
            print("Invalid option")

function get_input(string)
    answer = input(string)
    return answer

function check_score(score):
    if score >= 90
        return("Excellent")
    else if score >= 50
        return("Pass")
    else
        return("Bad")

main()
"""


MENU ="""(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""
def main():
    print(MENU)
    choice = get_input("Choice: ").upper()
    while choice != "Q":
        if choice == "G":
            score = int(get_input("Score: "))
        elif choice == "P":
            grade = check_score(score)
            print(grade)
        elif choice == "S":
            for i in range(score):
                print("*", end='')
            print()
        else:
            print("Invalid option")
        print(MENU)
        choice = get_input("Choice: ").upper()

def get_input(string):
    answer = input(string)
    return answer

def check_score(score):
    EXCELLENT_SCORE = 90
    PASSING_SCORE = 50
    if score >= EXCELLENT_SCORE:
        return("Excellent")
    elif score >= PASSING_SCORE:
        return("Pass")
    else:
        return("Bad")

main()