myString = "This is my string"
newString = ""

for i in range(len(myString)):
    if i % 2 == 0:
        newString = newString + myString[i].lower()

    else:
        newString = newString + myString[i].upper()

print(newString)
