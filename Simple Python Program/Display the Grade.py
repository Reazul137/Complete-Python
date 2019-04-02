sub1 = input("Enter marks of the first subject : ")
sub1 = int(sub1)

sub2 = input("Enter marks of the second subject : ")
sub2 = int(sub2)

sub3 = input("Enter marks of the third subject : ")
sub3 = int(sub3)

sub4 = input("Enter marks of the fourth subject : ")
sub4 = int(sub4)

sub5 = input("Enter marks of the fifth subject : ")
sub5 = int(sub5)

avg = (sub1 + sub2 + sub3 + sub4 + sub5) / 5

if avg >= 90:
    print("Grade : A")
elif avg >= 80 and avg < 90:
    print("Grade : B")
elif avg >= 70 and avg < 80:
    print("Grade : C")
elif avg >= 60 and avg <70:
    print("Grade : D")
else:
    print("Grade : F")




