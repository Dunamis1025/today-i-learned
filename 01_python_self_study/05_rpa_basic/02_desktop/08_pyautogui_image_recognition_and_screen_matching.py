"""
📌 PyAutoGUI - Image Recognition & Screen Matching Practice

This file summarizes the basic usage of locateOnScreen()
for screen-based automation.

Key Concepts:
- Detecting UI elements using screenshot images
- Moving the mouse to matched locations
- Optimizing performance using grayscale, region, and confidence
"""

import pyautogui

# =========================================================
# 1) Basic image detection
# =========================================================
# locateOnScreen() searches the entire screen for a matching image.
# If found, it returns a Box object (left, top, width, height).
# If not found, it returns None.

# file_menu = pyautogui.locateOnScreen("file_menu.png")
# print(file_menu)
# pyautogui.click(file_menu)


# =========================================================
# 2) Move mouse to detected image
# =========================================================

# trash_icon = pyautogui.locateOnScreen("trash_icon.png")
# pyautogui.moveTo(trash_icon)


# =========================================================
# 3) Detect multiple matching images
# =========================================================

# for box in pyautogui.locateAllOnScreen("checkbox.png"):
#     print(box)
#     pyautogui.click(box, duration=0.25)


# =========================================================
# 🚀 Performance Optimization Techniques
# =========================================================

# ---------------------------------------------------------
# (1) Use grayscale for faster matching
# ---------------------------------------------------------
# Converts screen and image to grayscale before matching.
# This may improve speed but slightly reduce accuracy.

# trash_icon = pyautogui.locateOnScreen("trash_icon.png", grayscale=True)
# pyautogui.moveTo(trash_icon)


# ---------------------------------------------------------
# (2) Limit search region
# ---------------------------------------------------------
# Instead of searching the entire screen,
# restrict the search area to improve performance.
#
# region = (left_x, top_y, width, height)

# trash_icon = pyautogui.locateOnScreen(
#     "trash_icon.png",
#     region=(1399, 692, 1601 - 1399, 830 - 692)
# )
# pyautogui.moveTo(trash_icon)


# ---------------------------------------------------------
# (3) Adjust matching confidence
# ---------------------------------------------------------
# confidence defines how similar the image must be.
# 0.9 = 90% similarity required.
#
# Higher confidence → more strict matching
# Lower confidence → more flexible but may cause false positives
#
# Note:
# confidence parameter requires OpenCV (opencv-python).

run_btn = pyautogui.locateOnScreen("run_btn.png", confidence=0.9)

if run_btn is not None:
    pyautogui.moveTo(run_btn)
else:
    print("run_btn.png not found on the screen. Check resolution or scaling.")


"""
Additional Notes:
- Image matching may fail if:
  - Windows display scaling is not 100%
  - Screen resolution changes
  - Dark mode / theme changes
  - Icons or UI layout changes

- If detection fails, try taking a new screenshot
  and replace the reference image file.
"""
