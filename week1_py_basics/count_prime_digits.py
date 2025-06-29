# count the number of prime digits in a number
def count_prime_digits(n):
    count = 0
    for digit in str(n):
        if digit in '2357':
            count+=1
    return count
n=int(input("enter number: "))
print(count_prime_digits(n))
