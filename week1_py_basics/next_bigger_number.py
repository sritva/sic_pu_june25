#Given a number, find very next possible bigger number that has all the digits of the given number.
def next_bigger_number(n):
    lst = []
    for i in str(n):
        lst.append(int(i))
        lst.sort()
    i = len(lst) - 2
    while i >= 0:
        if lst[i] < lst[i+1]:
            break
        i -= 1
    if i == -1:
        return 'no bigger number'
    else:
        j = len(lst) - 1
        while j > i:
            if lst[j] > lst[i]:
                break
            j -= 1
        temp = lst[i]
        lst[i] = lst[j]
        lst[j] = temp
        lst[i+1:] = sorted(lst[i+1:])
    new_num = ""
    for i in lst:
        new_num += str(i)
    return f'the next bigger number is {int(new_num)}'
n = int(input("enter number: "))
print(next_bigger_number(n))
        

    
    