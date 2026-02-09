# ==================================================
# 🌐 Web Scraping & Automation – Full Workflow Overview
# ==================================================

# --------------------------------------------------
# 1️⃣ HTML / CSS / JavaScript Basics
# --------------------------------------------------
# HTML : The structure (skeleton) of a web page
# CSS  : Styling and visual presentation
# JS   : Makes the page dynamic (events, loading, interaction)

# --------------------------------------------------
# 2️⃣ XPath Basics
# --------------------------------------------------
# XPath : A way to locate HTML elements by their path or attributes
# - Can use id, class, text, and structure
# Example: //*[@id="search_btn"]
# - Absolute paths are fragile and break easily when the page structure changes (not recommended)

# --------------------------------------------------
# 3️⃣ Chrome Developer Tools
# --------------------------------------------------
# Using DevTools (Inspect) allows you to:
# - Examine HTML structure
# - Check id / class / XPath
# → Essential for Selenium and BeautifulSoup

# --------------------------------------------------
# 4️⃣ Requests vs Selenium
# --------------------------------------------------
# Requests
# - Fast
# - Suitable for static web pages
# - Cannot execute JavaScript

# Selenium
# - Slower
# - Can handle dynamic web pages
# - Controls a real browser (click, input, scroll)

# BeautifulSoup
# - Parses HTML fetched by Requests or Selenium
# - Used only for data extraction

# --------------------------------------------------
# 5️⃣ User-Agent
# --------------------------------------------------
# User-Agent : Identifies your browser/device to the server
# - Often required to avoid bot blocking
# - Especially important when using headless browsers

# --------------------------------------------------
# 6️⃣ Selenium Core Actions
# --------------------------------------------------
# Locating elements
# find_element(By.ID, ...)
# find_element(By.CLASS_NAME, ...)
# find_element(By.LINK_TEXT, ...)
# find_element(By.XPATH, ...)

# Common actions
# click()      : Click element
# send_keys() : Input text
# clear()     : Clear input field

# --------------------------------------------------
# 7️⃣ Selenium Waiting (Critical)
# --------------------------------------------------
# Dynamic pages require explicit waits
# Use WebDriverWait + Expected Conditions

# Example:
# WebDriverWait(browser, 10).until(
#     EC.presence_of_element_located((By.XPATH, "//*[@id='content']"))
# )

# --------------------------------------------------
# 8️⃣ Selenium Scrolling (Infinite Scroll Handling)
# --------------------------------------------------
import time

# Scroll interval (seconds)
interval = 2

# Store current document height
prev_height = browser.execute_script("return document.body.scrollHeight")

while True:
    # Scroll to bottom
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(interval)

    # Check new height
    curr_height = browser.execute_script("return document.body.scrollHeight")

    # If height does not change, loading is complete
    if curr_height == prev_height:
        break

    prev_height = curr_height

# --------------------------------------------------
# 9️⃣ BeautifulSoup Core Methods
# --------------------------------------------------
# find()                   : First matching element
# find_all()               : All matching elements (list)
# find_next_sibling(s)     : Next sibling element(s)
# find_previous_sibling(s): Previous sibling element(s)

# Access attributes
# tag["href"]

# Get text only
# tag.get_text()

# --------------------------------------------------
# 🔟 Image Download
# --------------------------------------------------
# Binary files must be saved using "wb" mode
with open("filename.jpg", "wb") as f:
    f.write(res.content)

# --------------------------------------------------
# 1️⃣1️⃣ CSV Export
# --------------------------------------------------
import csv

# utf-8-sig prevents Excel Korean character issues
f = open("data.csv", "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)

# writer.writerow([...])
# writer.writerows([...])

f.close()

# --------------------------------------------------
# 1️⃣2️⃣ Headless Chrome
# --------------------------------------------------
# Runs browser in the background
# - Useful for servers and automation tasks
# - User-Agent may be required
# - Supported since Chrome 59+

# --------------------------------------------------
# ⚠️ 1️⃣3️⃣ Crawling & Scraping Ethics (Very Important)
# --------------------------------------------------
# Excessive scraping may cause:
# → Server overload
# → IP or account bans

# Unauthorized data usage may result in:
# → Copyright violations
# → Legal consequences

# --------------------------------------------------
# 1️⃣4️⃣ robots.txt
# --------------------------------------------------
# robots.txt
# - Indicates allowed / disallowed crawling paths
# - Not legally binding
# - Represents site owner's crawling preferences → should be respected

# Allow    : Allowed
# Disallow : Disallowed
