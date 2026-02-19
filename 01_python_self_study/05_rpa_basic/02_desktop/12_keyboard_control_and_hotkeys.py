"""
📌 PyAutoGUI Keyboard Automation Summary (NadoCoding Review)

Core concepts covered in this file:

1️⃣ Activating a specific window
2️⃣ Basic keyboard typing with write()
3️⃣ Sending arrow keys and special keys
4️⃣ Understanding keyDown() and keyUp()
5️⃣ Using hotkey() for shortcut combinations
6️⃣ Handling Korean input safely with pyperclip
"""

import pyautogui
import pyperclip


# -----------------------------------------------------------
# 1️⃣ Get a specific window and activate it
# -----------------------------------------------------------

"""
getWindowsWithTitle("Title") returns a list of matching windows.

Since it returns a list, we must access the first element using [0].

⚠ Important:
- If the window does not exist, IndexError will occur.
- Make sure the target window is already open.
"""

w = pyautogui.getWindowsWithTitle("Untitled - Notepad")[0]
w.activate()  # Bring the window to the front


# -----------------------------------------------------------
# 2️⃣ Basic typing with write()
# -----------------------------------------------------------

"""
write() simulates human typing.

interval:
Adds a delay between each key press.
Useful for more natural-looking automation.
"""

# pyautogui.write("12345")
# pyautogui.write("NadoCoding", interval=0.25)
# pyautogui.write("KoreanText")  # Korean input may not work reliably


# -----------------------------------------------------------
# 3️⃣ Sending special keys using a list
# -----------------------------------------------------------

"""
When a list is passed to write(),
each key is executed in order.

Special keys:
"left"  → Left arrow key
"right" → Right arrow key
"enter" → Enter key
"""

pyautogui.write(
    ["t", "e", "s", "t", "left", "left", "right", "l", "a", "enter"],
    interval=0.25
)

"""
Execution flow:

1. Type "test"
2. Move cursor left twice
3. Move cursor right once
4. Type "la"
5. Press Enter
"""


# -----------------------------------------------------------
# 4️⃣ Typing special characters (Shift combination)
# -----------------------------------------------------------

"""
Example: typing "$" (Shift + 4)

keyDown():
Press and hold a key

keyUp():
Release the key
"""

# pyautogui.keyDown("shift")
# pyautogui.press("4")
# pyautogui.keyUp("shift")


# -----------------------------------------------------------
# 5️⃣ Keyboard combinations
# -----------------------------------------------------------

"""
Method 1: Manual press and release
"""

# pyautogui.keyDown("ctrl")
# pyautogui.press("a")
# pyautogui.keyUp("ctrl")

"""
Method 2: Using hotkey() (simpler)
"""

# pyautogui.hotkey("ctrl", "a")

"""
Execution order of hotkey("ctrl", "alt", "shift", "a"):

Press Ctrl →
Press Alt →
Press Shift →
Press A →
Release A →
Release Shift →
Release Alt →
Release Ctrl
"""

# ⚠ Be careful with typos:
# "alt" is correct, not "art"


# -----------------------------------------------------------
# 6️⃣ Handling Korean input safely (Clipboard method)
# -----------------------------------------------------------

"""
PyAutoGUI may fail when typing Korean characters directly.

Safer method:
1. Copy text to clipboard using pyperclip
2. Paste using Ctrl + V
"""

def safe_write(text):
    """
    Safely write multilingual text using clipboard paste.
    """
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")


# Example usage
safe_write("나도코딩")


# -----------------------------------------------------------
# ⚠ Automation termination shortcuts
# -----------------------------------------------------------

"""
Windows:
Ctrl + Alt + Delete

Mac:
Cmd + Shift + Option + Q

Always test automation scripts in a safe environment first.
"""


# -----------------------------------------------------------
# 🔥 Key Takeaways
# -----------------------------------------------------------

"""
✔ write() simulates typing
✔ keyDown() / keyUp() control modifier keys
✔ hotkey() simplifies shortcut execution
✔ Arrow keys and special keys are passed as strings
✔ Clipboard paste is the safest way for Korean input
✔ Always test automation carefully
"""
