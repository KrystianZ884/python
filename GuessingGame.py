import random

num = random.randrange(1,11)
tries = 3

print("Let's play a game. The system will provide a number from 1 to 10. Try to guess it")
while tries != 0:
    shoot = int(input("What's your shoot? "))

    if num > shoot:
        print("It's too low")
        tries = tries - 1
    elif num == shoot:
        print("Congratulations. You've guessed")
        break
    else:
        print("It's too high")
        tries = tries - 1

if tries == 0:
    print("No more tries. You lose")

