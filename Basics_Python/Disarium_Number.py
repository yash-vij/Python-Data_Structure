num = int(input("Enter the number : "))
num2 = num
size = len(str(num))
sum = 0
while size >0:
    m = num%10
    sum = sum + (m**size)
    num = int(num /10)
    size -= 1
if num2 == sum:
    print("Number is Disarium")
else:
    print("Number is not disarium")