class Employee:
    companyName = "apple"
    noOfEmployee  = 0;
    def __init__(self,name):
        self.name = name
        self.hike = 0.02
        Employee.noOfEmployee += 1
    def showDetails(self):
        print(f"name  = {self.name} hike = {self.hike} company name = {self.companyName} {self.noOfEmployee}")
e1 = Employee("sudeep")
e1.hike = 0.3
e1.companyName = "apple india"
e2 = Employee("anaya")
e1.showDetails()
e2.showDetails()
Employee.companyName = "google"
e1.showDetails()
e2.showDetails()
e1.companyName = "apple india"
e1.showDetails()
e2.showDetails()
for i in range(4):
    print(i)