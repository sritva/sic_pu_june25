#check if a number is a perfect square 
number = int(input("enter positive number:"))
if (int(number**0.5)**2==number):
    print(number,"is a perfect square")
else:
    print(number,"is not a perfect square")