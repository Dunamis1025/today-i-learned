"""
📌 Google Movies Discounted Titles Scraping (Learning Note)

This script is NOT intended for production automation.

Its purpose is to understand:
- How Selenium controls dynamic web pages
- How infinite scroll pages work
- Why JavaScript execution is required in Selenium
- Clear role separation between Selenium and BeautifulSoup
- The mindset shift from Selenium 3 to Selenium 4

⚠️ Notes
- Google Movies content varies by country
- Some titles may not appear correctly outside Korea
- The goal is understanding the mechanism, not the result
"""

# ==================================================
# 1️⃣ Launch browser (Selenium 4 style)
# ==================================================
from selenium import webdriver

# Selenium 4 automatically manages the correct driver
browser = webdriver.Chrome()
browser.maximize_window()

# ==================================================
# 2️⃣ Open Google Movies page
# ==================================================
url = "https://play.google.com/store/movies?hl=ko"
browser.get(url)

# ==================================================
# 3️⃣ Load all content using infinite scroll
# ==================================================
import time

interval = 2  # seconds to wait after each scroll

# --------------------------------------------------
# IMPORTANT:
# We execute JavaScript inside the browser to get
# the total scrollable height of the page.
#
# document.body.scrollHeight returns:
# → the full height of the page including hidden content
#
# This value increases when new items are loaded.
# --------------------------------------------------
prev_height = browser.execute_script(
    "return document.body.scrollHeight"
)

while True:
    # Scroll to the bottom of the page
    browser.execute_script(
        "window.scrollTo(0, document.body.scrollHeight)"
    )

    # Wait for new content to load
    time.sleep(interval)

    # Get the new height after scrolling
    curr_height = browser.execute_script(
        "return document.body.scrollHeight"
    )

    # If height does not change, no more content is loading
    if curr_height == prev_height:
        break

    prev_height = curr_height

print("Scrolling completed")

# ==================================================
# 4️⃣ Parse HTML with BeautifulSoup
# ==================================================
from bs4 import BeautifulSoup

# Selenium loads the page, BeautifulSoup analyzes it
soup = BeautifulSoup(browser.page_source, "lxml")

# Select all movie cards
movies = soup.find_all("div", attrs={"class": "Vpfmgd"})
print("Total movies found:", len(movies))

# ==================================================
# 5️⃣ Extract discounted movies only
# ==================================================
for movie in movies:
    # Movie title
    title = movie.find(
        "div", attrs={"class": "WsMG1c nnK0zc"}
    ).get_text()

    # Original price exists ONLY when the movie is discounted
    original_price = movie.find(
        "span", attrs={"class": "SUZt4c djCuy"}
    )

    if not original_price:
        # Skip non-discounted movies
        continue

    original_price = original_price.get_text()

    # Discounted price
    discounted_price = movie.find(
        "span", attrs={"class": "VfPpfd ZdBevf i5DZme"}
    )
    if discounted_price:
        discounted_price = discounted_price.get_text()

    # Movie detail link
    link = movie.find("a", attrs={"class": "JC71ub"})["href"]
    full_link = "https://play.google.com" + link

    print(f"""
🎬 Title: {title}
💰 Original Price: {original_price}
🔥 Discounted Price: {discounted_price}
🔗 Link: {full_link}
""")
