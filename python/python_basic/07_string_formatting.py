📌 Python String Formatting Examples


This repository demonstrates four common ways to format strings in Python:

1. % formatting (old style)
2. str.format() (basic)
3. str.format() with named arguments
4. f-strings (modern & recommended)


🔹 Method 1: % Formatting (Old Style)
print("I am %d years old." % 20)
print("I like %s." % "Python")
print("Apple starts with %c." % "A")

%d → integer
%s → string
%c → single character


🔹 Method 2: format() with Position
print("I am {} years old.".format(20))
print("I like {} and {}.".format("blue", "red"))
print("I like {0} and {1}.".format("blue", "red"))
print("I like {1} and {0}.".format("blue", "red"))

{} inserts values in order
{0}, {1} allow you to control the position


🔹 Method 3: format() with Named Arguments
print("I am {age} years old, and I like {color}.".format(age=20, color="red"))

Improves readability
Useful when there are many variables


🔹 Method 4: f-string (Recommended – Python 3.6+)
age = 20
color = "red"
print(f"I am {age} years old, and I like {color}.")

✅ Most readable
✅ Fast
✅ Widely used in modern Python


🖨️ Output
I am 20 years old.
I like Python.
Apple starts with A.
I am 20 years old.
I like blue and red.
I like blue and red.
I like red and blue.
I am 20 years old, and I like red.
I am 20 years old, and I like red.
