# if statement

saarc = ["Bangladesh","bangladesh", "Afghanistan","afghanistan", "Bhutan","bhutan", "Nepal","nepal", "India","india", "Pakistan","pakistan", "SriLanka", "srilanka"]

country = input("Enter the name of the country : ")
if country in saarc:
    print(country, "is a member of SAARC")
else:
    print(country, "is not a member of SAARC")
print("Program terminated")