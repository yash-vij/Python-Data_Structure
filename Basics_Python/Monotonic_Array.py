import numpy as np
arr4 = np.array([1,2,3,4,5,6,7,8,9])
l4 = arr4.tolist()
l5, l6 = [],[]
l5.extend(l4)
l6.extend(l5)
l5.sort()
l6.sort(reverse=True)
if(l5 == l4 or l6 == l4):
    print("Array is monotonic")
else:
    print("Array is not monotonic")