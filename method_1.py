import random
import string

def password_generator():
    upper_case = string.ascii_uppercase
    lower_case = string.ascii_lowercase
    numbers = string.digits
    symbols = string.punctuation

    # add characters to a new variable
    password = upper_case + lower_case + numbers + symbols

    # create an empty list
    password_generator = []

    # add password to the list
    password_generator.extend(password)

    # shuffle password list
    random.shuffle(password_generator)

    # get password length from user
    password_length = int(input("Enter your password length: "))

    # convert password list to string from index 0 to password length
    generate_password = "".join(password_generator[0 : password_length])

    # print password generated
    print ("You password is: ", generate_password)

# call the password_generator function
password_generator()