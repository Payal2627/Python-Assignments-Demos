from emp import Emp
class SalesMgr(Emp):
    def __init__(self,eid,ename,basic,commission):
        #Call the constructor of super class
        super().__init__(eid,ename,basic)
        self.commission = commission

    # def displaySales(self):
    #     super().display() 
    #     print("Commission =",self.commission)
    
    def display(self):
        super().display() 
        print("Commission =",self.commission)