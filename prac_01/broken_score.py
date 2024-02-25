"""
get score
while score < 0 or score > 100
    print("Invalid Score")
if score >= 90
    print("Excellent)
else if score >= 50
    print("Pass")
else
    print("Bad")
"""
MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
EXCELLENT_SCORE = 90
PASSING_SCORE = 50

score = float(input("Enter score: "))
while score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
    print("Invalid Score")
    score = float(input("Enter score: "))
if score >= EXCELLENT_SCORE:
    print("Excellent")
elif score >= PASSING_SCORE:
    print("Pass")
else:
    print("Bad")