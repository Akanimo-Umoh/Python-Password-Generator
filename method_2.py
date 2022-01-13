import random
import string

upper_case = string.ascii_uppercase
lower_case = string.ascii_lowercase
numbers = string.digits
symbols = string.punctuation

password = upper_case + lower_case + numbers + symbols
password_generator = []
password_generator.extend(password)

while True:
    password_length = int(input("Enter password length: "))
    password_count = int(input("How many passwords would you like?: "))
    for x in range(0, password_count):
        password = ""
        for x in range(0, password_length):
            password_characters = random.choice(password_generator)
            password = password + password_characters
        print ("Here is your password: ", password)