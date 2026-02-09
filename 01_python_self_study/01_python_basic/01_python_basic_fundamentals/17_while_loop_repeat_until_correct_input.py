# Repeat until the correct name is entered

customer_name = "Thor"
entered_name = "Unknown"

while entered_name != customer_name:
    print(f"{customer_name}, your coffee is ready.")
    entered_name = input("May I have your name, please? ")

✅ Example Output
Thor, your coffee is ready.
May I have your name, please? Iron Man
Thor, your coffee is ready.
May I have your name, please? I am Groot
Thor, your coffee is ready.
May I have your name, please? Thor
