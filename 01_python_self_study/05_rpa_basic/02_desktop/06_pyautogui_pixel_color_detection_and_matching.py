import pyautogui

"""
📌 PyAutoGUI – Screenshot, Pixel Color Detection, and Color Matching

This script demonstrates how to:

1️⃣ Take a screenshot of the screen
2️⃣ Use mouseInfo() to identify the mouse cursor position (x, y)
   and the RGB color of the pixel under the cursor
3️⃣ Retrieve the RGB color of a specific screen coordinate using pixel()
4️⃣ Compare a pixel's color with a target RGB value using pixelMatchesColor()

These techniques are commonly used in:
- UI automation
- Macro scripting
- Game bots
- GUI testing and screen-based condition checks
"""

# ==================================================
# 1️⃣ Taking a screenshot
# ==================================================

# Capture the entire screen
# img = pyautogui.screenshot()

# Save the screenshot as an image file
# img.save("screenshot.png")

# (Uncomment when needed)


# ==================================================
# 2️⃣ Mouse information (position & color)
# ==================================================

# pyautogui.mouseInfo()
"""
mouseInfo() opens a small window showing:
- Current mouse cursor coordinates (x, y)
- RGB color values at that position
- HEX color code

Example output:
29,16  37,174,243  #25AEF3

These values can be reused in pixel() and pixelMatchesColor().
"""


# ==================================================
# 3️⃣ Getting the pixel color at a specific coordinate
# ==================================================

# Get the RGB color of the pixel at (x=29, y=16)
pixel = pyautogui.pixel(29, 16)

# pixel is returned as an (R, G, B) tuple
print(pixel)

"""
Example output:
(37, 174, 243)

This means:
R = 37
G = 174
B = 243
"""


# ==================================================
# 4️⃣ Comparing pixel colors (True / False)
# ==================================================

# pixelMatchesColor() returns:
# - True if the pixel color matches the given RGB value
# - False if it does not match

# Example: checking with a slightly different color (expected False)
print(pyautogui.pixelMatchesColor(29, 16, (37, 174, 244)))

"""
Why pixelMatchesColor() is useful:

- It allows conditional logic such as:
  "If this button turns blue, click it"
  "If this screen appears, proceed to the next step"

- Enables reliable screen-based automation using True / False logic
"""


# ==================================================
# 📌 Key Summary
# ==================================================
"""
- screenshot(): captures the screen
- mouseInfo(): shows cursor position and pixel color
- pixel(x, y): returns the RGB color at a screen coordinate
- pixelMatchesColor(x, y, (R, G, B)):
    → True if colors match
    → False otherwise
"""
