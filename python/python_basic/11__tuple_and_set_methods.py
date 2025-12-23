# This file demonstrates how tuples and sets work in Python.
# Each example shows the expected output right below the code.
# ============================================


# ----------------------------
# Tuple Practice
# ----------------------------

# Creating a tuple
menu = ("Pork Cutlet", "Cheese Cutlet")

# Accessing tuple elements
print(menu[0])
# Result -> Pork Cutlet

print(menu[1])
# Result -> Cheese Cutlet


# Tuple unpacking
(name, age, hobby) = ("Tony Stark", 45, "Engineering")
print(name, age, hobby)
# Result -> Tony Stark 45 Engineering


# ----------------------------
# Set Practice
# ----------------------------

# Creating a set (duplicates are removed automatically)
my_set = {1, 2, 3, 3, 3}
print(my_set)
# Result -> {1, 2, 3}


# Two developer groups (Avengers theme)
java = {"Iron Man", "Captain America", "Hulk"}
python = set(["Iron Man", "Spider-Man"])


# ----------------------------
# Set Operations
# ----------------------------

# Intersection: developers who know both Java and Python
print(java & python)
# Result -> {'Iron Man'}

print(java.intersection(python))
# Result -> {'Iron Man'}


# Union: developers who know Java or Python
print(java | python)
# Result -> {'Iron Man', 'Captain America', 'Hulk', 'Spider-Man'}

print(java.union(python))
# Result -> {'Iron Man', 'Captain America', 'Hulk', 'Spider-Man'}


# Difference: Java developers who do NOT know Python
print(java - python)
# Result -> {'Captain America', 'Hulk'}

print(java.difference(python))
# Result -> {'Captain America', 'Hulk'}


# ----------------------------
# Modifying Sets
# ----------------------------

# A new Python developer is added
python.add("Captain America")
print(python)
# Result -> {'Iron Man', 'Spider-Man', 'Captain America'}

# Someone forgot Java
java.remove("Captain America")
print(java)
# Result -> {'Iron Man', 'Hulk'}


# ----------------------------
# Converting Data Structures
# ----------------------------

# Coffee shop menu example
menu = {"Coffee", "Milk", "Juice"}
print(menu, type(menu))
# Result -> {'Coffee', 'Milk', 'Juice'} <class 'set'>


# Convert set to list
menu = list(menu)
print(menu, type(menu))
# Result -> ['Coffee', 'Milk', 'Juice'] <class 'list'>


# Convert list to tuple
menu = tuple(menu)
print(menu, type(menu))
# Result -> ('Coffee', 'Milk', 'Juice') <class 'tuple'>


# Convert tuple back to set
menu = set(menu)
print(menu, type(menu))
# Result -> {'Coffee', 'Milk', 'Juice'} <class 'set'>
