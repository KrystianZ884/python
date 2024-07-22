def sum(x, y):
    return (x + y)

def sub(x, y):
    return (x - y)

def div(x, y):
    return (x / y)

def mul(x, y):
    return (x * y)

def kalkulator():
    print("Choose operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    operator = int(input("Provide a number [1], [2], [3], or [4]: "))

    while operator > 0 and operator < 5:
        if operator in (1, 2, 3, 4):
            num1 = float(input("Provide the first number: "))
            num2 = float(input("Provide the second number: "))

            if operator == 1:
                print(f"{num1} + {num2} = ", sum(num1, num2))
            elif operator == 2:
                print(f"{num1} - {num2} = ", sub(num1, num2))
            elif operator == 3:
                print(f"{num1} * {num2} = ", mul(num1, num2))
            elif operator == 4:
                if num1 == 0 or num2 == 0:
                    print("You can't divide by 0.")
                else:
                    print(f"{num1} / {num2} = ", div(num1, num2))

        another_operation = input("Would you like another to try another operation? Y/N: ")
        if another_operation.lower() == "y":
            kalkulator()
        else:
            print("Closing the calculator")
            break
    else:
        print("Provide the proper operation number (1 / 2 / 3 / 4)")
        kalkulator()

kalkulator()