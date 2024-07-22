def is_palindrome(text):
    text = text.replace(" ", "").lower()
    return text == text[::-1]

text = input("Provide text: ")

if is_palindrome(text):
    print("Your text is a palindrome")
else:
    print("Your text is not a palindrome")