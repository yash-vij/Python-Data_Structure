# If a string contains a soecial character.
st = "Write a P^ython P(rogram to check% if a string$ contains #a@ny special character"
special = "[@_!#$%^&*()<>?/\|}{~:]"
spe_used = []
count = 0
data = [d for d in st]
data
for i in range(len(data)):
    if (data[i] in special):
        spe_used.append(data[i])
        count = count + 1
if count > 0:
    print("Special character is used")
    print("Special characters are :", spe_used)
else:
    print("Special character is not used")
