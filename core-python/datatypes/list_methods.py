# Initial list with multiple data types
items = ['apple', 42, True, 3.14]
print("Original List:", items)

# 1. append(x)
# Adds an element to the end of the list
items.append(False)
print("After append(False):", items)

# 2. extend(iterable)
# Adds multiple elements to the end of the list
items.extend(['banana', 100, 2.71])
print("After extend(['banana', 100, 2.71]):", items)

# 3. insert(i, x)
# Inserts an element 'x' at the specified index 'i'
items.insert(1, 'inserted')
print("After insert at index 1:", items)

# ✅ Safe to check index/count before removal or popping
# 4. index(x)
# Finds the index of the first occurrence of the specified element 'x'
index_of_42 = items.index(42)
print("Index of 42:", index_of_42)

# 5. count(x)
# Returns the count of how many times element 'x' appears in the list
count_of_100 = items.count(100)
print("Count of 100:", count_of_100)

# 6. remove(x)
# Removes the first occurrence of the specified element 'x' from the list
items.remove(True)
print("After remove(True):", items)

# 7. pop([i])
# Removes and returns the item at the specified index 'i'. If no index is provided, it removes the last item.
popped = items.pop(2)
print("After pop(2):", items, "| Popped item:", popped)

# Removes and returns the last item in the list
last = items.pop()
print("After pop():", items, "| Last popped:", last)

# 8. clear()
# Removes all items from the list, leaving an empty list
copy_items = items.copy()
copy_items.clear()
print("After clear():", copy_items)

# 9. sort()
# Sorts the elements of the list in ascending order. Works only if all elements are comparable (e.g., integers, floats)
only_numbers = [3, 1.5, 2, 4.5]
only_numbers.sort()
print("Sorted numbers:", only_numbers)

# 10. reverse()
# Reverses the order of the elements in the list
items.reverse()
print("After reverse():", items)

# 11. copy()
# Creates a shallow copy of the list
copied = items.copy()
print("Copied list:", copied)

# Final State
# Displays the final state of the list after all operations
print("Final items list:", items)