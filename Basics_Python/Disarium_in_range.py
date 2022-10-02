for i in range(1,101):
    num2 = i
    size = len(str(i))
    sum = 0
    while size >0:
        m = i%10
        sum = sum + (m**size)
        i = int(i /10)
        size -= 1
    if num2 == sum:
        print(num2," ")