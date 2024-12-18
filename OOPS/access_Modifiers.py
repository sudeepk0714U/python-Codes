""" private
class Employee:
    def __init__(self):
        self.__name = "sudeep"
a = Employee()
print(a._Employee__name)
"""


"""protected
class Student:
    def __init__(self):
        self._name = "sudeep" #protected variable
    def _funname(self): # protected method
        return "codeWithRamu"
class Subject(Student):
    pass
obj1 = Student()
obj2 = Subject()
print(obj1._name)
print(obj1._funname())
print(obj2._name)
print(obj2._funname())
"""



