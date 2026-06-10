'''Python Assignment 2 (Basics)'''


#Question 1) Convert the time entered in hh,min and sec into seconds.
hh = int(input("Enter hours: "))
mm = int(input("Enter minutes: "))
ss = int(input("Enter seconds: "))
total_seconds = (hh * 3600) + (mm * 60) + ss
print("Total seconds =", total_seconds)


#Questin 2) Convert temp from Celsius to Fahrenheit. (C/5 = (F-32)/9)
c = float(input("Enter temperature in Celsius: "))
f = (c * 9 / 5) + 32
print("Temperature in Fahrenheit =", f)


#Question 3) Convert distant given in feet and inches into meter and centimeter.
feet = int(input("Enter feet: "))
inches = int(input("Enter inches: "))
total_inches = (feet * 12) + inches
cm = total_inches * 2.54
meter = cm / 100
print("Distance in centimeters =", cm)
print("Distance in meters =", meter)


#Question 4) WAP to calculate area of triangle and rectangle
base = float(input("Enter base: "))
height = float(input("Enter height: "))
area = 0.5 * base * height
print("Area of triangle =", area)
length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
area = length * breadth
print("Area of rectangle =", area)


#Question 5) WAP to calculate selling price of book based on cost price and discount.
cp = float(input("Enter cost price: "))
discount = float(input("Enter discount percentage: "))
discount_amount = (cp * discount) / 100
sp = cp - discount_amount
print("Selling Price =", sp)


#Question 6) WAP to calculate total salary of employee based on basic, da=10% of basic, ta=12% of basic, hra=15% of basic.
basic = float(input("Enter basic salary: "))
da = basic * 10 / 100
ta = basic * 12 / 100
hra = basic * 15 / 100
total_salary = basic + da + ta + hra
print("DA =", da)
print("TA =", ta)
print("HRA =", hra)
print("Total Salary =", total_salary)


#Question 7) Find the sum of three-digit number.
num = int(input("Enter a three-digit number: "))
digit1 = num // 100
digit2 = (num // 10) % 10
digit3 = num % 10
sum_digits = digit1 + digit2 + digit3
print("Sum of digits =", sum_digits)


#Question 8) Write a program to swap two numbers using third variable.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
temp = a
a = b
b = temp
print("After swapping:")
print("a =", a)
print("b =", b)


#Question 9) Write a program to swap two numbers without using third variable.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
a = a + b
b = a - b
a = a - b
print("After swapping:")
print("a =", a)
print("b =", b)


#Question 10) Write a program to reverse three-digit number.
num = int(input("Enter a three-digit number: "))
digit1 = num // 100
digit2 = (num // 10) % 10
digit3 = num % 10
reverse = (digit3 * 100) + (digit2 * 10) + digit1
print("Reversed number =", reverse)


#Question 11) Write a program to accept an integer amount from user and tell minimum number of notes needed for representing that amount.
amount = int(input("Enter amount: "))

note500 = amount // 500
amount = amount % 500

note200 = amount // 200
amount = amount % 200

note100 = amount // 100
amount = amount % 100

note50 = amount // 50
amount = amount % 50

note20 = amount // 20
amount = amount % 20

note10 = amount // 10
amount = amount % 10

print("500 notes =", note500)
print("200 notes =", note200)
print("100 notes =", note100)
print("50 notes =", note50)
print("20 notes =", note20)
print("10 notes =", note10)