# Example with List
list = [5, "hello", 3.14, True, 10, "world", False, 25, 10, 30]

# append() - Adds an element at the end of the list
list.append(35)
print("List after append(35):", list)

# clear() - Removes all items from the list
list.clear()
print("List after clear():", list)

# copy() - Returns a shallow copy of the list
list = [5, "hello", 3.14, True, 10, "world", False, 25, 10, 30]
list_copy = list.copy()
print("List copy:", list_copy)

# insert() - Inserts an element at the specified index
list.insert(2, "inserted_value")
print("List after insert(2, 'inserted_value'):", list)

# pop() - Removes and returns an element at the specified index (default is the last item)
removed_item = list.pop()
print("Removed item with pop():", removed_item)
print("List after pop():", list)

# reverse() - Reverses the order of the list
list.reverse()
print("List after reverse():", list)

# sort() - Sorts the list in ascending order
# Note: This will cause an error because the list contains mixed data types (int, str, etc.)
# To demonstrate sorting properly, we'll use only numeric elements for the sort
numeric_list = [5, 10, 25, 15, 30]
numeric_list.sort()
print("Numeric list after sort():", numeric_list)