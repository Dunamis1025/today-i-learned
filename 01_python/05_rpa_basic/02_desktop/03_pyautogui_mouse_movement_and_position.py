"""
📌 pyautogui – Mouse Cursor Control Basics

This file is a beginner-friendly study note covering
how to control the mouse cursor using Python's pyautogui library.

Topics covered:
1️⃣ Moving the mouse to an absolute position
2️⃣ Moving the mouse relative to the current cursor position
3️⃣ Controlling mouse movement speed using duration
4️⃣ Printing the current mouse cursor coordinates to the terminal

⚠️ Important Notes:
- pyautogui controls the real mouse cursor on your system.
- Always use the `duration` option while testing to avoid sudden movements.
- This module is commonly used for automation, macros, and UI testing.
"""

import pyautogui

# ==================================================
# 1️⃣ Moving the mouse using absolute coordinates (moveTo)
# ==================================================
# moveTo(x, y)
# → Moves the mouse cursor to a specific screen position.
# → The top-left corner of the screen is (0, 0).

# pyautogui.moveTo(200, 100)
# Moves instantly to x=200, y=100

# pyautogui.moveTo(100, 200, duration=5)
# Moves smoothly to (100, 200) over 5 seconds


# ==================================================
# 2️⃣ Controlling mouse movement speed (duration)
# ==================================================
# The duration parameter allows smooth, human-like movement.

# pyautogui.moveTo(100, 100, duration=0.25)
# pyautogui.moveTo(200, 200, duration=0.25)
# pyautogui.moveTo(300, 300, duration=0.25)
# Moves diagonally with smooth transitions


# ==================================================
# 3️⃣ Moving the mouse relative to its current position (move)
# ==================================================
# move(x, y)
# → Moves the mouse relative to its current position.

# pyautogui.moveTo(100, 100, duration=0.25)
# print(pyautogui.position())  # Point(x=100, y=100)

# pyautogui.move(100, 100, duration=0.25)
# Moves +100, +100 from the current position → (200, 200)

# print(pyautogui.position())  # Point(x=200, y=200)

# pyautogui.move(100, 100, duration=0.25)
# Moves again → (300, 300)

# print(pyautogui.position())  # Point(x=300, y=300)


# ==================================================
# 4️⃣ Getting the current mouse cursor position
# ==================================================
# position() returns the current mouse cursor coordinates.

p = pyautogui.position()

# Method 1: Access using index
print(p[0], p[1])  # x, y

# Method 2: Access using attributes (recommended)
print(p.x, p.y)    # x, y


# ==================================================
# ✨ Key Summary
# ==================================================
# ✔ moveTo(x, y)  → Move to an absolute screen position
# ✔ move(x, y)    → Move relative to the current position
# ✔ duration      → Control movement speed (seconds)
# ✔ position()    → Get current mouse cursor coordinates
#
# → Essential foundation for desktop automation and UI scripting
