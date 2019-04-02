year = input("Type the year value : ")
year = int(year)

if year % 100 != 0 and year % 4 == 0:
    print("Yes!!.. This is leap year!!")
elif year % 100 == 0 and year % 400 == 0:
    print("Yes!!.. This is leap year!!")
else:
    print("No!!.. This is not leap year!!")