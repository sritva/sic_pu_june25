#binary search algorithm using recursion
def recursive_binary_search(array, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return recursive_binary_search(array, target, low, mid - 1)
    else:
        return recursive_binary_search(array, target, mid + 1, high) 
array = list(map(int, input("enter space seperated elements of array: ").split())) 
sorted_array = sorted(array)
target = int(input("enter target element: "))
print(recursive_binary_search(sorted_array, target, 0, len(sorted_array)-1))
