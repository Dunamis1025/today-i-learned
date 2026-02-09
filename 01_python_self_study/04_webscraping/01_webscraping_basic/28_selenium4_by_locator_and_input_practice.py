"""
📌 Selenium 4 Learning Notes - Locator (By) and Input Practice with Naver Login Page

This file is NOT intended to perform an automatic login.
Instead, it focuses on understanding:

- Selenium 4 standard locator syntax (By.ID, By.NAME, etc.)
- How Selenium finds elements in the DOM
- send_keys() and clear() behavior on input elements
- Why the browser closes immediately after a script ends
- How to intentionally keep the browser open for inspection

⚠️ Important Notice
- Naver actively blocks automated login attempts.
- The goal is NOT login success,
  but confirming that element interaction works correctly.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# ==================================================
# 1️⃣ Launch browser
# ==================================================
# In Selenium 4, chromedriver does NOT need to be specified manually.
# Selenium automatically matches the correct driver version
# based on the installed Chrome browser.
browser = webdriver.Chrome()

# ==================================================
# 2️⃣ Navigate directly to Naver login page
# ==================================================
# We skip the main page and go straight to the login page.
browser.get("https://nid.naver.com/nidlogin.login")

# ==================================================
# 3️⃣ Wait for page to fully load
# ==================================================
# Selenium runs much faster than humans.
# Without waiting, Selenium may try to locate elements
# before they exist in the DOM, causing errors.
time.sleep(3)

# ==================================================
# 4️⃣ Locate the ID input field (Selenium 4 standard)
# ==================================================
"""
Why this import matters:
from selenium.webdriver.common.by import By

- selenium.webdriver.common.by  → the module (by.py)
- By                            → the class inside that module

By acts like a "locator toolbox" that defines HOW elements are found.
Selenium 4 unified all locator methods into this single interface.

Example:
By.ID
By.NAME
By.CLASS_NAME
By.CSS_SELECTOR
By.XPATH
"""

# On Naver's login page, the ID input field uses name="id"
id_input = browser.find_element(By.NAME, "id")

# ==================================================
# 5️⃣ First input attempt
# ==================================================
id_input.send_keys("first_test_id")
time.sleep(2)

# ==================================================
# 6️⃣ Clear the input field
# ==================================================
# clear() removes all text from the input box.
id_input.clear()
time.sleep(1)

# ==================================================
# 7️⃣ Second input attempt
# ==================================================
id_input.send_keys("second_test_id")
time.sleep(2)

print("✅ Input → clear → re-input sequence completed successfully")

# ==================================================
# 8️⃣ Keep browser open intentionally
# ==================================================
# input() pauses the script until the user presses Enter.
# Without this line, the script would finish
# and the browser would close immediately.
input("Press Enter to close the browser...")

# ==================================================
# 9️⃣ Close browser cleanly
# ==================================================
browser.quit()
