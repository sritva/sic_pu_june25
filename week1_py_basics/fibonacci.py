# print n terms of the fibonacci series with 1 and 2 as first and second terms
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fibonacci(n-1) + fibonacci(n-2)
n = int(input("enter number of terms: "))
for i in range(1, n+1):
    if i != n:
        print(fibonacci(i), end = ", ")
    else:
        print(fibonacci(i))