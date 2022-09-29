l = []
a = int(input("Enter the number of elements to find their LCM : "))
print("Enter elements : ")
for i in range(0, a):
    ele = int(input())
    l.append(ele)


def lcm(num1, num2):
    if (num1 > num2):
        greater = num1
    else:
        greater = num2
    while (True):

        if (greater % num1 == 0) and (greater % num2 == 0):
            lcm = greater
            break
        else:
            greater = greater + 1
    return lcm

print("Data is : ", l)
lc = l[0]
for i in range(1, len(l)):
    lc = lcm(lc, l[i])
print("LCM is : ", lc)