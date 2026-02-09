# ==================================================
# [2020 Tutorial] BeautifulSoup + Selenium Example
# ==================================================

# ❌ requests + BeautifulSoup approach (fails on JS-heavy pages)
# import requests
# from bs4 import BeautifulSoup
#
# url = "https://play.google.com/store/movies?hl=ko"
# headers = {
#     "User-Agent": "Mozilla/5.0",
#     "Accept-Language": "ko-KR,ko"
# }
#
# res = requests.get(url, headers=headers)
# res.raise_for_status()
# soup = BeautifulSoup(res.text, "lxml")
#
# movies = soup.find_all("div", attrs={"class": "ImZGtf mpg5gc"})
# print(len(movies))

# ==================================================
# ✔ Selenium approach (browser-driven)
# ==================================================

from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.maximize_window()

# Navigate to the page
url = "https://play.google.com/store/movies?hl=ko"
browser.get(url)

# --------------------------------------------------
# Core idea: scroll until no more content loads
# --------------------------------------------------

# Get initial document height
prev_height = browser.execute_script(
    "return document.body.scrollHeight"
)

interval = 2  # scroll every 2 seconds

while True:
    # Scroll to the bottom of the page
    browser.execute_script(
        "window.scrollTo(0, document.body.scrollHeight)"
    )

    # Wait for new content to load
    time.sleep(interval)

    # Measure new document height
    curr_height = browser.execute_script(
        "return document.body.scrollHeight"
    )

    # Stop when height no longer increases
    if curr_height == prev_height:
        break

    prev_height = curr_height

print("Scrolling completed")


What this tutorial was teaching (2020 perspective)

requests cannot load JavaScript-rendered content

Google Movies loads more items only when scrolling

Selenium is required to control a real browser

Scroll termination logic:

👉 Stop when the document height no longer changes

🟢 Refactored Version (Selenium 4 – 2026 Learning Mindset)

🎯 Purpose of this script
❌ Not data scraping
⭕ Understanding how Selenium interacts with modern, dynamic web pages

"""
📌 Selenium 4 Learning Notes - Infinite Scroll Handling

This script is NOT for automated data scraping.
It focuses on understanding:
- How JavaScript-driven pages load content dynamically
- How Selenium controls browser behavior
- How to detect the end of an infinite scroll

This file is intended as a study note for future reference.
"""

from selenium import webdriver
import time

# ==================================================
# 1️⃣ Launch browser (Selenium 4 standard)
# ==================================================
# ✔ No need to manually specify chromedriver path
# ✔ Selenium automatically matches the installed Chrome version
browser = webdriver.Chrome()
browser.maximize_window()

# ==================================================
# 2️⃣ Open Google Movies page
# ==================================================
url = "https://play.google.com/store/movies?hl=ko"
browser.get(url)

# ==================================================
# 3️⃣ Infinite scroll logic
# ==================================================

SCROLL_PAUSE_TIME = 2  # seconds

# Store initial page height
prev_height = browser.execute_script(
    "return document.body.scrollHeight"
)

while True:
    # ▶ Scroll to the bottom of the page
    browser.execute_script(
        "window.scrollTo(0, document.body.scrollHeight)"
    )

    # ▶ Wait for new content to load
    time.sleep(SCROLL_PAUSE_TIME)

    # ▶ Measure updated page height
    curr_height = browser.execute_script(
        "return document.body.scrollHeight"
    )

    # ▶ Exit loop when no new content is loaded
    if curr_height == prev_height:
        break

    prev_height = curr_height

print("✅ Scrolling completed (no more content to load)")
