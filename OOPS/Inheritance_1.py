
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print(self.name)
        print(self.age)
class Teacher(Person):
    def __init__(self,name,age,exp,salary):
        Person.__init__(self,name,age)
        self.exp = exp
        self.salary = salary
    def displayDetails(self):
        print(self.name)
        print(self.age)
        print(self.exp)
        print(self.salary)
class Student(Person):
    def __init__(self,name,age,college,cgpa):
        Person.__init__(self,name,age)
        self.college = college
        self.cgpa = cgpa
    def displayDetails(self):
        print(self.name)
        print(self.age)
        print(self.college)
        print(self.cgpa)
s1 = Student("sudeep",20,"vasavi",9.09)
t1 = Teacher("CodeWithRamu",40,100,10000)
s1.displayDetails()
t1.displayDetails()


