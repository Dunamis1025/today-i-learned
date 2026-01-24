"""
📌 Selenium REPL Practice - Controlling a Browser in Real Time

⚠️ This file is NOT meant to be executed as a script.

Today's practice was done in the following way:

1️⃣ I did NOT run a Python file directly
2️⃣ I started Python from the terminal and entered the REPL (>>> prompt)
3️⃣ Selenium commands were typed one line at a time
4️⃣ Each command caused an immediate, visible change
   in the actual Naver browser window

In other words,

This was NOT:
"Python script → browser runs automatically"

This WAS:
"Already opened browser ← Python controls it in real time"

The goal of this practice was to experience that feeling.
"""

# ==================================================
# 1️⃣ Commands entered step by step in Python REPL
# ==================================================

# (REPL)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


# --------------------------------------------------
# 2️⃣ Create browser options
# --------------------------------------------------
options = Options()
options.add_argument("--start-maximized")


# --------------------------------------------------
# 3️⃣ Launch Chrome browser
# 👉 A real Chrome window opens at this moment
# --------------------------------------------------
browser = webdriver.Chrome(options=options)


# --------------------------------------------------
# 4️⃣ Navigate to Naver main page
# --------------------------------------------------
browser.get("https://www.naver.com")


# --------------------------------------------------
# 5️⃣ Click the login button
# 👉 Selenium finds the HTML element and performs a real click
# --------------------------------------------------
login_button = browser.find_element(By.CLASS_NAME, "link_login")
login_button.click()


# --------------------------------------------------
# 6️⃣ Browser navigation control
# 👉 Same as clicking back / forward buttons manually
# --------------------------------------------------
browser.back()
browser.forward()
browser.refresh()


# --------------------------------------------------
# 7️⃣ Find the search input box
# --------------------------------------------------
search_box = browser.find_element(By.ID, "query")


# --------------------------------------------------
# 8️⃣ Type a search keyword
# 👉 Behaves like real keyboard input
# --------------------------------------------------
search_box.send_keys("Nado Coding")


# --------------------------------------------------
# 9️⃣ Press ENTER key
# 👉 Exactly the same as pressing Enter on the keyboard
# --------------------------------------------------
search_box.send_keys(Keys.ENTER)


"""
📌 Key Takeaways

- Python is not only for "scraping" web pages
- Python can directly control a real web browser
- In REPL, one command equals one immediate action
- Clicking, typing, pressing Enter, navigating pages
  can all be done through code

Through this practice,
I experienced for the first time that
code can replace real human actions.
"""
