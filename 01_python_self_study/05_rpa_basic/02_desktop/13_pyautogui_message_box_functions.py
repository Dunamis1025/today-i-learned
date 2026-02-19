"""
File Name:
13_pyautogui_message_box_functions.py

📌 Today's Topic
Using PyAutoGUI message box functions for simple user interaction.

These functions allow interaction between the user and an automation script.
They are much simpler than creating GUI windows using tkinter.

Useful for:
- Confirming execution before automation starts
- Receiving user input (e.g., filenames)
- Asking for passwords
- Displaying warnings or notices
"""

import pyautogui


# -----------------------------------------------------------
# 1️⃣ alert() - Simple Alert Box
# -----------------------------------------------------------
"""
✔ Displays a message with only an "OK" button
✔ Commonly used for warnings or notifications

Syntax:
pyautogui.alert("Message content", "Window title")
"""

# pyautogui.alert("Automation failed.", "Warning")


# -----------------------------------------------------------
# 2️⃣ confirm() - Confirmation Box
# -----------------------------------------------------------
"""
✔ Displays "OK" and "Cancel" buttons
✔ Returns the user's selection as a string

Return values:
- "OK"
- "Cancel"

Syntax:
result = pyautogui.confirm("Question", "Window title")
"""

# result = pyautogui.confirm("Do you want to continue?", "Confirmation")
# print(result)


# -----------------------------------------------------------
# 3️⃣ prompt() - Text Input Box
# -----------------------------------------------------------
"""
✔ Allows the user to enter text
✔ Returns the entered value as a string

Syntax:
result = pyautogui.prompt("Enter something", "Input")
"""

# result = pyautogui.prompt("Enter the file name:", "Input")
# print(result)


# -----------------------------------------------------------
# 4️⃣ password() - Password Input Box
# -----------------------------------------------------------
"""
✔ Masks input characters with dots (●●●)
✔ Returns the actual value as a string

⚠ Note:
In real applications, avoid hardcoding passwords.
This example is for learning purposes only.

Syntax:
result = pyautogui.password("Enter password")
"""

result = pyautogui.password("Enter your password:")
print("Entered password:", result)


# -----------------------------------------------------------
# 💡 Practical Example (Using condition with password)
# -----------------------------------------------------------
"""
Example:
Verify password before starting automation
"""

"""
password = pyautogui.password("Enter admin password:")

if password != "1234":
    pyautogui.alert("Access denied.", "Warning")
else:
    pyautogui.alert("Access granted.", "Info")
"""
