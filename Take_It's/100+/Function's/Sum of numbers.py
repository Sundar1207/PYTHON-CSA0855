#Write a Python program to find the factorial of a number using a loop.
def sum_of(num):
  a=0
  for i in range(1,num+1):
      a+=i
  print(a)
  
num=int(input())
sum_of(num)
