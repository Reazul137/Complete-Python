lower = input("Enter the lower limit for the range : ")
lower = int(lower)

upper = input("Enter the upper limit for the range : ")
upper = int(upper)

for i in range ( lower, upper+1):
    if i %2 != 0:
        print(i)