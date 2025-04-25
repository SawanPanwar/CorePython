# Creating a sample tuple
t = (10, 20, 30, 20, 40, 10, 20)

print("Tuple:", t)

# 1. count(value)
print("Count of 20:", t.count(20))   # Output: 3

# 2. index(value)
print("Index of 30:", t.index(30))   # Output: 2

# Built-in functions that work with tuples

# 3. len()
print("Length of tuple:", len(t))    # Output: 7

# 4. max()
print("Maximum value:", max(t))      # Output: 40

# 5. min()
print("Minimum value:", min(t))      # Output: 10

# 6. sum()
print("Sum of all elements:", sum(t))  # Output: 150

# 7. sorted()
print("Sorted tuple:", sorted(t))    # Output: [10, 10, 20, 20, 20, 30, 40]

# 8. any()
print("Any non-zero?", any(t))       # Output: True

# 9. all()
print("All non-zero?", all(t))       # Output: True

# 10. tuple() constructor
l = [1, 2, 3]
new_tuple = tuple(l)
print("Tuple from list:", new_tuple)  # Output: (1, 2, 3)