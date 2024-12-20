def partion(arr,st,end):
    idx = st-1
    pivot = arr[end]
    for j in range(st,end):
        if arr[j] <= pivot:
            idx +=1
            arr[j],arr[idx] = arr[idx],arr[j]
    idx += 1
    arr[end],arr[idx] = arr[idx],arr[end]
    return idx
def quickSort(arr,st,end):
    if st < end:
        pidx = partion(arr,st,end)
        quickSort(arr,st,pidx-1)
        quickSort(arr,pidx+1,end)

l1 = [5,2,6,4,1,3]
quickSort(l1,0,len(l1)-1)
print(l1)