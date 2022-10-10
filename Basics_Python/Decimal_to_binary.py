def binary_number(num):
    return "{0:b}".format(int(num))


num = int(input("Enter the base 10 number : "))
print(binary_number(num))