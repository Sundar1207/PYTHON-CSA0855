a=int(input("Enter the number : "))
tem=a
rem=0
num=0

while(a>0):
    rem=a%10
    num=(num*10)+rem
    a=a//10
print(num)
