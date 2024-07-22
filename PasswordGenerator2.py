import random
import string

def generate_password(length, letters = True, digits = True, punctuation = True):
    chars = ""
    if letters:
        chars += string.ascii_letters
    if digits:
        chars += string.digits
    if punctuation:
        chars += string.punctuation
    if not chars:
        print("Choose at least one character type")

    password = "".join(random.choice(chars) for i in range(length))
    return password


def main():
    length = int(input("How long would the password be?: "))
    letters = input("Should it contain letters?: Y/N ") == "Y"
    digits = input("Should it contain digits?: Y/N ") == "Y"
    punctuation = input("Should it contain punctuation?: Y/N ") == "Y"

    password = generate_password(length, letters, digits, punctuation)
    print(password)

main()
