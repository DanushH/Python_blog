is_positive_integer = True

while is_positive_integer:
    positive_integer = input("Enter a positive integer: ")
    
    if positive_integer.isdigit() and int(positive_integer) > 0:
        print(f"{positive_integer} is a positive integer.")
        is_positive_integer = False
    else:
        print("A positive integer is a whole number larger than 0.")