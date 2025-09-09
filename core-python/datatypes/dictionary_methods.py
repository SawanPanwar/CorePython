# Example with Dictionary
dict_example = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# clear() - Removes all items from the dictionary
dict_example.clear()
print("Dictionary after clear():", dict_example)

# Reinitialize dictionary for other examples
dict_example = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# copy() - Returns a shallow copy of the dictionary
dict_copy = dict_example.copy()
print("Dictionary copy:", dict_copy)

# get() - Returns the value associated with the specified key
print("Value for key 'b':", dict_example.get('b'))  # Output: 2

# keys() - Returns a view object displaying all the dictionary's keys
print("Dictionary keys:", dict_example.keys())

# values() - Returns a view object displaying all the dictionary's values
print("Dictionary values:", dict_example.values())

# pop() - Removes the specified key and returns the associated value
popped_value = dict_example.pop('b')
print("Popped value for key 'b':", popped_value)
print("Dictionary after pop():", dict_example)