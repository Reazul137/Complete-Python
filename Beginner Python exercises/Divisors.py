__author__="Reazul Islam"

num = int (input("Please chose a number to divide : "))

listRange = list(range(1, num+1))
divisorList = []

for number in listRange:
    if num % number == 0:
        divisorList.append(number)
        
        print(divisorList)