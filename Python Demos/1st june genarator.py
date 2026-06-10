import random
# def generateNumber(n):
#     result = []
#     for i in range(n):
#         result.append(random.randint(1,10000))
#     return result

def generateNumber(n):    
    for i in range(n):
        yield random.randint(1,10000)
    

mynumbers = generateNumber(10)
print(next(mynumbers))
print(next(mynumbers))
print(next(mynumbers))
print(next(mynumbers))
print(next(mynumbers))
print(next(mynumbers))
print(next(mynumbers))
print(next(mynumbers))
print(next(mynumbers))
print(next(mynumbers))
print(next(mynumbers))
print(next(mynumbers))