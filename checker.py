import math
import re

while True:
    print("Welcome to PASSWORD STRENGTH CHECKER!!\n")

    password = input("Please input your password:\n")

    if len(password) >= 8:
        print("Length ✅")
    else:
        print("Your password should be at least 8 characters long ❌")

    def check_password_strength(password: str) -> dict:
        length = len(password)
        if length == 0:
            return {"score": "Invalid", "entropy": 0.0, "feedback": "Empty password"}


    has_lower = int(bool(re.search(r"[a-z]", password)))
    has_upper = int(bool(re.search(r"[A-Z]", password)))
    has_digit = int(bool(re.search(r"[0-9]", password)))
    has_special = int(bool(re.search(r"[^a-zA-Z0-9]", password)))


    criteria_score = has_lower + has_upper + has_digit + has_special



    pool_size = 0
    if has_lower:
        pool_size += 26
    if has_upper:
        pool_size += 26
    if has_digit:
        pool_size += 10
    if has_special:
        pool_size += 32

    length = len(password)
    entropy = length * math.log2(pool_size) if pool_size > 0 else 0


    if entropy < 40:
        strength = "Weak 🔴"
    elif entropy < 60:
        strength = "Medium 🟠"
    else:
        strength = "Strong 🟢"

    print(F"Password strength is {strength}.")

    again = input("Would you like to test another password? (y/n)\n").lower()
    if again == "y":
        continue
    elif again == "n":
        print("Thank you for using PASSWORD STRENGTH CHECKER!!")
        break
    else:
        print("Please type either y or n.")
