name = input("enter a string")
dict = {}
for i in name:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
for i in dict:
    print(f"{i} : {dict[i]}")
