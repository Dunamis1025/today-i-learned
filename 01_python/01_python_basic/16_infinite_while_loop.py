# infinite loop
customer = "Iron Man"
call_count = 1

while True:
    print("{0}, your coffee is ready. Call number {1}".format(customer, call_count))
    call_count += 1

Output
Iron Man, your coffee is ready. Call number 98143
Iron Man, your coffee is ready. Call number 98144
Iron Man, your coffee is ready. Call number 98145
Iron Man, your coffee is ready. Call number 98146
...

Press Ctrl + C to stop the program.
