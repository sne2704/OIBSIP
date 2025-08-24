import random
import string
print("Hello! ")
print()
ans=input("Do you need help in generating a new password (y/n)?\n")
if ans == "y":
    length = int(input("Enter password length: "))

    letters = input("Do you want letters in your password (y/n)? : \n")
    digits = input("Do you want digits in your password (y/n)? : \n")
    symbols = input("Do you want symbols in your password (y/n)? : \n")

#initializing characters and password
    characters = ""
    password = ""

    if letters == "y":
        characters += string.ascii_letters
    if digits == "y":
        characters += string.digits
    if symbols == "y":
        characters += string.punctuation

    if characters == "":
        print("You must select at least one character type!")
    else:
        for i in range(length):
            password = password + random.choice(characters)

    print("Your password is:\n", password)
else:
    print("Thank you")