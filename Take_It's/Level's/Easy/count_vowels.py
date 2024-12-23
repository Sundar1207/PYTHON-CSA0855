# Accept a string from the user
string = input("Enter a string: ")

# Define vowels
vowels = "aeiouAEIOU"

# Initialize a counter for vowels
vowel_count = 0

# Loop through each character in the string
for char in string:
    if char in vowels:
        vowel_count += 1

# Print the number of vowels
print("Number of vowels =", vowel_count)
