"""
📌 PyAutoGUI - Image Recognition and Automated Clicking

This file documents how to use PyAutoGUI's locateOnScreen()
function to detect specific images on the screen and automate
mouse movement and clicking.

------------------------------------------------------------
📌 What I Learned Today
------------------------------------------------------------

1️⃣ How to find the position of an image on the screen
2️⃣ How to click a detected image
3️⃣ How to move the mouse to a detected image
4️⃣ That locateOnScreen() returns None if no image is found
5️⃣ How to handle multiple identical images using a loop
6️⃣ How to select only the first matched image
7️⃣ How Windows display scaling affects image recognition

------------------------------------------------------------
⚠️ IMPORTANT: Display Scaling Issue
------------------------------------------------------------

PyAutoGUI matches images at the pixel level.

If Windows display scaling changes (100% → 125% → 150%),
the pixel structure changes slightly.

As a result:
- Previously captured images may not match
- locateOnScreen() may return None

✅ Best Practice:

• Always capture screenshots at the same scaling you use for execution
• If scaling changes, re-capture all reference images
• Keep your working environment consistent

------------------------------------------------------------
"""

import pyautogui


# ------------------------------------------------------------
# 1️⃣ Find a specific image on the screen
# ------------------------------------------------------------

file_menu = pyautogui.locateOnScreen("file_menu.png")

print(file_menu)
# If found → Box(left=..., top=..., width=..., height=...)
# If not found → None


# ------------------------------------------------------------
# 2️⃣ Click the detected image
# ------------------------------------------------------------

if file_menu is not None:
    pyautogui.click(file_menu)


# ------------------------------------------------------------
# 3️⃣ Move mouse to detected image
# ------------------------------------------------------------

trash_icon = pyautogui.locateOnScreen("trash_icon.png")

if trash_icon is not None:
    pyautogui.moveTo(trash_icon)


# ------------------------------------------------------------
# 4️⃣ Handling None result
# ------------------------------------------------------------

screen = pyautogui.locateOnScreen("screenshot.png")
print(screen)

# Always check for None before clicking.


# ------------------------------------------------------------
# 5️⃣ Click all matching images (multiple checkboxes example)
# ------------------------------------------------------------

for checkbox in pyautogui.locateAllOnScreen("checkbox.png"):
    print(checkbox)
    pyautogui.click(checkbox, duration=0.25)


# ------------------------------------------------------------
# 6️⃣ Click only the first matching image
# ------------------------------------------------------------

first_checkbox = pyautogui.locateOnScreen("checkbox.png")

if first_checkbox is not None:
    pyautogui.click(first_checkbox)


"""
📌 Summary

✔ locateOnScreen() → finds one match
✔ locateAllOnScreen() → finds all matches
✔ Returns None if no image is found
✔ Always check for None before clicking
✔ Display scaling affects recognition
✔ Automation must run in a consistent environment
"""