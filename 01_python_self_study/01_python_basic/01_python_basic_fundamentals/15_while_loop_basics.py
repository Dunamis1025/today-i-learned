While Loop Example

# while loop
customer = "Thor"
count = 5

while count >= 1:
    print("{0}, your coffee is ready. {1} attempts remaining.".format(customer, count))
    count -= 1

    if count == 0:
        print("The coffee has been discarded.")

Output
Thor, your coffee is ready. 5 attempts remaining.
Thor, your coffee is ready. 4 attempts remaining.
Thor, your coffee is ready. 3 attempts remaining.
Thor, your coffee is ready. 2 attempts remaining.
Thor, your coffee is ready. 1 attempts remaining.
The coffee has been discarded.
