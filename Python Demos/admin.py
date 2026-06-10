from emp import Emp
class Admin(Emp):
    def __init__(self,eid,ename,basic,incentive):
        #Call the constructor of super class
        super().__init__(eid,ename,basic)
        self.incentive = incentive

    # def displayAdmin(self):
    #     super().display() 
    #     print("Incentive =",self.incentive)
        
    def display(self):
        super().display() 
        print("Incentive =",self.incentive)