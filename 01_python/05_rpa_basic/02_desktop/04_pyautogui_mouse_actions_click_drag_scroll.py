"""
📌 pyautogui – Mouse Actions: Click, Drag, Scroll

This file documents the core mouse actions available in
Python's pyautogui library.

Topics covered:
1️⃣ Pausing execution using sleep
2️⃣ Checking the current mouse cursor position
3️⃣ Mouse clicking (single, double, multiple clicks)
4️⃣ Holding and releasing the mouse button
5️⃣ Dragging with mouseDown/mouseUp
6️⃣ Right-click and middle-click
7️⃣ Dragging using drag() and dragTo()
8️⃣ Scrolling the mouse wheel

⚠️ Important Notes:
- pyautogui controls the real mouse cursor.
- Always verify coordinates before running scripts.
- Use sleep() and duration to avoid unexpected behavior.
"""

import pyautogui


# ==================================================
# 1️⃣ Pause execution (sleep)
# ==================================================
# sleep(seconds)
# → Pauses the script for a given number of seconds.
# → Useful to prepare the screen before automation starts.

pyautogui.sleep(3)  # Wait for 3 seconds


# ==================================================
# 2️⃣ Get current mouse cursor position
# ==================================================
# position() returns the current mouse coordinates as (x, y).

# print(pyautogui.position())
# Example output: Point(x=1276, y=449)


# ==================================================
# 3️⃣ Mouse click actions
# ==================================================
# click()
# → Single click at the current cursor position

# pyautogui.click()

# click(x, y, duration)
# → Move to (x, y) and click

# pyautogui.click(64, 17, duration=1)


# ==================================================
# 4️⃣ Mouse button control (press & release)
# ==================================================
# mouseDown() → Press and hold the mouse button
# mouseUp()   → Release the mouse button

# pyautogui.mouseDown()
# pyautogui.mouseUp()


# ==================================================
# 5️⃣ Double click & multiple clicks
# ==================================================
# doubleClick()
# → Perform a double click

# pyautogui.doubleClick()

# clicks parameter
# → Perform multiple clicks (use with caution)

# pyautogui.click(clicks=500)  # Click 500 times (dangerous)


# ==================================================
# 6️⃣ Drag using mouseDown + move + mouseUp
# ==================================================
# Simulates click-and-drag behavior manually

# pyautogui.moveTo(400, 400)
# pyautogui.mouseDown()       # Hold mouse button
# pyautogui.moveTo(500, 500)  # Move while holding
# pyautogui.mouseUp()         # Release button


# ==================================================
# 7️⃣ Right-click & middle-click
# ==================================================
# pyautogui.rightClick()   # Right mouse button click
# pyautogui.middleClick()  # Middle (wheel) button click


# ==================================================
# 8️⃣ Drag using drag() and dragTo()
# ==================================================
# drag(x, y)
# → Drag relative to the current position

# pyautogui.drag(100, 0)

# If the drag is too fast, use duration
# pyautogui.drag(100, 0, duration=0.25)

# dragTo(x, y)
# → Drag to an absolute screen position

# pyautogui.dragTo(1514, 349, duration=0.25)


# ==================================================
# 9️⃣ Mouse scroll
# ==================================================
# scroll(amount)
# → Positive value: scroll up
# → Negative value: scroll down

pyautogui.scroll(300)    # Scroll up
pyautogui.scroll(-300)   # Scroll down


# ==================================================
# ✨ Key Summary
# ==================================================
# ✔ sleep()        : Pause script execution
# ✔ position()     : Get current mouse coordinates
# ✔ click()        : Single / multiple clicks
# ✔ mouseDown/Up() : Control mouse button state
# ✔ drag / dragTo  : Drag mouse
# ✔ rightClick()   : Right-click
# ✔ middleClick()  : Middle button click
# ✔ scroll()       : Mouse wheel control
#
# → Core building blocks for desktop automation and macros
