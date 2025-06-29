# accept a number from user and print its formatted math table 
input_number = int(input("Enter a number to print its math table: "))
for i in range(1, 11):
    print(f"{input_number:2} * {i:02} = {input_number * i:03}")  #
    
