class Time:
    def setTime(self):
        self.hr = int(input("Enter hr : "))
        self.min = int(input("Enter min : "))
        self.sec = int(input("Enter sec : "))

    def showTime(self):
        print(self.hr," : ",self.min," : ",self.sec)

t1 = Time()
t1.setTime()
t1.showTime()