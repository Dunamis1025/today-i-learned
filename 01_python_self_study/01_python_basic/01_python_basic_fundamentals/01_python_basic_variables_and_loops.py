# Basic coding practice


# Variables
animal = "dog"
name = "Yeontan"
age = 4
hobby = "walking"
is_adult = age >= 3

print("Our " + animal + "'s name is " + name)
hobby = "playing with a ball"
print(name + " is " + str(age) + " years old, and loves " + hobby)
print("Is " + name + " an adult? " + str(is_adult))


# Practice
stations = ["Sadang", "Sindorim", "Incheon Airport"]
for station in stations:
    print("{0} train is now arriving.".format(station))


# Output
# Sadang train is now arriving.
# Sindorim train is now arriving.
# Incheon Airport train is now arriving.
