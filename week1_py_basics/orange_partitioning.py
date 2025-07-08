#orange partitioning problem 
#def quicksort(array, low, high):
#   if low < high:
#       pivot_index = Partition(array, low, high)
#       quicksort(array, low, pivot_index - 1)
#       quicksort(array, pivot_index + 1, high)
#    return array
def partition(array, low, high):
    pivot = array[high]
    k = low
    for i in range(low, high):
        if array[i] < pivot:
            array[i], array[k] = array[k], array[i]
            k += 1
    array[k], array[high] = array[high], array[k]
    return k

        
        