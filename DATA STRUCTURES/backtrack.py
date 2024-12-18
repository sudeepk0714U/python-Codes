def permutation(arr,idx):
    if idx == len(arr):
        print(arr)
        return
    for i in range(idx,len(arr)):
        arr[i],arr[idx] = arr[idx],arr[i]
        permutation(arr,idx+1)
        arr[i], arr[idx] = arr[idx], arr[i]

n = "abc"
name = list(n)

permutation(name,0)


