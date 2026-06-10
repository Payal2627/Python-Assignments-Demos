class Student:
    '''Constructor :  It is a special type of method which is
    called automatically while object is created. It is used 
    to initialize the object'''
    '''Parameterized constructor -> We pass parameters for initialization'''
    def __init__(self,sid=101,sname="Abc",percentage=89):
        self.sid = sid
        self.sname = sname
        self.percentage = percentage
    
    def setStudent(self):
        self.sid = int(input("Enter sid : "))
        self.sname = input("Enter sname : ")
        self.percentage = float(input("Enter percentage : "))

    def showStudent(self):
        print("Sid = ",self.sid)
        print("SName = ",self.sname)
        print("Percentage =",self.percentage)

s1 = Student(101,"Ajay",89)
#s1.setStudent()
s1.showStudent()
