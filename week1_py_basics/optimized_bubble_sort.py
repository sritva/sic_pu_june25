#optimized bubble sort algorithm 
def optimized_bubble_sort(array):
    n = len(array)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if not swapped:
            break
    return array
array = list(map(int, input("enter space seperated elemts of array: ").split()))
print(optimized_bubble_sort(array))