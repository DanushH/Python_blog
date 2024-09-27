number1 = float(input("Enter 1st number: "))
number2 = float(input("Enter 2nd number: "))

add = round(number1 + number2, 2)
subtract = round(number1 - number2, 2)
multiply = round(number1 * number2, 2)
divide = round(number1 / number2, 2)

print(f"{number1} + {number2} = {add}")
print(f"{number1} - {number2} = {subtract}")
print(f"{number1} * {number2} = {multiply}")
print(f"{number1} / {number2} = {divide}")