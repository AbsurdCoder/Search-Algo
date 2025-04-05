"""
Function to call search algos
"""


def linear_search(arr, target):
    for i,val in enumerate(arr):
        if val == target:
            return i
    return -1

def binary_search(arr, target):
    # Assumption : Array is sorted
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1

def hash_table_search(data_in_dict, target):
    return data_in_dict.get(target, None)

