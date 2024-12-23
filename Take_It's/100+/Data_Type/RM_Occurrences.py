numbers=list(map(int,input().split()))
remove=int(input())

while n in numbers:
  numbers.remove(remove)
print(numbers)
