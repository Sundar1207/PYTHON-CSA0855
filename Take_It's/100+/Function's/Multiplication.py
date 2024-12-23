#. Write a Python program to print the multiplication table of a given number.
def mul(num,x):
  for i in range(x,11):
    print(f"{i} X {num} = {num*i}")
num=12
x=1
mul(num,x)
