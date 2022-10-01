import numpy as np
arr3 = np.array([21,56,98,2654,221,56,5,565,65,2,32,32])
li1 = arr3.tolist()

size = len(li1)
half = int(size/2)
l1=[]
l2=[]
for i in range(0,half):
    l1.append(li1[i])
for i in range(half,size):
    l2.append(li1[i])
new_li = l2+l1
new_arr = np.array(new_li)
print(new_arr)