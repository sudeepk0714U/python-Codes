
l1 = []
print("enter 10 elements in tuple")
for i in range(10):
    x = int(input())
    l1.append(x)
tuple1 = tuple(l1)
tuple2 = tuple1[::-1]
print(tuple2)

