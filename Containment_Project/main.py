from SY.symarks import SYMarks
from TY.tymarks import TYMarks
from student import Student

roll_no = int(input("Enter Roll Number : "))
name = input("Enter Name : ")

computer = int(input("Enter SY Computer Marks : "))
maths = int(input("Enter SY Maths Marks : "))
electronics = int(input("Enter SY Electronics Marks : "))

theory = int(input("Enter TY Theory Marks : "))
practical = int(input("Enter TY Practical Marks : "))

sy = SYMarks(computer, maths, electronics)
ty = TYMarks(theory, practical)

student = Student(roll_no, name, sy, ty)

student.calculate_result()