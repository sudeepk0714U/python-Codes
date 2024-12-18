class student:
    def __init__(self,n,m):
        self.name = n
        self.marks = m
    def avg(self):
        sum = 0
        for i in self.marks:
            sum = sum+i
        print(sum/3)
name = input("enter the name")
marks =[]
print("enter marks in 3 sub :")
for i in range(3):
   a = int(input(f"Enter marks for subject {i + 1}: "))
   marks.append(a)
s1 = student(name,marks)
s1.avg()
    
