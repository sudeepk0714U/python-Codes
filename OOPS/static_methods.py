class Math:
    def __init__(self,num):
        self.num = num
    def addT(self,n):
        self.num = self.num + n
    @staticmethod
    def add(a,b):
        return a+b

a=  Math(5)
print(a.num)
a.addT(5)
print(a.num)
print(a.add(4,5))