str1 = "WriteaPythonprogramforremovingi-thcharacterfromastring"
i = int(input("Enter the position : "))
str_lt = [x for x in str1]
for j in range(0,len(str_lt)):
    if( i == j):
        str_lt.pop(j)
new_str = "".join([str(k) for k in str_lt] )
print(new_str)