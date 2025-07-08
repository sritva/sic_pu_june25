#binary search algorithm 
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1
array = list(map(int, input("enter space seperated elements of array: ").split()))
sorted_array = sorted(array)
target = int(input("enter target element: "))
print(binary_search(sorted_array, target))