#print the prime numbers in decreasing order between m and n (m < n)
def print_primes(m, n):
    if m <= 1 or n <= 1 or n < m:
        return 'enter valid range values'
    for num in range(n, m-1, -1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end = " ")
m=int(input("enter start point: "))
n=int(input("enter end point: "))
print_primes(m,n)