import random
import string
import os

i = 1
while i < 6:
    letters_list = list(string.ascii_letters)
    numbers_list = list(string.digits)
    characters_list = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]

    os.system('cls' if os.name == 'nt' else 'clear')

    print("\nwelcome to PASSWORD GENERATOR\n")
    
    letters = input("How many letters do you want in your password?\n")

    numbers = input("How many numbers do you want in your password?\n")

    characters = input("How many symbols do you want in your password?\n")

    int_letters = int(letters)
    int_numbers = int(numbers)
    int_characters = int(characters)

    random_letters = random.sample(letters_list, int_letters)
    random_numbers = random.sample(numbers_list, int_numbers)
    random_characters = random.sample(characters_list, int_characters)

    password = random_letters + random_numbers + random_characters

    random.shuffle(password)

    print(f"Here is your generated password: {''.join(password)}")

    again = input("\nWould you like to generate a new password? (y/n)\n")
    if again.lower() == "y":
        i = 2
    elif again.lower() == "n":
        i = 7
        print("Thank you for using PASSWORD GENERATOR. See you soon! :)")