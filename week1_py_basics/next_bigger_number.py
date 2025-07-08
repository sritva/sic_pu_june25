#Given a number, find very next possible bigger number that has all the digits of the given number.
def next_bigger_number(n):
    lst = []
    for i in str(n):
        lst.append(int(i))
    i = len(lst) - 2
    while i >= 0 and lst[i] >= lst[i+1]:
        i -= 1
    if i == -1:
        return 'no bigger number'
    #to be completed
    

    
    