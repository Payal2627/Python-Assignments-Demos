A = set()
print(type(A))
A.add(10)
A.add(20)
A.add(30)
A.add(40)
A.add(50)
A.add(60)
print(A)
A.discard(200) #NO error if element is not present
print(A)
A.remove(300) #Raise an error if element is not present
print(A)

A = {10,20,30,40,50}
B = {40,50,60,70,80}
C = A.union(B)
print(C)
C = A | B #Union
print(C)

# Intersection
C = A.intersection(B)
print(C)
C = A & B #Intersection
print(C)
C = A.difference(B)
print(C)

C = B.difference(A)
print(C)

C = A - B
print(C)

C = A.symmetric_difference(B)
print(C)
C = A ^ B
print(C)

