# Find uncommon words from two strings.
str1 = "Hello how are you ?"
str2 = "Hello how is they !"
str1_sp = str1.split()
str2_sp = str2.split()
new_d = []
for i in str1_sp:
    if i not in str2_sp:
        new_d.append(i)
for i in str2_sp:
    if i not in str1_sp:
        new_d.append(i)
print("Uncommon words are : ",new_d)
