def counting_sort(arr, pos):
    Max = 9
    count = [0] * (Max + 1)
    b = [0] * len(arr)
    for i in range(len(arr)):
        count[(arr[i] // pos) % 10] += 1
    for i in range(1, Max + 1):
        count[i] += count[i - 1]
    for i in range(len(arr) - 1, -1, -1):
        digit = (arr[i] // pos) % 10
        b[count[digit] - 1] = arr[i]
        count[digit] -= 1
    return b
def Radixsort(arr):
    max1 = max(arr)
    exp = 1
    while max1 // exp > 0:
        arr = counting_sort(arr, exp)
        exp *= 10
    return arr

arr = [73, 5, 19, 50, 97, 3, 33, 89, 46, 75, 85, 20, 59, 38, 56, 22, 10, 13, 77, 91]
print("Sorted array is:")
print(Radixsort(arr))
