#calculator
# num1 = int(input("Enter a number :"))
# num2 = int(input("Enter a number : "))
# op = input("Enter operator (+,-,/,*) : ")

# if op == "+":
#     print("Sum = ",num1+num2)
# elif op == '-':
#     print("Difference =",num1-num2)
# elif op == '*':
#     print("Product :",num1*num2)
# elif op == '/':
#     print("Division :",num1/num2)
# else:
#     print("Invalid operator")


#Login with 2 step verification
# uname = input("Enter username : ")
# pwd = input("Enter password : ")
# import random
# if uname == "PNM" and pwd =="2627":
#     otp = random.randint(1000,10000)
#     print("Your 4 digit otp is : ",otp)
#     input_otp = int(input("Enter otp : "))
#     if otp == input_otp:
#         print("Login successful")
#     else:
#         print("Invalid OTP")
# else:
#     print("Invalid credential")


#marraige verification
# gender = input("Enter your gender (m/f) : ")
# age = int(input("Enter your age :"))

# if gender == 'm':
#     if age>=21:
#         print("You are eligible to marry")
#     else:
#         print("You are not eligible to marry")
# else:
#     if age>=18:
#         print("You are eligible to marry")
#     else:
#         print("You are not eligible to marry")


#menu driven program
print(" 1. Even Odd")
print(" 2. Greater of Two Numbers")
print(" 3. Area of Circle")
print(" 4. Percentage of Student")
print(" 5. Exit")

choice = int(input("Enter your choice : "))

if choice == 1:
    num = int(input("Enter a number : "))

    if num % 2 == 0:
        print(num, "is Even")
    else:
        print(num, "is Odd")

elif choice == 2:
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))

    if num1 > num2:
        print(num1, "is greater")
    elif num2 > num1:
        print(num2, "is greater")
    else:
        print("Both numbers are equal")

elif choice == 3:
    radius = float(input("Enter radius of circle : "))

    area = 3.14 * radius * radius

    print("Area of Circle =", area)

elif choice == 4:
    m1 = float(input("Enter marks of Subject 1 : "))
    m2 = float(input("Enter marks of Subject 2 : "))
    m3 = float(input("Enter marks of Subject 3 : "))
    m4 = float(input("Enter marks of Subject 4 : "))
    m5 = float(input("Enter marks of Subject 5 : "))

    total = m1 + m2 + m3 + m4 + m5
    percentage = total*100 / 500

    print("Total Marks =", total)
    print("Percentage =", percentage, "%")

elif choice == 5:
    print("---------- End of Program ----------")

else:
    print("Invalid Choice")