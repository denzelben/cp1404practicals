"""
function main()
    get score
    while score < 0 or score > 100
        print("Invalid Score")
        get score
    grade = function check_score(score)
    print(grade)

function check_score(score)
    if score >= 90
        return("Excellent")
    else if score >= 50
        return("Pass")
    else
        return("Bad")

main()
"""

def main():
    MINIMUM_SCORE = 0
    MAXIMUM_SCORE = 100
    score = float(input("Enter score: "))
    while score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        print("Invalid Score")
        score = float(input("Enter score: "))
    grade = check_score(score)
    print(grade)
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