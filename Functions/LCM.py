import math

# Function to find LCM
def find_lcm(num1, num2):
    return abs(num1 * num2) // math.gcd(num1, num2)

# Input from the user
a = int(input())
b = int(input())

# Validate input
if a > 0 and b > 0:
    lcm = find_lcm(a, b)
    print(f"The LCM of {a} and {b} is: {lcm}")
else:
    print("Please enter positive integers.")
