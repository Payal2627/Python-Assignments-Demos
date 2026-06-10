from emp import Emp
class Programmer(Emp):
    def __init__(self,eid,ename,basic,extraHrs,costPerHrs):
        #Call the constructor of super class
        super().__init__(eid,ename,basic)
        self.extraHrs = extraHrs
        self.costPerHrs = costPerHrs

    # def displayPrg(self):
    #     super().display() 
    #     print("Extra Hrs =",self.extraHrs)
    #     print("Cost Per Hrs =",self.costPerHrs)

    def display(self):
        super().display() 
        print("Extra Hrs =",self.extraHrs)
        print("Cost Per Hrs =",self.costPerHrs)