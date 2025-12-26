# String Methods (lower, upper, find, index, etc.)

text = "Python is Amazing"

print(text.lower())          # Convert all characters to lowercase
print(text.upper())          # Convert all characters to uppercase
print(text[0].isupper())     # Check if the first character is uppercase
print(len(text))             # Get the length of the string
print(text.replace("Python", "Java"))  # Replace a substring

index = text.index("n")
print(index)

# Find the next occurrence of "n" starting after the previous index
index = text.index("n", index + 1)
print(index)

print(text.find("Java"))     # Returns -1 if the substring is not found

# print(text.index("Java"))  # Raises an error if the substring is not found

print("hi")  # This line is executed because find() does not raise an error

print(text.count("n"))      # Count how many times "n" appears in the string

output
python is amazing
PYTHON IS AMAZING
True
17
Java is Amazing
5
15
-1
hi
2

When using index() with a missing value
Traceback (most recent call last):
  File "practice.py", line 14, in <module>
    print(text.index("Java"))
ValueError: substring not found

text.find("Java")   # Returns -1 if not found (program continues)
text.index("Java")  # Raises ValueError if not found (program stops)
