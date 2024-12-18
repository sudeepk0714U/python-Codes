class Student :
    def __init__(self,p,c,m):
        self.p = p
        self.c = c
        self.m = m
    @property
    def average(self):
        return (self.p + self.c + self.m) / 3
s = Student(99,99,99)
print(s.average)
s.p = 89
print(s.average)