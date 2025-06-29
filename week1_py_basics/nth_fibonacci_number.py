#find the nth fibonacci number (first two numbers are 1 and 2)
def fib(n):
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n-1) + fib(n-2)
n=int(input("enter number: "))
print(fib(n))
    
