def print_pattern():
    # Input from the user
    rows = input("Enter the number of rows: ").strip()

    if not rows.isdigit():
        print("Invalid input. Enter a positive integer.")
        return

    rows = int(rows)

    # Print the pattern
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(f"0.{j}", end=" ")
        print()

# Run the function
print_pattern()
