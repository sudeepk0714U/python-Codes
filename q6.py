def series(a):
    sum = 0
    for i in range(1,a+1):
        sum+= (i**i)/i
        
    return sum

b = int(input("enter a number : "))
print("Series expansion is : ",series(b))

