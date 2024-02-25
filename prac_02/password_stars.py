"""
get password
while len(password) < 5
    print("Letters must be greater than 4")
    get password

for i in range of len(password)
    print("*", end='')
"""

def main():
    password = get_password()
    for i in range(len(password)):
        print("*", end='')

def get_password():
    PASSWORD_MINIMAL_LENGTH = 4
    password = input("Password: ")
    while len(password) <= PASSWORD_MINIMAL_LENGTH:
        print("Letters must be greater than 4")
        password = input("Password: ")
    return password




