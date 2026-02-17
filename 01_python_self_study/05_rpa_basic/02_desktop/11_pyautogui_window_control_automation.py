import pyautogui

"""
📌 Today's Topic: Window Automation using PyAutoGUI

This script focuses on controlling application windows,
NOT mouse-coordinate automation.

Core concepts learned today:

1️⃣ Get the currently active window
2️⃣ Retrieve all open windows
3️⃣ Find a window by title
4️⃣ Bring a window to the front (activate)
5️⃣ Maximize / Minimize / Restore a window
6️⃣ Close a window

👉 Window control is a fundamental step before image-based automation.
"""


# -----------------------------------------------------------
# 1️⃣ Get Information About the Currently Active Window
# -----------------------------------------------------------

# fw = pyautogui.getActiveWindow()
# Returns the currently active window object.

# print(fw.title)
# Prints the window title.

# print(fw.size)
# Prints the window size (width, height).

# print(fw.left, fw.top, fw.right, fw.bottom)
# Prints the window coordinates.
# left/top = starting position
# right/bottom = ending position

# pyautogui.click(fw.left + 25, fw.top + 20)
# Example: Click a specific relative position inside the window.


# -----------------------------------------------------------
# 2️⃣ List All Open Windows (for debugging)
# -----------------------------------------------------------

# for w in pyautogui.getAllWindows():
#     print(w)
# Useful when checking exact window titles.


# -----------------------------------------------------------
# 3️⃣ Get a Window by Title
# -----------------------------------------------------------

"""
getWindowsWithTitle("test")

Returns a list of windows containing "test" in the title.
Since it returns a list, we select the first match with [0].
"""

w = pyautogui.getWindowsWithTitle("test")[0]
print(w)


# -----------------------------------------------------------
# 4️⃣ Activate the Window if Not Active
# -----------------------------------------------------------

if not w.isActive:
    w.activate()
    # Brings the window to the front.


# -----------------------------------------------------------
# 5️⃣ Maximize the Window if Not Maximized
# -----------------------------------------------------------

if not w.isMaximized:
    w.maximize()
    # Expands the window to full screen.


pyautogui.sleep(1)
# Pause for visual confirmation.


# -----------------------------------------------------------
# 6️⃣ Restore Window to Original State
# -----------------------------------------------------------

w.restore()
# Restores from maximized/minimized state.


# -----------------------------------------------------------
# 7️⃣ Close the Window
# -----------------------------------------------------------

w.close()
# Closes the application window.


"""
📌 Summary

🔹 getActiveWindow() → Current active window
🔹 getAllWindows() → List all open windows
🔹 getWindowsWithTitle() → Find window by title

🔹 isActive / activate()
🔹 isMaximized / maximize()
🔹 minimize()
🔹 restore()
🔹 close()

This is the foundation of GUI automation before moving to image recognition.
"""
