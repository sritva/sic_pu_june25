#find the smallest among three numbers
num1, num2, num3 = map(int, input("enter three numbers: ").split())
if num1 < num2:
    if num1 < num3:
        print(num1,"is the smallest")
    else:
        print(num3,"is the smallest")
else:
    if num2 < num3:
        print(num2,"is the smallest")
    else:
        print(num3,"is the smallest")
    

