"""
📌 Google Movies – Infinite Scroll Handling with Selenium (Learning Note)

This script is NOT intended to be a production crawler.

Its purpose is to understand:
- Why Selenium is required for dynamic, JavaScript-rendered pages
- How infinite-scroll pages load content progressively
- Why scrolling alone is insufficient without waiting
- How Selenium and BeautifulSoup should be used together with clear roles

⚠️ Notes
- Google Movies content varies by region
- Some movies or discounts may not appear depending on location
- The focus is on understanding the mechanism, not perfect data accuracy
"""

# ==================================================
# 1️⃣ Launch browser with Selenium WebDriver
# ==================================================

from selenium import webdriver

# WebDriver acts as the controller that allows Python
# to operate a real browser (Chrome in this case)
browser = webdriver.Chrome()

# Maximizing the window helps stabilize scrolling behavior
# by exposing more content at once
browser.maximize_window()

# ==================================================
# 2️⃣ Open a dynamic web page
# ==================================================

url = "https://play.google.com/store/movies?hl=ko"
browser.get(url)

# Google Movies is a JavaScript-driven page.
# Content is loaded dynamically as the user scrolls.

# ==================================================
# 3️⃣ Scroll strategy overview
# ==================================================

# Example of scrolling to a fixed position (not suitable for infinite scroll)
# browser.execute_script("window.scrollTo(0, 1080)")

# Scroll to the very bottom of the document
# document.body.scrollHeight represents the total scrollable height
browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

# ==================================================
# 4️⃣ Core infinite scroll logic
# ==================================================

import time

interval = 2  # seconds to wait between scrolls

# Store the initial document height
prev_height = browser.execute_script("return document.body.scrollHeight")

while True:
    # Scroll to the bottom of the page
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    # Give JavaScript time to load and render new content
    time.sleep(interval)

    # Measure the new document height
    curr_height = browser.execute_script("return document.body.scrollHeight")

    # If the height has not changed, no more content is loading
    if curr_height == prev_height:
        break

    # Update height and continue scrolling
    prev_height = curr_height

print("Scrolling finished")

# ==================================================
# 5️⃣ Transfer control to BeautifulSoup for parsing
# ==================================================

from bs4 import BeautifulSoup

# Selenium handles browser control and dynamic loading
# BeautifulSoup handles HTML parsing and data extraction
soup = BeautifulSoup(browser.page_source, "lxml")

# ==================================================
# 6️⃣ Extract discounted movie information
# ==================================================

# Each movie card is wrapped in a div with class "Vpfmgd"
movies = soup.find_all("div", attrs={"class": "Vpfmgd"})
print(f"Total movie cards found: {len(movies)}")

for movie in movies:
    # Movie title
    title = movie.find("div", attrs={"class": "WsMG1c nnK0zc"}).get_text()

    # Original price exists only for discounted movies
    original_price = movie.find("span", attrs={"class": "SUZt4c djCuy"})
    if not original_price:
        # Skip movies without discounts
        continue
    original_price = original_price.get_text()

    # Discounted price
    price = movie.find("span", attrs={"class": "VfPpfd ZdBevf i5DZme"}).get_text()

    # Movie detail link (relative path)
    link = movie.find("a", attrs={"class": "JC71ub"})["href"]

    print(f"Title: {title}")
    print(f"Original Price: {original_price}")
    print(f"Discounted Price: {price}")
    print("Link:", "https://play.google.com" + link)
    print("-" * 100)

# ==================================================
# 7️⃣ Close the browser and release resources
# ==================================================

browser.quit()

"""
🧠 Key Takeaways
- Selenium controls browser behavior and dynamic loading
- BeautifulSoup focuses on HTML structure and parsing
- Infinite scroll requires both scrolling AND waiting
- Page readiness should be verified, not assumed
- Height comparison is a reliable termination condition
"""
