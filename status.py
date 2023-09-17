grade = 'A'

match grade:
    case 'A' | 'B' | 'C' | 'D':
        print("Pass")
    case 'F':
        print("Fail")
    case _:
        print("Invalid Grade")
