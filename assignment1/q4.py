import sys
while(1):
    a = input("enter a string : ")
    if(a == 'QUIT'):
        print("exitting the code !!")
        sys.exit(0)
    l = len(a);
    print(f"length is {l}")