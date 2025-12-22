📌 Python List Methods

This example demonstrates commonly used list methods in Python,
using a simple subway (train carriage) analogy.

🔹 Creating a List
subway = ["Alice", "Bob", "Charlie"]

🔹 Finding an Index
# Which position is Bob in?
print(subway.index("Bob"))
➡ Output: 1

🔹 Adding an Element (append)
# David gets on at the next station
subway.append("David")
print(subway)
➡ Output:['Alice', 'Bob', 'Charlie', 'David']

🔹 Inserting an Element (insert)
# Ethan gets on between Alice and Bob
subway.insert(1, "Ethan")
print(subway)
➡ Output: ['Alice', 'Ethan', 'Bob', 'Charlie', 'David']

🔹 Removing the Last Element (pop)
# One person gets off from the back
print(subway.pop())
print(subway)
➡ Output:David
['Alice', 'Ethan', 'Bob', 'Charlie']

🔹 Counting Elements (count)
# Alice gets on again
subway.append("Alice")
print(subway)
print(subway.count("Alice"))
➡ Output:
['Alice', 'Ethan', 'Bob', 'Charlie', 'Alice']
2

🔹 Sorting a List (sort)
num_list = [5, 2, 4, 3, 1]
num_list.sort()
print(num_list)
➡ Output:[1, 2, 3, 4, 5]

🔹 Reversing a List (reverse)
num_list.reverse()
print(num_list)
➡ Output:[5, 4, 3, 2, 1]

🔹 Clearing a List (clear)
num_list.clear()
print(num_list)
➡ Output:[]

🔹 Using Mixed Data Types
mix_list = ["Bob", 20, True]
print(mix_list)
➡ Output:['Bob', 20, True]

🔹 Extending a List (extend)
num_list = [5, 2, 4, 3, 1]
num_list.extend(mix_list)
print(num_list)
➡ Output:[5, 2, 4, 3, 1, 'Bob', 20, True]

