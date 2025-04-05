"""
Function to call search algos
1. Linear Search
2. Binary Search
3. Hash Search
4. Tree Search (Binary Tree)
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

def tree_search(arr, target):
    # Create Binary tree and search
    import tree_def as t
    tree = t.TreeNode(arr[0])
    for each_val in arr:
        tree.insert(each_val)

    # Search
    return tree.search_tree(target)

