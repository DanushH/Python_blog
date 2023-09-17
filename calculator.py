def main():
    number1 = float(input("Enter 1st number: "))
    number2 = float(input("Enter 2nd number: "))

    print(f"{number1} + {number2} = {add(number1, number2)}")
    print(f"{number1} - {number2} = {subtract(number1, number2)}")
    print(f"{number1} * {number2} = {multiply(number1, number2)}")
    print(f"{number1} / {number2} = {divide(number1, number2)}")


def add(num1, num2):
    return round(num1 + num2, 2)

def subtract(num1, num2):
    return round(num1 - num2, 2)

def multiply(num1, num2):
    return round(num1 * num2, 2)

def divide(num1, num2):
    return round(num1 / num2, 2)

main()