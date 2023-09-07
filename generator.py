import os
import string
import random
import colorama
from colorama import Fore, Style
from pyfiglet import Figlet

fig = Figlet(font='small')

colorama.init()

# Declare arrays of the avaliable caracters
lowercase_characters = list(string.ascii_lowercase)
upercase_characters = list(string.ascii_uppercase)
punctuation = list(string.punctuation)
digits = list(string.digits)

def clear_terminal():
    if os.name == 'posix':  # Linux
        os.system('clear')
    elif os.name == 'nt':  # Windows
        os.system('cls')
    else:
        print("The operating system could not be determined")

def main():
    # Ask the user to choose the number of characters
    # of each type they want in their password.
    num_lowers = int(input("How many lowercase characters do you want to? "))
    num_upers = int(input("How many upercase characters do you want to? "))
    num_punctuations = int(input("How many punctuation do you want to? "))
    num_digits = int(input("How many digits do you want to? "))

    pass_len = num_lowers + num_upers + num_punctuations + num_digits

    # Choose different types of characters according to the user's choice
    rand_lowers = random.choices(lowercase_characters, k = num_lowers)
    rand_uppers = random.choices(upercase_characters, k = num_upers)
    rand_punctuations = random.choices(punctuation, k = num_punctuations)
    rand_digits = random.choices(digits, k = num_digits)

    # List of characters to be in the password
    char_list = rand_lowers + rand_uppers + rand_punctuations + rand_digits

    # We shuffle the list of characters a certain number of times
    # to avoid patterns when generating the password
    Z = 3 if pass_len - 3 < 3 else pass_len - 3
    for _ in range(pass_len - len([x for x in range(1, Z)])):

        random.shuffle(char_list)

    print("Generated password: " + ''.join(char_list))

clear_terminal()
main()