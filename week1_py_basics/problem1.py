def rotate(str1, str2):
    concat = str1 + str1
    return str2 in concat
str1 = input("enter first string: ")
str2 = input("enter second string: ")
print(rotate(str1, str2))