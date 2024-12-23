set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union: All elements from both sets
union_set = set1 | set2
print("Union:", union_set)

# Intersection: Common elements in both sets
intersection_set = set1 & set2
print("Intersection:", intersection_set)

# Difference: Elements in set1 but not in set2
difference_set = set1 - set2
print("Difference:", difference_set)

# Symmetric Difference: Elements in either set, but not both
symmetric_difference_set = set1 ^ set2
print("Symmetric Difference:", symmetric_difference_set)
