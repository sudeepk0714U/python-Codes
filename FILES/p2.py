f = open("abc.txt","w")
f.write("Hello ! I am learning Python.\n")
f.write("This is my first file in Python.\n")


f = open("abc.txt","r")
print(f.read())

f.close()