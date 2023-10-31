def factorial(num):
    # base case
    if num == 1:
        return 1
    
    # recursive case
    return num * factorial(num - 1)
    
NUM = 3
print(f"Factorial of {NUM} is {factorial(NUM)}")