numbers = [64, 34, 25, 12, 22, 11, 90]
n = len(numbers)
for i in range(n):
    swapped = False
    for j in range(0,n-i-1):
        if numbers[j] > numbers[j+1] :
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
            swapped = True
    if not swapped:
        break
print(numbers)

