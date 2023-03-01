# def prime_check(number):
myList = [1, 4, 13, 30, 19, 70, 80 , 100]
myResult = []
for num in myList:
    if num == 0 or num == 1:
        continue
    for i in range(2, num//2 + 1):
        if num % i == 0:
            break
    else:
        myResult.append(num)
if len(myResult):
    print("Prime number is : ")
    for ans in myResult:
        print(ans, end = ", ")
else:
    print("No any number from the given list is prime")

