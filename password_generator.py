# Importing the necessary libraries
from random import randint

# Generating password based off the length given
def generate_password(l):
    password = ""
    for i in range(l):
        x  = randint(33, 126)
        password = password + chr(x)
    return password

# Running the script
if __name__ == "__main__":
    length = int(input("please type the length of your password : "))
    print(generate_password(length))