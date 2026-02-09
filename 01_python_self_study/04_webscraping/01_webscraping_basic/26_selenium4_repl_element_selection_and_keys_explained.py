"""
📌 Selenium 4 REPL Practice (Element Selection + Keyboard Input Explained)

This file is NOT an auto-running script.

Instead, it is a learning record created by:
👉 entering commands one by one
👉 inside the Python REPL (>>> prompt)
👉 while directly observing browser behavior.

---------------------------------------
🎯 Purpose of This File
---------------------------------------
1️⃣ Understand why Selenium 4 imports are split into multiple modules
2️⃣ Understand how text input and the Enter key actually work
3️⃣ Understand why Selenium 3-style code causes errors in Selenium 4
4️⃣ Understand why CSS_SELECTOR is the most commonly used selector
5️⃣ Reach the point where you can trace the cause of errors instead of guessing

If you come back to this file later,
👉 you should be able to quickly restore the core Selenium workflow.
"""

# ==================================================
# 1️⃣ Core Selenium imports
# ==================================================

# webdriver
# 👉 Controls a real browser (Chrome, Edge, etc.) using Python
from selenium import webdriver

# By
# 👉 Specifies HOW an element should be located
#    (id, name, class, css selector, etc.)
# 👉 Required in Selenium 4
from selenium.webdriver.common.by import By

# Keys
# 👉 Represents special keyboard keys
# 👉 Examples: Enter, Tab, Shift, Ctrl
from selenium.webdriver.common.keys import Keys


# ==================================================
# 2️⃣ Launch the browser
# ==================================================

browser = webdriver.Chrome()

# Open Daum homepage
browser.get("https://www.daum.net")


# ==================================================
# 3️⃣ Locate the search input (Selenium 4 style)
# ==================================================

"""
❌ Old Selenium 3 style (deprecated)
-----------------------------------
elem = browser.find_element_by_name("q")

⚠️ Problems with this approach:
- Removed in Selenium 4
- Causes AttributeError or very long error messages
"""

"""
✅ Correct Selenium 4 approach
-----------------------------------
find_element(By.METHOD, "value")
"""

search = browser.find_element(By.NAME, "q")

"""
How to read this line:
- By.NAME → locate the element using the 'name' attribute
- "q"     → the actual HTML attribute value (name="q")

In plain English:
"Find the input element whose name attribute is 'q'"
"""


# ==================================================
# 4️⃣ Type text and press Enter
# ==================================================

"""
send_keys()
👉 Simulates real keyboard input
"""

# Type the search keyword
search.send_keys("나도코딩")

"""
At this point:
It is equivalent to a human typing "나도코딩" into the search box.
"""

# Press Enter
search.send_keys(Keys.ENTER)

"""
Keys.ENTER means:
- The same as pressing the Enter key on a keyboard
- This is NOT a string, but a special key
- That is why it comes from the Keys class
"""


# ==================================================
# 5️⃣ One element vs multiple elements (IMPORTANT)
# ==================================================

"""
find_element  → returns ONE WebElement
find_elements → returns a list of WebElements

If you confuse the two:
❌ You will get: WebElement is not iterable
"""

# Find all <a> tags on the page
links = browser.find_elements(By.CSS_SELECTOR, "a")

print(f"Number of <a> tags: {len(links)}")


# ==================================================
# 6️⃣ Why CSS_SELECTOR is preferred
# ==================================================

"""
CSS_SELECTOR:
✔ Most flexible option
✔ Can target by class, id, attributes, combinations
✔ More resilient to HTML structure changes

Examples:
"a"                  → all <a> tags
"a[href]"            → <a> tags with an href attribute
"a[href*='youtube']" → <a> tags whose href contains 'youtube'
"""

youtube_links = browser.find_elements(
    By.CSS_SELECTOR,
    "a[href*='youtube']"
)

print(f"Number of YouTube links: {len(youtube_links)}")


# ==================================================
# 7️⃣ Extract information from WebElements
# ==================================================

for link in youtube_links[:5]:
    # Visible text on the page
    print(link.text)

    # Actual destination URL
    print(link.get_attribute("href"))

    print("-" * 50)


# ==================================================
# 8️⃣ Key takeaways from this session
# ==================================================

"""
✔ Imports are separated by responsibility
✔ Selenium 4 requires the By-based syntax
✔ send_keys simulates real keyboard actions
✔ WebElement is NOT a list
✔ CSS_SELECTOR is the most powerful selector
✔ Long error messages usually come from:
   - Version differences
   - Confusing element vs list
   - Incorrect selectors
"""

"""
This file serves as:
👉 A personal Selenium recovery guide
👉 A reference point when things stop working

Once this makes sense,
moving on to CSV export or BeautifulSoup integration becomes natural.
"""
