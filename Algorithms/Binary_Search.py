l = [2,342,34,32,34,342,535,656,54,8,789,689,9,0,4,435,324,34,4]
l.sort()
print(l)
ele = int(input("Enter the element to be search : "))
def binary_search(l,ele):
    top = 0
    last = len(l)-1
    location = -1
    while(last>=top and location == -1):
        mid = int((top+last)/2)
        if l[mid] == ele:
            location = mid
        elif l[mid] > ele:
            last = mid-1
        else:
            top = mid+1
    return location
loc = binary_search(l,ele)
print(loc)
