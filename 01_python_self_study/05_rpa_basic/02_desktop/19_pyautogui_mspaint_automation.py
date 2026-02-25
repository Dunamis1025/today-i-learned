"""
Filename example:
19_pyautogui_mspaint_automation.py

📌 Today's Learning Topic
GUI Automation Practice using PyAutoGUI – Automatic MSPaint Launch and Exit

📌 Practice Objectives
1. Open the Run dialog using Win + R
2. Launch MSPaint and maximize the window
3. Click the Text tool and enter text
4. Wait for 5 seconds
5. Close MSPaint without saving

📌 Key Learning Points
- pyautogui.hotkey()
- pyautogui.write()
- pyautogui.locateOnScreen()
- Using pyperclip for Korean text input
- Handling automatic key input when closing programs
"""

import sys
import pyautogui
import pyperclip


# -----------------------------------------------------------
# Basic Settings
# -----------------------------------------------------------

pyautogui.PAUSE = 1
# Adds a 1-second delay between every PyAutoGUI action
# This prevents recognition failures caused by actions being too fast

pyautogui.useImageNotFoundException(False)
# Returns None instead of raising an error when image detection fails


# -----------------------------------------------------------
# 1️⃣ Launch MSPaint
# -----------------------------------------------------------

# Open Run dialog (Win + R)
pyautogui.hotkey("win", "r")

# Type mspaint in the Run dialog
pyautogui.write("mspaint")

# Press Enter to execute
pyautogui.press("enter")

# Wait for MSPaint to load (considering loading time)
pyautogui.sleep(2)


# -----------------------------------------------------------
# 2️⃣ Maximize MSPaint Window
# -----------------------------------------------------------

# Find window with title "Untitled - Paint"
# (Assuming only one MSPaint window is open)
window = pyautogui.getWindowsWithTitle("Untitled - Paint")[0]

# Maximize if not already maximized
if not window.isMaximized:
    window.maximize()


# -----------------------------------------------------------
# 3️⃣ Click Text Tool
# -----------------------------------------------------------

# Locate the Text button on the screen
# btn_text.png must be captured beforehand
btn_text = pyautogui.locateOnScreen("btn_text.png", confidence=0.7)

if btn_text:
    pyautogui.click(btn_text, duration=0.5)
else:
    print("Failed to locate the Text button.")
    sys.exit()


# -----------------------------------------------------------
# 4️⃣ Click White Area and Enter Text
# -----------------------------------------------------------

# Click somewhere in the white canvas area
# Coordinates may need adjustment depending on resolution
pyautogui.click(300, 300, duration=0.5)


# 🔹 Korean Text Input Function
# pyautogui.write() does not handle Korean characters reliably
# Therefore, use clipboard copy + Ctrl+V paste method

def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")


my_write("참 잘했어요")


# -----------------------------------------------------------
# 5️⃣ Wait for 5 Seconds
# -----------------------------------------------------------

pyautogui.sleep(5)


# -----------------------------------------------------------
# 6️⃣ Close MSPaint (Do Not Save)
# -----------------------------------------------------------

# Close the window
window.close()

# Wait briefly for the save confirmation dialog
pyautogui.sleep(0.5)

# Select "Don't Save"
# On English OS, press 'n'
pyautogui.press("n")

"""
📌 Execution Flow Summary

Win + R
→ Launch mspaint
→ Maximize window
→ Click Text tool
→ Click white canvas
→ Enter "참 잘했어요"
→ Wait 5 seconds
→ Close window
→ Select "Don't Save"

📌 Important Notes

1. btn_text.png must be captured using the current screen resolution.
2. Image detection may fail if display scaling (125%, 150%) differs.
3. Save confirmation shortcut key may vary depending on OS language.
4. locateOnScreen can be slow; confidence value may require tuning.

📌 Purpose of This Practice

- Understanding the basic flow of GUI automation
- Automating keyboard and mouse control
- Using image-based UI element detection
- Handling Korean text input properly
- Managing program termination scenarios

This script follows the same structural pattern used in real-world RPA workflows.
"""
