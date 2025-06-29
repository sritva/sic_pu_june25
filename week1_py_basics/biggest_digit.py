# find the biggest digit in a number 
def find_biggest_digit(n):
    return max(int(digit) for digit in str(n))
n=int(input("enter number:"))
print(find_biggest_digit(n)) 