student = {'name':"sudeep",'age' : 21,'courses' : ['math','ece']}
print(student)
print(student['name'])

print(student.get('name'))
print(student.get('address'))# return none
print(student.get('address','not there'))# returns not there

student['age'] = 22
print(student.get('age'))# 22

student['phone'] ='7013680993'
print(student)

student.update({'name' : "sudeep kumar",'age' : 20})
print(student)

del student['courses']
print(student)

age = student.pop('age') # removes age
print(student)
print(age)

print(student.keys())
print(student.values())
print(student.items())

# looping

for key,values in student.items():
    print(key,"+",values)