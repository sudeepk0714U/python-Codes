class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Salary(Person):
    def __init__(self,age,name, salary):
        super().__init__(name,age)
        self.salary = salary
    def printdet(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}")

list =[
Salary('20',"krishna",10000),
 Salary('20',"krishna",1000),
Salary('20',"krishna",10000),
 Salary('20',"krishna",10000),
Salary('20',"krishna",10000),
]
for i in list:
    i.printdet()