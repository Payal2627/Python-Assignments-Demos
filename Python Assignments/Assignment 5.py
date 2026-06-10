'''Python Assignment -5 (Looping)'''

'''
Question 1) Write a program to prompt user to enter userid and password. If Id and password is incorrect give him chance to re-enter the credentials. Let him try 3
times. After that program to terminate.
'''
correct_userid = "admin"
correct_password = "1234"
attempts = 0

while attempts < 3:
    userid = input("Enter User ID: ")
    password = input("Enter Password: ")

    if userid == correct_userid and password == correct_password:
        print("Login Successful")
        break
    else:
        print("Incorrect User ID or Password")
        attempts = attempts + 1

if attempts == 3:
    print("Program Terminated")


'''
Question 2) Enter number of students from user. For those many students accept marks of 5
subject marks from user and calculate percentage. Display all percentage and
average percentage of students.
'''
students = int(input("Enter number of students: "))
total_percentage = 0

for i in range(students):
    print("Enter marks for Student", i + 1)

    total = 0

    for j in range(5):
        marks = int(input("Enter marks of subject: "))
        total = total + marks

    percentage = total / 5

    print("Percentage =", percentage)

    total_percentage = total_percentage + percentage

average_percentage = total_percentage / students

print("Average Percentage of all students =", average_percentage)


'''
Question 3) Accept no. of passengers from user and per ticket cost. Then accept age of each
passenger and then calculate total amount to ticket to travel for all of them based on
following condition :
a. Children below 12 = 30% discount
b. Senior citizen (above 59) = 50% discount
c. Others need to pay full.
'''
passengers = int(input("Enter number of passengers: "))
ticket_cost = float(input("Enter cost of one ticket: "))
total_amount = 0

for i in range(passengers):
    age = int(input("Enter age of passenger: "))

    if age < 12:
        amount = ticket_cost - (ticket_cost * 0.30)

    elif age > 59:
        amount = ticket_cost - (ticket_cost * 0.50)

    else:
        amount = ticket_cost

    total_amount = total_amount + amount

print("Total Ticket Amount =", total_amount)


#Question 4) WAP to print Armstrong number within a given range
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

print("Armstrong Numbers are:")

for num in range(start, end + 1):

    temp = num
    digits = len(str(num))
    total = 0

    while temp > 0:
        digit = temp % 10
        total = total + (digit ** digits)
        temp = temp // 10

    if total == num:
        print(num)


#Question 5) Write a program to print prime numbers between 1 to 100.
print("Prime Numbers from 1 to 100:")

for num in range(2, 101):

    prime = True

    for i in range(2, num):

        if num % i == 0:
            prime = False
            break

    if prime:
        print(num)



#Question 6) Write a program to print first n prime numbers.
n = int(input("Enter value of n: "))

count = 0
num = 2

while count < n:

    prime = True

    for i in range(2, num):

        if num % i == 0:
            prime = False
            break

    if prime:
        print(num)
        count = count + 1

    num = num + 1
    

'''
Question 7 
Write a program to solve the following series :
a. 1! + 2! + 3! + 4! + .....n!
b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)
c. Find the sum of a geometric series from 1 to n where the common ratio is 2.
d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10
e. x - x2/3 + x3/5 - x4/7 + .... to n terms
''' 
#a)
n = int(input("Enter n: "))
sum = 0
factorial = 1

for i in range(1, n + 1):

    factorial = factorial * i
    sum = sum + factorial

print("Sum of series =", sum)

#b)
N = int(input("Enter value of N: "))
sum = 0

for i in range(1, N + 1):

    sum = sum + (N ** i)

print("Sum of series =", sum)

#c)
n = int(input("Enter n: "))
sum = 0

for i in range(n):
    sum = sum + (2 ** i)

print("Sum of geometric series =", sum)

#d)
a = int(input("Enter value of a: "))
sum = 0

for i in range(1, 11):

    sum = sum + (a ** i) / i

print("Sum of series =", sum)

#e)
x = int(input("Enter value of x: "))
n = int(input("Enter number of terms: "))

sum = 0
sign = 1
denominator = 1

for i in range(1, n + 1):

    term = (x ** i) / denominator

    sum = sum + (sign * term)

    sign = sign * -1
    denominator = denominator + 2

print("Sum of series =", sum)