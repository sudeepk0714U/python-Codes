def Merge(arr,si,mid,ei):
    idx1 = si
    idx2 = mid+1
    i = 0
    temp = [0] * (ei - si + 1)
    while idx1 <=mid and idx2 <=ei:
        if arr[idx1] < arr[idx2]:
            temp[i] = arr[idx1]
            idx1 += 1
        else:
            temp[i] = arr[idx2]
            idx2 += 1
        i += 1
    while idx1 <=mid:
        temp[i] = arr[idx1]
        i += 1
        idx1 += 1
    while idx2 <=ei:
        temp[i] = arr[idx2]
        i += 1
        idx2 += 1
    j = si
    for k in range(len(temp)):
        arr[j] = temp[k]
        j += 1

def MergeSort(arr,si,ei):
    if si >= ei:
        return
    mid = si + (ei - si)//2
    MergeSort(arr, si, mid)
    MergeSort(arr, mid+1, ei)
    Merge(arr,si,mid,ei)

array = []
s = int(input("enter the size of the array"))
for i in range(s):
    array.append(int(input(f"enter element {i+1}: ")))

MergeSort(array,0,s-1)
print(array)
