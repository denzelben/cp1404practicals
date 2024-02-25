"""
for i in range from 1 to 20 with 2 steps
    print i with spacing
print()

for i in range from 0 to 100 with 10 steps
    print i with spacing
print()

for i in range from 20 to 0 with -1 steps
    print i with spacing
print()

get number_of_stars
for i in range of number_of_stars
    print * with no spacing
print()
"""


for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 101, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

number_of_stars = int(input("Number of stars: "))
for i in range(number_of_stars):
    print("*", end='')
print()