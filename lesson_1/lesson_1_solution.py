"""
Create a list with combination of both - strings and numbers
Iterate over this list and print whether element is a string or a number
"""

elements = [1, 2, 5.3, "test", "les", 141]

for elem in elements:
    if isinstance(elem, (int, float)):
        print(f"{elem} is a number")
    elif isinstance(elem, str):
        print(f"{elem} is a string")

"""
Create a dictionary and iterate over its elements
"""

elements = {
    "apple": 10,
    "banana": 3,
    "strawberry": 12
}

for key, value in elements.items():
    print(f"{key}: {value}")

"""
Create dictionary with counts of items in this list:

["milk", "egg", "milk", "egg", "egg", "meat", "cream", "meat"] 

and print it in sorted order
"""

elements = ["milk", "egg", "milk", "egg", "egg", "meat", "cream", "meat"]
dictionary = dict()

for element in elements:
    if element in dictionary:
        dictionary[element] += 1
    else:
        dictionary.update({element: 1})

print(sorted(dictionary.items(), key=lambda x: x[1], reverse=True))

"""
Sort following list of tuple by first member in tuple:
[(1, 30), (5, 456), (2, 44), (6, 221), (3, 545), (4, 545)]
"""
original_list = [(1, 30), (5, 456), (2, 44), (6, 221), (3, 545), (4, 545)]
sorted_list = sorted(original_list, key=lambda x: x[0])
print(sorted_list)
