lower = int(input("Enter lower range limit"))
upper = int(input("Enter upper range limit"))

for i in range(lower, upper + 1):
    if i % 7 == 0:
        print(i)