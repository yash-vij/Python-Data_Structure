def HCF(num1, num2):
    while (True):
        if (num1 < num2):
            smaller = num1
        else:
            smaller = num2
        for i in range(smaller, 0, -1):
            if (num1 % i == 0 and num2 % i == 0):
                hcf = i
                break
        break
    return hcf


print(HCF(2, 30))
print(HCF(332, 234))
print(HCF(12, 20))
print(HCF(12, 16))
print(HCF(24, 104))