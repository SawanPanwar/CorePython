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

# fromkeys() - Returns a dictionary with specified keys and their associated values
keys = ['e', 'f', 'g']
default_value = 0
new_dict = dict.fromkeys(keys, default_value)
print("New dictionary with fromkeys():", new_dict)

# get() - Returns the value associated with the specified key
print("Value for key 'b':", dict_example.get('b'))  # Output: 2

# items() - Returns a view object displaying the dictionary's key-value pairs
print("Dictionary items:", dict_example.items())

# keys() - Returns a view object displaying all the dictionary's keys
print("Dictionary keys:", dict_example.keys())

# pop() - Removes the specified key and returns the associated value
popped_value = dict_example.pop('b')
print("Popped value for key 'b':", popped_value)
print("Dictionary after pop():", dict_example)

# popitem() - Removes and returns the last key-value pair
last_item = dict_example.popitem()
print("Popped last item:", last_item)
print("Dictionary after popitem():", dict_example)

# setdefault() - Returns the value for the specified key, and if not found, inserts it with a default value
print("Value for key 'z' with setdefault:", dict_example.setdefault('z', 100))
print("Dictionary after setdefault():", dict_example)

# update() - Updates the dictionary with elements from another dictionary or iterable
new_data = {'x': 10, 'y': 20}
dict_example.update(new_data)
print("Dictionary after update():", dict_example)

# values() - Returns a view object displaying all the dictionary's values
print("Dictionary values:", dict_example.values())
