#program to find the sum of list elements recursively
def sum_list(lst):
    if lst == []:
        return 0
    return lst[0] + sum_list(lst[1:])
lst = list(map(int, input("enter space seperated elements of list: ").split()))
print("sum of list elements is:", sum_list(lst))
    