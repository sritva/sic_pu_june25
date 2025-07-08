#program to find the factorial of a given number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)
n = int(input("enter a number: "))
print("factorial of", n, "is", factorial(n))