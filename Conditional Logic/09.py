year = input("Please enter the year : ")
year = int(year)

if year % 400 == 0:
    print("Yes, This year is leap year.")
elif year % 100 == 0:
    print("No, This is not Leap Year.")
elif year % 4 == 0:
    print("Yes, This is is leap year.")
else:
    print("No, This year is not a leap year.")