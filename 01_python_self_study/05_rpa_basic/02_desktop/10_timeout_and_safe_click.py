import pyautogui
import time
import sys


"""
📌 What I learned today

1️⃣ Understanding the danger of infinite waiting (while target is None)
2️⃣ Introducing timeout logic to improve program stability
3️⃣ Structuring code into reusable functions

This script practices how to build a safer and more reliable
image-based automation structure.
"""


# -----------------------------------------------------------
# 1️⃣ Function to find a target image with timeout protection
# -----------------------------------------------------------

def find_target(img_file, timeout=30):
    """
    Searches for an image on the screen within a given timeout.

    Parameters:
        img_file : Name of the image file to locate
        timeout  : Maximum waiting time in seconds

    How it works:
        - Repeatedly searches for the image
        - Stops searching once the timeout is exceeded
        - Prevents infinite loop situations

    Returns:
        - The location (Box object) if found
        - None if timeout is reached
    """

    start_time = time.time()  # Record start time
    target = None             # Initially, target is not found

    while target is None:  # Keep searching until found
        target = pyautogui.locateOnScreen(img_file)

        current_time = time.time()
        elapsed_time = current_time - start_time  # Calculate elapsed time

        # Stop searching if timeout is exceeded
        if elapsed_time > timeout:
            break

    return target


# -----------------------------------------------------------
# 2️⃣ Safe click function using the timeout-protected finder
# -----------------------------------------------------------

def my_click(img_file, timeout=30):
    """
    Safe click function.

    - Calls find_target() internally
    - Clicks if the image is found
    - Exits the program if not found within timeout

    Purpose:
        Build a practical and stable automation structure
    """

    target = find_target(img_file, timeout)

    if target:
        # Click if the image is found
        pyautogui.click(target)
    else:
        # If not found within timeout
        print(f"[Timeout {timeout}s] Target not found: {img_file}")
        print("Program will terminate safely.")
        sys.exit()


# -----------------------------------------------------------
# 3️⃣ Execution Section
# -----------------------------------------------------------

"""
Instead of directly calling pyautogui.click(),
use the safe wrapper function:

    my_click("image.png", timeout_seconds)

Benefits:
    - Reusable
    - Cleaner code
    - Easier maintenance
    - More stable automation
"""

my_click("file_menu_notepad.png", 10)
