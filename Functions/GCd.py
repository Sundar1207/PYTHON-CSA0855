def gcd(a, b):
    while b:
        a, b = b, a % b  # Swap and take the remainder
    return a

# Example usage
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print(f"The GCD of {num1} and {num2} is: {gcd(num1, num2)}")
