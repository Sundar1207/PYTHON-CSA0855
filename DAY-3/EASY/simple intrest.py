def simple(p,year,ci):
    if ci=='y':
       intrest=(p*year*12)/100
    elif ci=='n' :
        interst=(p*year*10)/100
    else:
        return ("Enter valid option .")

    return intrest

p=float(input("Enter the princle : "))
year=float(input("Enter the year : "))
ci=str(input("Enter the citysen (y/n): "))

print(simple(p,year,ci))
