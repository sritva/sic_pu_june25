#bubble sort algorithm
def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array
array = list(map(int, input("enter space seperated elements of array: ").split()))
print(bubble_sort(array))

