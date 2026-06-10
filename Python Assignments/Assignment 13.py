'''Python Assignment 13 (Dictionary)'''


#Q1 Python Program to Add a Key-Value Pair to the Dictionary
d = {"a": 10, "b": 20}

key = input("Enter key: ")
value = int(input("Enter value: "))

d[key] = value

print("Updated Dictionary:", d)


#Q2 Python Program to Concatenate Two Dictionaries Into One
d1 = {"a": 10, "b": 20}
d2 = {"c": 30, "d": 40}

d3 = {}

for i in d1:
    d3[i] = d1[i]

for i in d2:
    d3[i] = d2[i]

print("Merged Dictionary:", d3)


#Q3 Python Program to Check if a Given Key Exists in a Dictionary or Not
d = {"a": 10, "b": 20, "c": 30}

key = input("Enter key to search: ")

flag = 0

for i in d:
    if i == key:
        flag = 1
        break

if flag == 1:
    print("Key exists")
else:
    print("Key does not exist")


#Q4 Python Program to Generate a Dictionary that Contains Numbers (between 1 and n) in the Form (x,x*x).
n = int(input("Enter n: "))

d = {}

for i in range(1, n + 1):
    d[i] = i * i

print(d)


#Q5 Python Program to Sum All the Items in a Dictionary
d = {"a": 10, "b": 20, "c": 30}

sum = 0

for i in d:
    sum = sum + d[i]

print("Sum =", sum)


#Q6 Python Program to Multiply All the Items in a Dictionary
d = {"a": 2, "b": 3, "c": 4}

mul = 1

for i in d:
    mul = mul * d[i]

print("Multiplication =", mul)


#Q7 Python Program to Remove the Given Key from a Dictionary
d = {"a": 10, "b": 20, "c": 30}

key = input("Enter key to remove: ")

if key in d:
    del d[key]
    print("Updated Dictionary:", d)
else:
    print("Key not found")


#Q8 Python Program to Count the Frequency of Words Appearing in a String Using a Dictionary
s = input("Enter a string: ")

words = s.split()

d = {}

for word in words:
    if word in d:
        d[word] = d[word] + 1
    else:
        d[word] = 1

print("Word Frequencies:")
for i in d:
    print(i, ":", d[i])