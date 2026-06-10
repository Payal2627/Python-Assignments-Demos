#WAP to print prime first n prime numbers 

count = int(input("Enter a number : "))
num = 2
while count >= 1:
    for i in range(2,num):
        if num%i == 0:
            break
    else:
        print(num,end= " ")
        count -= 1
    num += 1


#ulte numbers
num = int(input("Enter a number : "))
while num >= 1:
    print(num,end=" ")
    num-=1


#WAP to print prime numbers between 1 to 100
start = int(input("Enter the start value  :"))
stop = int(input("Enter the stop value : "))

for num in range(start,stop+1):
    for i in range(2,num):
        if num%i == 0:
            break
    else:
        print(num,end= " ")


#WAP to print prime numbers between 1 to 100
for num in range(2,101):
    for i in range(2,num):
        if num%i == 0:
            break
    else:
        print(num,end= " ")

#pattern 1
for i in range(1,6):
    for j in range(1,6):
        print("*",end=" ")
    print()


#pattern 2
for i in range(1,6):
    for j in range(1,6):
        print(j,end=" ")
    print()


#pattern 3
for i in range(1,6):
    for j in range(1,6):
        print(i,end=" ")
    print()


#pattern 4
for i in range(1,6):
    for j in range(5,0,-1):
        print(j,end=" ")
    print()


#pattern 5
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print()


#pattern 6
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()


#pattern 7
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end=" ")
    print()


#pattern 8
for i in range(6,1,-1):
    for j in range(1,i):
        print(j,end=" ")
    print()
