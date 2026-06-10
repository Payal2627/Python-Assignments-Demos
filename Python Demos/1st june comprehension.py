data = [1,2,3,4,5,6,7]
result = [x*x for x in data]
print(result)

result = {x:x*x for x in data}
print(result)

mydict= {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49}
result = [x+y for x,y in mydict.items()]
print(result)