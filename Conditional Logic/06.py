# Leap year
year = input("Type the year : ")
year = int(year)

if year % 4 != 0:
    print("This is not a Leap Year")
else:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Yes this is a leap year")
        else:
            print("This is not a leap year")

