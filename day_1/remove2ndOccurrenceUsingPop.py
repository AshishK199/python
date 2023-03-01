myList = [1, 2, 3, 1, 4, 5, 1]
myCount = myList.count(1)

if myCount >= 2:
    myIndex = myList.index(1, myList.index(1) + 1)
    myList.pop(myIndex)

print(myList)