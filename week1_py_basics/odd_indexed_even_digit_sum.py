#program to find the sum of odd placed even digits in a given number
def odd_placed_even_sum(n):
    sum = 0
    for i in range(len(str(n))):
        if int(str(n)[i]) % 2 == 0 and i % 2 == 1:
            sum += int(str(n)[i])
    return sum
n =int(input("enter a number: "))
print(odd_placed_even_sum(n))