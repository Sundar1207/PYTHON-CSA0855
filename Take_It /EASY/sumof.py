a=int(input("sum of two degit,\nNow enter the value :"))
rem=0
c=0
while a>1:
    rem=a%10
    c+=rem
    a=a//10
print(c)
