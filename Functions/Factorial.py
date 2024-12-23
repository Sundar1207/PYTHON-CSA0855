#Write a Python program to find the factorial of a number using a loop.
def fact(num):
  
  a=1
  for i in range(1,num+1):
      a*=i
  print(a)
  
num=int(input())
fact(num)
