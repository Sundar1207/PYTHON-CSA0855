# Get user input
month, day = input("Enter the month and day (e.g., Mar 20): ").split(",")
print(type(month))
day = int(day)

# Determine the season
if (month == "Mar" and day >= 20) or (month == "Apr" or month == "May") or (month == "Jun" and day < 21):
    print("Spring")
elif (month == "Jun" and day >= 21) or (month == "Jul" or month == "Aug") or (month == "Sep" and day < 22):
    print("Summer")
elif (month == "Sep" and day >= 22) or (month == "Oct" or month == "Nov") or (month == "Dec" and day < 21):
    print("Fall")
else:
    print("Winter")
