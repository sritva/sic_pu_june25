#program to print the frequency of an element in a given list of integers
def element_frequency(l, element):
    count = 0
    for i in l:
        if i == element:
            count += 1
    return f"the frequency of {element} is {count}"
l = list(map(int,input("enter space seperated elements of list: ").split()))
element = int(input("enter the element to find frequency: "))
print(element_frequency(l, element))