#sum of  series
num = int(input("Enter a number : "))
sum = 0
for i in range(1,num+1):
    sum = sum+i
    print(sum)
    

#table
num = int(input("Enter a number : "))
for i in range(1,11):
    p = num * i
    print(num," * ",i," = ",p)


#Prime number
num = int(input("Enter a number : "))
for i in range(2, num):
    if num % i == 0:
        print(num," is not prime ")
        break
  
else:
    print(num," is prime")


#Percentage
num = int(input("Enter number of students : "))

for i in range(1,num+1):
    m1 = int(input("Enter marks of english : "))
    m2 = int(input("Enter marks of hindi : "))
    m3 = int(input("Enter marks of sst : "))
    m4 = int(input("Enter marks of science : "))
    m5 = int(input("Enter marks of maths : "))
    sum  = m1+m2+m3+m4+m4
    percentage = sum  * 100 / 500
    print("Percentage = ",percentage)


#Factorial
num = int(input("Enter a number : "))
fact = 1
for i in range(1,num+1):
    fact = fact * i

print("Factorial - ",fact)


#fabonanccica series
num = int(input("Enter a number : "))
a,b = 1,0

for i in range(1,num+1):
    c = a+b
    print(c,end=" ")
    a = b
    b = c


#ticket price
num = int(input("Enter the number of passengers : "))
ticket_price = float(input("Enter ticket price  :"))
total = 0

for i in range(1,num+1):
    age = int(input("Enter the age : "))
    if age >= 60:
        dis = 50
    elif age <= 12:
        dis = 30
    else:
        dis = 0

    final_price = ticket_price - ticket_price * dis /100
    print(final_price)
    total = total + final_price

print("Please pay : ",total)


#keyword else/break
for i in range(1,11):
    print(i,end=" ")
    if i == 7:
        break
else:
    print("I am done")


#keyword pass
for i in range(1,11):
    pass # do nothing
print(i)