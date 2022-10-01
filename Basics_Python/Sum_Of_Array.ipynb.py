import numpy as np

sum = 0
a = int(input("Enter the size of array : "))
arr = np.empty(a)
print("Enter array element : ")
for i in range(0,a):
    ele = int(input())
    arr = np.append(arr,ele)
    sum = sum + ele
print("Sum of the array is : ",sum)