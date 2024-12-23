def second_largest(lst):
    lst = list(set(lst))  # Remove duplicates
    if len(lst) < 2:  # If there are fewer than 2 unique elements
        return None
    lst.sort()  # Sort the list
    return lst[-2]  # Return the second largest element

# Example usage
numbers = [12, 35, 1, 10, 34, 1]
print(f"The second largest element is: {second_largest(numbers)}")
