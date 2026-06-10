'''Python Assignment 3 (Branching)'''


#Question 1) Write a program to check if the given number is positive or negative.
num = int(input("Enter a number: "))

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Number is zero")


#Question 2) Write a program to input any alphabet and check whether it is vowel or consonant.
ch = input("Enter an alphabet: ")

if ch in "aeiouAEIOU":
    print("Vowel")
else:
    print("Consonant")


#Question 3) Write a program to input angles of a triangle and check whether triangle is valid or not.
a = int(input("Enter first angle: "))
b = int(input("Enter second angle: "))
c = int(input("Enter third angle: "))

if a + b + c == 180:
    print("Valid triangle")
else:
    print("Invalid triangle")


#Question 4) Write a program to input all sides of a triangle and check whether triangle is valid or not.
a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if a + b > c and a + c > b and b + c > a:
    print("Valid triangle")
else:
    print("Invalid triangle")


#Question 5) Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.
a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if a == b == c:
    print("Equilateral triangle")
elif a == b or b == c or a == c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")


#Question 6) Write a program to calculate profit or loss.
cp = float(input("Enter cost price: "))
sp = float(input("Enter selling price: "))

if sp > cp:
    print("Profit =", sp - cp)
elif cp > sp:
    print("Loss =", cp - sp)
else:
    print("No profit no loss")


#Question 7) Write a program to check if user has entered correct userid and password.
userid = input("Enter userid: ")
password = input("Enter password: ")

if userid == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid userid or password")


'''
Question 8)
Write a program to prompt user to enter userid and password. After verifying
userid and password display a 4 digit random number and ask user to enter the
same. If user enters the same number then show him success message otherwise
failed. (Something like captcha)
''' 
import random

userid = input("Enter userid: ")
password = input("Enter password: ")

if userid == "admin" and password == "1234":

    num = random.randint(1000, 9999)
    print("Captcha:", num)

    user_num = int(input("Enter captcha: "))

    if user_num == num:
        print("Success")
    else:
        print("Failed")

else:
    print("Wrong userid or password")


#Question 9) Input 5 subject marks from user and display grade(eg.First class,Second class ..)
m1 = int(input("Enter marks 1: "))
m2 = int(input("Enter marks 2: "))
m3 = int(input("Enter marks 3: "))
m4 = int(input("Enter marks 4: "))
m5 = int(input("Enter marks 5: "))

total = m1 + m2 + m3 + m4 + m5
per = total / 5

print("Percentage =", per)

if per >= 60:
    print("First Class")
elif per >= 50:
    print("Second Class")
elif per >= 35:
    print("Pass Class")
else:
    print("Fail")


#Question 10) Write a program to check if person is eligible to marry or not (male age >=21 and female age>=18)
gender = input("Enter gender (male/female): ")
age = int(input("Enter age: "))

if gender == "male" and age >= 21:
    print("Eligible for marriage")
elif gender == "female" and age >= 18:
    print("Eligible for marriage")
else:
    print("Not eligible")


'''
Question 11)
Accept age of five people and also per person ticket amount and then calculate total
amount to ticket to travel for all of them based on following condition :
a. Children below 12 = 30% discount
b. Senior citizen (above 59) = 50% discount
c. Others need to pay full.
'''
total = 0

for i in range(1, 6):

    age = int(input("Enter age: "))
    ticket = float(input("Enter ticket amount: "))

    if age < 12:
        amount = ticket - (ticket * 0.30)

    elif age > 59:
        amount = ticket - (ticket * 0.50)

    else:
        amount = ticket

    total = total + amount

print("Total ticket amount =", total)


#Question 12) Write a program to check if given 3 digit number is a palindrome or not.
num = int(input("Enter 3 digit number: "))

rev = 0
temp = num

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

if temp == rev:
    print("Palindrome number")
else:
    print("Not palindrome")


'''
Question 13
Write a program to input electricity unit charges and calculate total electricity bill
according to the given condition:
For first 50 units Rs. 0.50/unit
For next 100 units Rs. 0.75/unit
For next 100 units Rs. 1.20/unit
For unit above 250 Rs. 1.50/unit
An additional surcharge of 20% is added to the bill
'''

unit = int(input("Enter electricity units: "))

if unit <= 50:
    bill = unit * 0.50

elif unit <= 150:
    bill = (50 * 0.50) + ((unit - 50) * 0.75)

elif unit <= 250:
    bill = (50 * 0.50) + (100 * 0.75) + ((unit - 150) * 1.20)

else:
    bill = (50 * 0.50) + (100 * 0.75) + (100 * 1.20) + ((unit - 250) * 1.50)

surcharge = bill * 0.20
total = bill + surcharge

print("Electricity Bill =", total)