num = int(input("Enter the number : "))
lis = []

a=0
while(a == 0):
    sum=0
    while(num > 0):
        dig = num % 10
        sum = sum + (dig**2)
        num = int(num/10)
    if(sum in lis or sum == 1):
        a = 1
    else:
        si = len(lis)
        lis.insert(si,sum)
        num = sum
if(sum == 1):
    print("Number is a Happy number.")
else:
    print("Number is not a Happy number.")