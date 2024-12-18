#Write a Python program to merge the contents of two files into a third file. The names
#of the files must be accepted from the user.

n1 = input("Enter file name 1 :")
n2 = input("Enter file name 2 :")
f1  = open(n1,'w')
txt1 = input("Enter text in file 1 :")
f1.write(txt1)


f2  = open(n2,'w')
txt2 = input("Enter text in file 2 :")
f2.write(txt2)

f3 = open("ans.txt",'w')
f3.write(txt1 + "\n" + txt2)

print("Files merged successfully.")