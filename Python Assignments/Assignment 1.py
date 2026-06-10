'''Python Assignment 1 (Basics)'''


#Question1) Write a program to calculate the percentage of student based on marks of any 5 subjects.
# Input marks of 5 subjects
sub1 = float(input("Enter marks of subject 1: "))
sub2 = float(input("Enter marks of subject 2: "))
sub3 = float(input("Enter marks of subject 3: "))
sub4 = float(input("Enter marks of subject 4: "))
sub5 = float(input("Enter marks of subject 5: "))
# Calculate total
total = sub1 + sub2 + sub3 + sub4 + sub5
# Calculate percentage
percentage = (total / 500) * 100
# Display result
print("Total Marks =", total)
print("Percentage =", percentage, "%")


#Question 2) Write a program to calculate area of rectangle based on length and breadth.
length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
area = length * breadth
print("Area of Rectangle =", area)


#Question 3) Program to find quotient and remainder of two numbers.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
quotient = num1 // num2
remainder = num1 % num2
print("Quotient =", quotient)
print("Remainder =", remainder)


#Question 4) Write a program to enter P, T, R and calculate simple Interest.
P = float(input("Enter Principal Amount: "))
T = float(input("Enter Time: "))
R = float(input("Enter Rate: "))
SI = (P * T * R) / 100
print("Simple Interest =", SI)


#Question 5) Write a program to enter P, T, R and calculate Compound Interest. 
P = float(input("Enter Principal Amount: "))
R = float(input("Enter Rate: "))
T = float(input("Enter Time: "))
amount = P * (1 + R/100) ** T
CI = amount - P
print("Compound Interest =", CI)


#Question 6) Write a Program to input two angles from user and find third angle of the triangle.
angle1 = float(input("Enter first angle: "))
angle2 = float(input("Enter second angle: "))
third_angle = 180 - (angle1 + angle2)
print("Third angle =", third_angle)


#Question 7) Program to Find the Roots of a Quadratic Equation
a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
c = float(input("Enter value of c: "))

d = (b**2) - (4*a*c)  # Discriminant
# Finding roots
root1 = (-b + d**0.5) / (2*a)
root2 = (-b - d**0.5) / (2*a)
print("Root 1 =", root1)
print("Root 2 =", root2)


#Question 8) Write a program to convert days into years, weeks and days.
days = int(input("Enter number of days: "))
years = days // 365
remaining_days = days % 365
weeks = remaining_days // 7
days_left = remaining_days % 7
print("Years =", years)
print("Weeks =", weeks)
print("Days =", days_left)


#Question 9) Write a program to enter base and height of a triangle and find its area.
base = float(input("Enter base: "))
height = float(input("Enter height: "))
area = 0.5 * base * height
print("Area of Triangle =", area)


#Question 10 ) Write a program to calculate area of an equilateral triangle.
side = float(input("Enter side of triangle: "))
area = ((3**0.5) / 4) * side * side
print("Area =", area)


#Question 11) Find the area and circumference of circle.
radius = float(input("Enter radius: "))
pi = 3.14
area = pi * radius * radius
circumference = 2 * pi * radius
print("Area =", area)
print("Circumference =", circumference)


#Question 12) Find the volume of sphere.
radius = float(input("Enter radius: "))
pi = 3.14
volume = (4/3) * pi * radius**3
print("Volume of Sphere =", volume)