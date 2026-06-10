''''Python Assignment 10 (List)'''


#Q1) Write a program to find sum of all elements of list
lst = [10, 20, 30, 40, 50]

total = 0

for i in lst:
    total = total + i

print("Sum =", total)


#Q2) Write a program to find maximum and minimum element in a list.
lst = [25, 10, 45, 5, 30]

maximum = lst[0]
minimum = lst[0]

for i in lst:
    if i > maximum:
        maximum = i

    if i < minimum:
        minimum = i

print("Maximum =", maximum)
print("Minimum =", minimum)


#Q3) Write a program to find the second largest element in the list.
lst = [10, 50, 20, 80, 40]

largest = lst[0]
second = lst[0]

for i in lst:
    if i > largest:
        second = largest
        largest = i
    elif i > second and i != largest:
        second = i

print("Second Largest =", second)


#Q4) Write a program to reverse the list.
lst = [10, 20, 30, 40, 50]

rev = []

for i in range(len(lst)-1, -1, -1):
    rev.append(lst[i])

print("Original List =", lst)
print("Reversed List =", rev)


#Q5) Accept a number from user and check if this element is present in the list or not. Also tell how many times it is present in the list.
lst = [10, 20, 30, 20, 40, 20]

num = int(input("Enter number to search: "))

count = 0

for i in lst:
    if i == num:
        count += 1

if count > 0:
    print("Element Found")
    print("Occurrences =", count)
else:
    print("Element Not Found")


#Q6) Write a program to remove duplicates from the list.
lst = [10, 20, 30, 20, 40, 10, 50]

new_list = []

for i in lst:
    found = False

    for j in new_list:
        if i == j:
            found = True
            break

    if found == False:
        new_list.append(i)

print("List without duplicates:")
print(new_list)


# #Q7) Write a program to create a new list from existing list which contains cube of each number of list.
lst = [1, 2, 3, 4, 5]

cube_list = []

for i in lst:
    cube_list.append(i * i * i)

print(cube_list)


# #Q8) Write a program to create a duplicate of an existing list. It should not point to same list.
lst = [10, 20, 30, 40]

copy_list = []

for i in lst:
    copy_list.append(i)

print("Original =", lst)
print("Duplicate =", copy_list)



'''
Q9
Write a program of having n number of elements in the list and find out even
and odd elements in that list and then create two separate lists which will have
even elements and other will have odd elements.
'''
n = int(input("Enter number of elements: "))

lst = []

for i in range(n):
    num = int(input("Enter number: "))
    lst.append(num)

even_list = []
odd_list = []

for i in lst:
    if i % 2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)

print("Even List =", even_list)
print("Odd List =", odd_list)


#Q10) Write a program to remove all occurrences of a given element in the list.
lst = [10, 20, 30, 20, 40, 20, 50]

num = int(input("Enter element to remove: "))

new_list = []

for i in lst:
    if i != num:
        new_list.append(i)

print(new_list)


#Q11) Write a program to print all numbers which are divisible by m and n in the list.
lst = [10, 20, 30, 40, 60, 90]

m = int(input("Enter m: "))
n = int(input("Enter n: "))

print("Numbers divisible by both:")

for i in lst:
    if i % m == 0 and i % n == 0:
        print(i)


#Q12) Write a program to create three lists of numbers, their squares and cubes
numbers = []
squares = []
cubes = []

n = int(input("Enter number of elements: "))

for i in range(1, n + 1):
    numbers.append(i)
    squares.append(i * i)
    cubes.append(i * i * i)

print("Numbers =", numbers)
print("Squares =", squares)
print("Cubes =", cubes)


#Q13) Write a program to print list after removing even numbers.
lst = [10, 15, 20, 25, 30, 35, 40]

odd_list = []

for i in lst:
    if i % 2 != 0:
        odd_list.append(i)

print("List after removing even numbers:")
print(odd_list)