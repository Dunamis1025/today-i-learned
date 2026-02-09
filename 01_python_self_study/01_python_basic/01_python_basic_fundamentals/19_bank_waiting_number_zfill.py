# Bank waiting number system
# Output format: 001, 002, 003, ...

for num in range(1, 21):
    # Convert the number to a string
    num_str = str(num)

    # Pad the number with leading zeros to make it 3 digits long
    formatted_number = num_str.zfill(3)

    # Print the waiting number
    print("Waiting number :", formatted_number)


# result
Waiting number : 001
Waiting number : 002
Waiting number : 003
...
Waiting number : 019
Waiting number : 020
