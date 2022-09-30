a = int(input())
print("Binary number : ")
def binary(a):
    count = 0
    num=0
    while(a>0):
        rem = a%2
        a = int(a/2)
        num = (rem*(10**count))+num
        count = count+1
    return num
def octal(a):
    count = 0
    num=0
    while(a>0):
        rem = a%8
        a = int(a/8)
        num = (rem*(10**count))+num
        count = count+1
    return num
def hexa(a):
    count = 0
    num=0
    while(a>0):
        rem = a%16
        a = int(a/16)
        num = (rem*(10**count))+num
        count = count+1
    return num
print("Binary : ",binary(a)," Octal : ",octal(a)," Hexa : ",hexa(a))