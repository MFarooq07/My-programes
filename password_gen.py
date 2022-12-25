"""
Description: The following program generates a password of a length specified by a user

Created by: Muhammad Farooq Memon
Role: Student
Institute: Union College
"""
# The following program generates a password of a length specified by the user
import random

MIN_LENGTH = 3
special_char = ["~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", ",", "_", "-", "+", "=", "{", "}"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
letters = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w",
    "x",
    "y", "z"]

pass_bank = [special_char, letters, numbers]


def gen_password():
    """
    The following function generates a password of a specific length LEN_PASSWORD
    :return: generates a password of length LEN_PASSWORD
    """
    password = ""
    for char in range(0, LEN_PASSWORD):
        password_char_type = random.choice(pass_bank)
        password = password + random.choice(password_char_type)
    return password


def is_pass_strong(password):
    """
    Checks whether the password created is strong enough
    :param password: generated password
    :return: True or False based on the inclusion of all letter, numbers and Special Characters
    """
    if letter_in_pass(password) and numbers_in_pass(password) and special_char_in_pass(password):
        return True
    else:
        return False


def letter_in_pass(password):
    """
    Checks if there is at least one character in the generated password
    :param password: generated password
    :return: True or false based on the presence of at least one letter
    """
    for letter in letters:
        for char in password:
            if letter == char:
                return True
    return False


def numbers_in_pass(password):
    """
    Checks if there is at least one number in the generated password
    :param password: generated password
    :return: True or false based on the presence of at least one number
    """

    for number in numbers:
        for char in password:
            if number == char:
                return True
    return False


def special_char_in_pass(password):
    """
    Checks if there is at least one special character in the generated password
    :param password: generated password
    :return: True or false based on the presence of at least one special character
    """

    for s_char in special_char:
        for char in password:
            if s_char == char:
                return True
    return False


LEN_PASSWORD = int(input("Please enter the length of the password you desire to have: "))
while LEN_PASSWORD < MIN_LENGTH:
    LEN_PASSWORD = int(input("Please enter the length of the password you desire to have: "))

password = gen_password()
strong_password = is_pass_strong(password)
while not strong_password:
    password = gen_password()
    strong_password = is_pass_strong(password)

print("password is: " + password)
