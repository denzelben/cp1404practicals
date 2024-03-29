"""
CP1404/CP5632 Practical
Data file -> lists program
"""
"""
function main()
    datas = function get_data()
    function print_data(datas)
    
function get_data()
    datas = empty list
    input_file = open(subject_data.txt)
    for line in input_file
        print(line)
        print(repr(line))
        line = line.strip()
        parts = line.split(',')
        print(parts)
        parts[2] = int(parts[2])
        print(parts)
        print("----------")
        datas.append(parts)
    input_file.close()
    return datas
    
function print_data(datas)
    for data in datas
        print(f"{data[0]} is taught by {data[1]:12} and has {data[2]:3} students")
        
function main()
"""
FILENAME = "subject_data.txt"


def main():
    datas = get_data()
    print_data(datas)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    datas = []
    input_file = open(FILENAME)
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        print("----------")
        datas.append(parts)
    input_file.close()
    return datas

def print_data(datas):
    for data in datas:
        print(f"{data[0]} is taught by {data[1]:12} and has {data[2]:3} students")

main()