nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
result = []

for i in nums:
    result.append(sum(1 for j in nums if j < i))

print("Output:", result)
