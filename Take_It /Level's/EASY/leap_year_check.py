year = int(input("Enter the year: "))

if year % 400 == 0:
    print("Leap Year:", year)
elif year % 100 == 0:
    print("Given year is NonLeap Year")
elif year % 4 == 0:
    print("Leap Year:", year)
else:
    print("Given year is NonLeap Year")
