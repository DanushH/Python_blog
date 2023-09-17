marks = int(input("Enter marks: "))

# evaluate grade
if 100 >= marks >= 75:
    grade = 'A'
elif 75 > marks >= 65:
    grade = 'B'
elif 65 > marks >= 55:
    grade = 'C'
elif 55 > marks >= 45:
    grade = 'D'
elif 45 > marks >= 0:
    grade = 'F'
else:
    grade = "Invalid Score"

# evaluate status
match grade:
    case 'A' | 'B' | 'C' | 'D':
        status = "Pass"
    case 'F':
        status = "Fail"
    case _:
        status = "Invalid Score"

# print result
print(f"Grade: {grade}  Status: {status}")