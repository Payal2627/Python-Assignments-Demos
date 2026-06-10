'''Assignemnt on Comprehension, Generator & Decorator'''


#Q1) Find all of the numbers from 1–1000 that are divisible by 8
nums = [i for i in range(1, 1001) if i % 8 == 0]
print(nums)


#Q2) Find all of the numbers from 1–1000 that have a 6 in them
nums = [i for i in range(1, 1001) if '6' in str(i)]
print(nums)


#Q3) Count the number of spaces in a string (take input from user)
s = input("Enter a string: ")

spaces = len([ch for ch in s if ch == ' '])

print("Number of spaces:", spaces)


#Q4) Remove all of the vowels in a string (take input from user)
s = input("Enter a string: ")

result = ''.join([ch for ch in s if ch.lower() not in 'aeiou'])

print("String without vowels:", result)


#Q5) Find all of the words in a string that are less than 5 letters 
s = input("Enter a sentence: ")

words = [word for word in s.split() if len(word) < 5]

print(words)


#Q6) Use a dictionary comprehension to count the length of each word in a sentence
s = input("Enter a sentence: ")

word_lengths = {word: len(word) for word in s.split()}

print(word_lengths)


#Q7) Use a nested list comprehension to find all of the numbers from 1–1000 that are divisible by any single digit.
nums = [num for num in range(1, 1001)
        if any(num % digit == 0 for digit in range(2, 10))]

print(nums)


#Assignment on generator

#Q1 We want to generate Fibonacci numbers up to a certain limit. Instead of computing and storing the entire sequence in memory, create generator to yield Fibonacci numbers one by one, conserving memory and allowing for easy iteration.
def fibonacci(limit):
    a, b = 0, 1

    while a <= limit:
        yield a
        a, b = b, a + b


limit = int(input("Enter limit: "))

for num in fibonacci(limit):
    print(num, end=" ")


#Q2) Implement a generator function that yields palindrome numbers. Palindromes are numbers that read the same backward as forward (e.g., 121, 1331). Generate palindromes lazily and infinitely.
def palindrome_generator():
    num = 0

    while True:
        if str(num) == str(num)[::-1]:
            yield num
        num += 1


pal_gen = palindrome_generator()

for i in range(20):
    print(next(pal_gen), end=" ")


#Q3) Write a generator function that mimics the behavior of the built-in range() function. The generator should take start, stop, and step arguments and yield numbers within the specified range.
def my_range(start, stop=None, step=1):

    if stop is None:
        stop = start
        start = 0

    while (step > 0 and start < stop) or (step < 0 and start > stop):
        yield start
        start += step


for num in my_range(1, 10, 2):
    print(num, end=" ")


# Assignment on decorator

#Q1 Develop a memoization decorator that caches the results of function calls and returns the cached result when the same inputs occur again. This can greatly improve the performance of recursive or computationally intensive functions.
def memoize(func):
    cache = {}

    def wrapper(n):
        if n in cache:
            return cache[n]

        result = func(n)
        cache[n] = result
        return result

    return wrapper


@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


num = int(input("Enter a number: "))
print("Fibonacci:", fibonacci(num))
