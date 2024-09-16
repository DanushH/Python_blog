marks = int(input("Enter marks: "))

if 100 >= marks >= 75:
    print('A')
elif 75 > marks >= 65:
    print('B')
elif 65 > marks >= 55:
    print('C')
elif 55 > marks >= 45:
    print('D')
elif 45 > marks >= 0:
    print('F')
else:
    print("Invalid Score") 