#Write a program to demonstrate working with dictionaries in python. 
# Creating an empty Dictionary
Dict = { }
print("Empty Dictionary: ")
print(Dict)
# Adding elements one at a time
Dict[0] = 'zero'
Dict[2] = 'two'
Dict[3] = 1
print("\nDictionary after adding 3 elements: ")
print(Dict)
# Adding set of values to a single Key
Dict['Value_set'] = 2, 3, 4
print("\nDictionary after adding set of elements: ")
print(Dict)
# Updating existing Key's Value
Dict[2] = 'Welcome'
print("\nUpdated key value: ")
print(Dict)
# Deleting a Key value
del Dict[0]
print("\nDeleting a specific key: ")
print(Dict)

print(Dict.values())
print(Dict.keys())