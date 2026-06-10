class Emp:
    def __init__(self,eid=0,ename="",basic=0):
        self.eid = eid
        self.ename = ename
        self.basic = basic

    def display(self):
        print("Eid = ",self.eid)
        print("EName =",self.ename)
        print("Basic =",self.basic)


# e1 = Emp(101,"Akash",32000)
# e1.display()


