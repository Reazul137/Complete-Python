lower = input("Enter lower range : ")
lower = int(lower)

upper = input("Enter upper range: ")
upper = int(upper)

n = input("Enter the number to be divided by : ")
n = int(n)

for i in range (lower, upper+1):
    if i % n == 0:
        print(i)
