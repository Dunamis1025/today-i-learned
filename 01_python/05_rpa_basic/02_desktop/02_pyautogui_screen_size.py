"""
📌 pyautogui Screen Size (Resolution) – Fundamentals

This script demonstrates how to retrieve the current screen resolution
(width and height) using the pyautogui library.

Understanding screen size is a critical first step when working with:
- Desktop automation
- Mouse movement and clicking
- UI interaction scripts
- RPA (Robotic Process Automation)

If you know your screen resolution, you can precisely control
where the mouse moves and where actions are performed.
"""

# ==================================================
# 1️⃣ What is pyautogui?
# ==================================================
# pyautogui is a Python library that allows you to:
# - Move the mouse
# - Click the mouse
# - Type using the keyboard
# - Capture the screen
# - Read pixel colors
#
# In simple terms:
# pyautogui lets Python control the computer
# the same way a human uses a mouse and keyboard.


# ==================================================
# 2️⃣ Import pyautogui
# ==================================================
import pyautogui

# You must import pyautogui before using any of its functions.


# ==================================================
# 3️⃣ Get the screen size
# ==================================================
# pyautogui.size()
# → Returns the current screen resolution.
#
# Return type:
# Size(width=<screen_width>, height=<screen_height>)

size = pyautogui.size()


# ==================================================
# 4️⃣ Print the result
# ==================================================
# Example output:
# Size(width=1920, height=1080)
#
# This means:
# - Screen width  = 1920 pixels
# - Screen height = 1080 pixels

print(size)


# ==================================================
# 5️⃣ Access width and height separately
# ==================================================
# The size object behaves like a tuple.

# Screen width (horizontal size)
# size[0]
width = size[0]

# Screen height (vertical size)
# size[1]
height = size[1]

print("Screen width:", width)
print("Screen height:", height)


# ==================================================
# 6️⃣ Why is this important?
# ==================================================
# Knowing the screen size allows you to calculate positions.
#
# Example:
# pyautogui.moveTo(100, 100)
# → Move mouse near the top-left corner
#
# pyautogui.moveTo(width // 2, height // 2)
# → Move mouse to the center of the screen
#
# Without screen size information,
# precise mouse automation is not possible.


# ==================================================
# 7️⃣ Summary
# ==================================================
# ✔ pyautogui.size() returns the current screen resolution
# ✔ The result contains (width, height)
# ✔ width  = size[0]
# ✔ height = size[1]
# ✔ This is the foundation of all desktop automation
#
# Think of this file as the starting point
# for pyautogui-based automation scripts.
