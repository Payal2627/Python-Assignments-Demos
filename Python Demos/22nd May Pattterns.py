#pattern 1
# for i in range(1,6):
#     for j in range(1,7-i):
#         print("$",end=" ")
#     for j in range(1,i+1):
#         print("*",end=" ")
    
#     print()


#pattern 2
for i in range(1,6):
    for j in range(1,7-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*  ",end=" ")    
    print()


#pattern 3
for i in range(1,6):
    for j in range(1,i+1):
        print(" ",end=" ")
    for j in range(1,7-i):
        print("*  ",end=" ")    
    print()


#pattern 4
for i in range(1,5):
    for j in range(1,7-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*  ",end=" ")    
    print()
for i in range(1,6):
    for j in range(1,i+1):
        print(" ",end=" ")
    for j in range(1,7-i):
        print("*  ",end=" ")    
    print()


#pattern 5
for i in range(1,5):
    for j in range(1,i+1):
        print(" ",end=" ")
    for j in range(1,7-i):
        print("*  ",end=" ")    
    print()
for i in range(1,6):
    for j in range(1,7-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*  ",end=" ")    
    print()


#pattern 6
for i in range(1,6):
    for j in range(1,7-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        if j==1 or j==i or i==5:
            print("*  ",end=" ")    
        else:
            print("   ",end=" ")    
    print()


#pattern 7
for i in range(1,7):
    for j in range(1,7):
        if i==1 or i==6 or j==1 or j==6:
            print("*",end=" ")
        else:
            print(j,end=" ")

    print()


#pattern 8
for i in range(1,6):
    for j in range(1,7-i):
        print(" ",end=" ")
    for j in range(1,i+1):        
        print(j,end=" ")
    for j in range(i-1,0,-1):
        print(j,end=" ")
    print()


#sum of digits
num = int(input("Enter any number : "))
sum = 0
while num != 0 :
    sum = sum + num % 10
    num = num // 10

print("Sum = ",sum)


#reverse of digits
num = int(input("Enter any number : "))
rev = 0
while num != 0 :
    rev = rev*10 + num % 10
    num = num // 10

print("Reverse = ",rev)


#digit count
num = int(input("Enter any number : "))
count = 0

while num!= 0:
    num = num // 10
    count += 1

print("Number of digits =",count)


#palandrome
num = int(input("Enter any number : "))
temp = num
rev = 0
while num != 0 :
    rev = rev*10 + num % 10
    num = num // 10

print("Reverse = ",rev)

if temp == rev :
    print(temp," is a pallindrome")
else:
    print(temp," is not a pallindrome")



# armstrong
num = int(input("Enter any number : "))
count = 0
temp = num
while num!= 0:
    num = num // 10
    count += 1

print("Number of digits =",count)

sum = 0
num = temp
while num != 0:
    sum = sum + (num%10)**count
    num = num // 10

if sum == temp:
    print(temp," is armstrong")
else:
    print(temp," is not armstrong")