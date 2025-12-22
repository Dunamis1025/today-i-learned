# Python Dictionary Basics
# (Get, Add, Update, Delete)
#
# Example: Office locker assignment system
# Key   -> Locker ID
# Value -> Employee name


# 🔹 Creating a Dictionary
lockers = {"A-3": "Alice", "B-100": "Bob"}

print(lockers["A-3"])
print(lockers["B-100"])
# Output:
# Alice
# Bob


# 🔹 Using get()
print(lockers.get("A-3"))
print(lockers.get("C-20"))
print(lockers.get("C-20", "Available"))
print("hi")
# Output:
# Alice
# None
# Available
# hi


# 🔹 Checking if a Key Exists
print("A-3" in lockers)
print("C-20" in lockers)
# Output:
# True
# False


# 🔹 Updating and Adding Entries
print(lockers)
lockers["A-3"] = "Charlie"   # Update
lockers["C-20"] = "David"    # Add
print(lockers)
# Output:
# {'A-3': 'Alice', 'B-100': 'Bob'}
# {'A-3': 'Charlie', 'B-100': 'Bob', 'C-20': 'David'}


# 🔹 Deleting an Entry
del lockers["A-3"]
print(lockers)
# Output:
# {'B-100': 'Bob', 'C-20': 'David'}


# 🔹 Printing Keys Only
print(lockers.keys())
# Output:
# dict_keys(['B-100', 'C-20'])


# 🔹 Printing Values Only
print(lockers.values())
# Output:
# dict_values(['Bob', 'David'])


# 🔹 Printing Key-Value Pairs
print(lockers.items())
# Output:
# dict_items([('B-100', 'Bob'), ('C-20', 'David')])


# 🔹 Clearing the Dictionary
lockers.clear()
print(lockers)
# Output:
# {}

