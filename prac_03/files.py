# 1
"""
out_file = open file.txt as write
get name
out_file.write(name)
outfile.close()
"""
out_file = open("file.txt", "w")
name = input("Name: ")
out_file.write(name)
out_file.close()

#2
"""
in_file = open file.txt as readonly
name = in_file.read().strip()
in_file.close()
print(f"Your name is {name}")
"""
in_file = open("file.txt", "r")
name = in_file.read().strip()
in_file.close()
print(f"Your name is {name}")

#3
"""
in_file = open numbers.txt as readonly
number1 = int(in_file.readline())
number2 = int(in_file.readline())
in_file.close()
print(number1 + number2)
"""
in_file = open("numbers.txt", "r")
number1 = int(in_file.readline())
number2 = int(in_file.readline())
in_file.close()
print(number1 + number2)

#4
"""
in_file = open numbers.txt as readonly
total = 0
for line in in_file
    number = int(line)
    total += number
in_file.close()
print(total)
"""
in_file = open("numbers.txt", "r")
total = 0
for line in in_file:
    number = int(line)
    total += number
in_file.close()
print(total)