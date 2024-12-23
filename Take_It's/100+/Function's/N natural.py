
n = int(input("Enter a positive number: "))

if n > 0:
    # Calculate the sum
    total = sum(range(1, n + 1))
    print(f"The sum of the first {n} natural numbers is: {total}")
else:
    print("Please enter a positive number.")
