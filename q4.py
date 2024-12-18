a = input("enter any string : ")
u = 0
l = 0
s = 0
d = 0

for i in range(len(a)):
    if(a[i]>= 'A' and a[i]<='Z'):
        u = u+1
    elif(a[i]>= 'a' and a[i]<='z'):
        l = l+1
    elif(a[i]>='0' and a[i]<='9'):
        d = d+1
    else:
        s = s+1
print("upper case count : ",u)
print("lower case count : ",l)
print("special charachters : ",s)
print("digit count : ",d)

