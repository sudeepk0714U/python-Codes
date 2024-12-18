import random


def is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))


def bogo_sort(arr):
    while not is_sorted(arr):
        random.shuffle(arr)
    return arr

# Example usage
arr = [73, 5, 19, 50, 97, 3, 33, 89, 46, 75, 85, 20, 59, 38, 56, 22, 10, 13, 77, 91]
print("Original array:", arr)
sorted_arr = bogo_sort(arr)
print("Sorted array:", sorted_arr)