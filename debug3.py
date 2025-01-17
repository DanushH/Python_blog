# # 5. Exception Handling

# while True:
#     try:
#         number1 = float(input("Enter 1st number: "))
#         number2 = float(input("Enter 2nd number: "))

#         result = round(number1 / number2, 2)
        
#     except ValueError:
#         print("Incorrect value, Enter a valid number.")
#     except ZeroDivisionError:
#         print("Cannot divide by zero")
#     else:
#         print(f"{number1} / {number2} = {result}")
#         break


# # 7. Unit Tests

# # multiply.py
# def  multiply_numbers(num1, num2):
#     return  round(num1  *  num2, 2)

# # test_multiply.py 
# import unittest
# import multiply


# class TestMultiply(unittest.TestCase):

#     def test_multiply_positive_numbers(self):
#         self.assertEqual(multiply.multiply_numbers(4, 5), 20)

#     def test_multiply_negative_numbers(self):
#         self.assertEqual(multiply.multiply_numbers(-6, -3), 18)

#     def test_multiply_positive_and_negative_numbers(self):
#         self.assertEqual(multiply.multiply_numbers(7, -4), -28)

#     def test_multiply_decimals(self):
#         self.assertEqual(multiply.multiply_numbers(3.6587, 6.3254), 23.14)


# if __name__ == "__main__":
#     unittest.main()