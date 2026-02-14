import pyautogui

"""
📌 PyAutoGUI Exception Handling & Environment Troubleshooting (Day 2)

Today's Learning Focus:
1) Understanding how locateOnScreen() behaves differently depending on version
2) Handling ImageNotFoundException safely
3) Fixing environment issues (Pillow, pyscreeze, OpenCV)
4) Writing more Pythonic try/except automation logic

------------------------------------------------------------
🔥 1️⃣ Why does locateOnScreen() behave differently?

In older versions:
→ If the image was not found, it returned None.

In recent PyAutoGUI + pyscreeze combinations:
→ If the image is not found,
   ImageNotFoundException may be raised instead.

That means:

file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")

If the image is not on the screen:

❌ It does NOT simply return None.
❌ It does NOT go to the else block.
⛔ It immediately raises an exception and stops the program.

Therefore, a simple if/else structure is not always safe.
We must use try/except to handle this properly.

------------------------------------------------------------
🛡️ 2️⃣ Safe Exception Handling (Recommended Pattern)

Goal:
- If found → click
- If not found → print "Not Found"
- Do NOT crash the program
"""

try:
    location = pyautogui.locateOnScreen(
        "file_menu_notepad.png",
        confidence=0.8  # Allows similarity matching (requires OpenCV)
    )
    pyautogui.click(location)

except pyautogui.ImageNotFoundException:
    print("Not Found")


"""
------------------------------------------------------------
💡 3️⃣ Why is 'if file_menu_notepad' unnecessary?

Old-style approach:

if file_menu_notepad:
    ...
else:
    print("Not Found")

However, in newer environments:
- It may raise ImageNotFoundException instead of returning None.

So:
If an exception occurs,
Python immediately jumps to the except block.

This makes try/except cleaner and more Pythonic
for automation scripts.

------------------------------------------------------------
🧰 4️⃣ Environment Troubleshooting Summary

If image recognition does not work:

① Pillow not installed
→ pip install pillow

② pyscreeze issue
→ pip install pyscreeze

③ Using confidence parameter
→ pip install opencv-python

Important:
If using a virtual environment (venv),
you must install these inside that environment.

------------------------------------------------------------
🎯 Key Takeaways Today

✔ locateOnScreen() does not always return None.
✔ It can raise ImageNotFoundException.
✔ Proper exception handling makes automation stable.
✔ Some problems are environment issues, not code logic errors.

Today's focus was not just functionality,
but understanding library behavior deeply.
"""
