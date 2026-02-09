"""
📌 PyAutoGUI Basics: mouseInfo(), FAILSAFE, PAUSE, move(), sleep()

This file documents the basic concepts of PyAutoGUI for mouse automation.

What I learned in this script:

1) pyautogui.mouseInfo()
   - Opens a small window that shows the current mouse cursor position (x, y)
     and the RGB color of the pixel under the cursor in real time.
   - Very useful when you need to know exact coordinates or color values
     before automating mouse clicks or movements.

2) FAILSAFE (Safety Mechanism)
   - By default, PyAutoGUI has a safety feature enabled (FAILSAFE = True).
   - If the automation runs out of control, you can instantly stop it
     by moving the mouse cursor to any corner of the screen.
   - If you set pyautogui.FAILSAFE = False, this safety mechanism is disabled,
     meaning the script will not stop even if you move the mouse to a corner.
     ⚠️ This is NOT recommended unless you fully understand the risks.

3) PAUSE (Global Delay Between Actions)
   - pyautogui.PAUSE = 1 adds a 1-second delay after EVERY PyAutoGUI action.
   - This helps prevent actions from running too fast and makes debugging easier.
   - This is different from pyautogui.sleep(1), which pauses execution only
     at a specific point where you explicitly place it.

4) move() and sleep() for Repeated Mouse Movement
   - pyautogui.move(100, 100) moves the mouse cursor relatively:
     100 pixels to the right and 100 pixels downward from the current position.
   - Using a for-loop allows repeating this movement multiple times.
   - pyautogui.sleep(1) pauses the script for 1 second between each movement.

⚠️ Safety Tip:
- Always start with a small number of repetitions when testing automation.
- Keep FAILSAFE enabled to avoid losing control of your mouse.
"""

import pyautogui

# ==================================================
# 1) FAILSAFE (Safety Mechanism)
# ==================================================
# Enabled by default.
# Move the mouse to any corner of the screen to stop the script immediately.
# Uncomment the line below ONLY if you intentionally want to disable it.
# pyautogui.FAILSAFE = False


# ==================================================
# 2) PAUSE (Global Delay)
# ==================================================
# Adds a 1-second pause after every PyAutoGUI action
pyautogui.PAUSE = 1


# ==================================================
# 3) mouseInfo() (Cursor Position & Color Info)
# ==================================================
# Opens a live window showing mouse coordinates and RGB values.
# Useful for identifying exact positions before automation.
# pyautogui.mouseInfo()


# ==================================================
# 4) Automated Mouse Movement Example
# ==================================================
# Move the mouse (x + 100, y + 100) five times
# Pause for 1 second between each movement
for i in range(5):
    pyautogui.move(100, 100)   # Relative movement
    pyautogui.sleep(1)         # Explicit pause between loops

# ✅ If FAILSAFE is enabled:
# - Move the mouse cursor to a screen corner to stop execution instantly.
