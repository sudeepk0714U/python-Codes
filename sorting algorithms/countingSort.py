def counting_sort(arr,pos):
    Max = max(arr)
    count = [0] * (Max + 1)
    b = [0] * len(arr)


    for i in range(len(arr)):
        count[(arr[i]/pos)%10] += 1


    for i in range(1, Max + 1):
        count[i] += count[i - 1]


    for i in range(len(arr) - 1, -1, -1):
        b[count[(arr[i]/pos)%10] - 1] = arr[i]
        count[arr[i]] -= 1

    return b
arr = [64, 25, 12, 22, 11, 90]
print("Sorted array is:")
print(counting_sort(arr))

