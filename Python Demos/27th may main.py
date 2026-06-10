from programmer import Programmer
from salesmgr import SalesMgr
from admin import Admin

p1 = Programmer(101,"Prakash",45000,10,1000)
s1 = SalesMgr(102,"Surya",34000,4000)
a1 =Admin(103,"Akaash",34000,8000)


# p1.displayPrg() # Programmer's displayPrg
# s1.displaySales()
# a1.displayAdmin()

# p1.display()
# s1.display()
# a1.display()

# List of emps
allEmps = [p1,s1,a1]
for e in allEmps:
    e.display()