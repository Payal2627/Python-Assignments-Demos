'''Assignment on Exception Handling'''


'''
Develop a simple calculator program that performs basic arithmetic operations (+,
-, *, /) on two numbers provided by the user. The program should ask the user for
the numbers and the operator. However, the program should handle the following
exceptions:
a. Invalid Number: If the user enters a number that is not valid, catch the
exception and display an error message.
b. Invalid Operator: If the user enters an operator other than "+", "-", "*", or
"/", catch the exception and display an error message.
c. Division by Zero: If the user tries to divide by zero, catch the exception and
display an error message.
Write a program that performs the requested arithmetic operation and
handles the exceptions as described above.
'''

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    op = input("Enter operator (+, -, *, /): ")

    if op not in ['+', '-', '*', '/']:
        raise ValueError("Invalid Operator")

    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        if num2 == 0:
            raise ZeroDivisionError
        result = num1 / num2

    print("Result =", result)

except ValueError as e:
    if str(e) == "Invalid Operator":
        print("Error: Invalid operator entered.")
    else:
        print("Error: Invalid number entered.")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")



'''
Q2 Create class television that has members to hold the model number ,screen size
and price. Take a member function to take input from user, If more than 4 digits
are entered for model number, if screen size is smaller than 12 inches or greater
than 70 inches or if the price is negative or greater than 5000 Rs, then throw an
exception.
Write a main() that instantiates an object and allows the user to enter and display
data. If exception is caught, replace all data member values with zero'''
class Television:
    def __init__(self):
        self.model_no = 0
        self.screen_size = 0
        self.price = 0

    def accept(self):
        try:
            self.model_no = int(input("Enter Model Number: "))

            if len(str(self.model_no)) > 4:
                raise Exception("Model number should not exceed 4 digits.")

            self.screen_size = int(input("Enter Screen Size (12-70 inches): "))

            if self.screen_size < 12 or self.screen_size > 70:
                raise Exception("Screen size must be between 12 and 70 inches.")

            self.price = float(input("Enter Price: "))

            if self.price < 0 or self.price > 5000:
                raise Exception("Price must be between 0 and 5000.")

        except Exception as e:
            print("Exception:", e)
            self.model_no = 0
            self.screen_size = 0
            self.price = 0

    def display(self):
        print("\nTelevision Details")
        print("Model Number :", self.model_no)
        print("Screen Size  :", self.screen_size)
        print("Price        :", self.price)


# Main Program
tv = Television()
tv.accept()
tv.display()