bigStr = input("enter main string :")
subStr = input("enter sub string :")

index  = bigStr.find(subStr)

if(index > 0):
    print(f"sub string is at {index}th index")
else:
    print("sub string not present!!")