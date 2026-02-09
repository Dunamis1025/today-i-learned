"""
📌 Selenium Headless Mode & User-Agent Configuration (Learning Note)

This script demonstrates:
- How to run Selenium without opening a visible browser (headless mode)
- Why setting a window size is important in headless execution
- How to customize the User-Agent string
- How infinite scroll still works in headless mode
- How to verify the applied User-Agent
- How to capture screenshots even when the browser is invisible

This is a learning note, not a production crawler.
"""

# ==================================================
# 1️⃣ Import WebDriver and configure Chrome options
# ==================================================

from selenium import webdriver

# ChromeOptions allows us to customize browser behavior
options = webdriver.ChromeOptions()

# Run Chrome in headless mode
# → The browser runs in the background without a visible window
options.headless = True

# Set a fixed window size
# This is critical in headless mode because:
# - There is no real screen
# - Layout, scrolling, and lazy loading depend on viewport size
options.add_argument("window-size=1920x1080")

# Set a custom User-Agent
# This makes the browser identify itself like a real desktop Chrome browser
# Useful for:
# - Avoiding simple bot detection
# - Ensuring consistent page rendering
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/144.0.0.0 Safari/537.36"
)

# Create the browser instance with the configured options
browser = webdriver.Chrome(options=options)

# maximize_window() has no visual effect in headless mode,
# but calling it keeps behavior consistent with normal mode
browser.maximize_window()

# ==================================================
# 2️⃣ Open a dynamic page (Google Movies)
# ==================================================

url = "https://play.google.com/store/movies?hl=ko"
browser.get(url)

# This page loads content dynamically as the user scrolls

# ==================================================
# 3️⃣ Infinite scroll logic (headless-compatible)
# ==================================================

import time

interval = 2  # seconds to wait between scrolls

# Store the initial document height
prev_height = browser.execute_script("return document.body.scrollHeight")

while True:
    # Scroll to the bottom of the page
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    # Wait for JavaScript to load new content
    time.sleep(interval)

    # Measure the updated document height
    curr_height = browser.execute_script("return document.body.scrollHeight")

    # If the height does not change, no more content is loading
    if curr_height == prev_height:
        break

    prev_height = curr_height

print("Scrolling finished")

# ==================================================
# 4️⃣ Capture a screenshot in headless mode
# ==================================================

# Even though the browser is invisible,
# Selenium can still capture screenshots of the rendered page
browser.get_screenshot_as_file("google_movie.png")

# ==================================================
# 5️⃣ Parse the fully loaded HTML with BeautifulSoup
# ==================================================

from bs4 import BeautifulSoup

# Selenium handles dynamic loading
# BeautifulSoup handles HTML parsing
soup = BeautifulSoup(browser.page_source, "lxml")

# Each movie card is wrapped in a div with class "Vpfmgd"
movies = soup.find_all("div", attrs={"class": "Vpfmgd"})
print(f"Total movie cards found: {len(movies)}")

# ==================================================
# 6️⃣ Extract discounted movie information
# ==================================================

for movie in movies:
    # Movie title
    title = movie.find("div", attrs={"class": "WsMG1c nnK0zc"}).get_text()

    # Original price exists only if the movie is discounted
    original_price = movie.find("span", attrs={"class": "SUZt4c djCuy"})
    if not original_price:
        # Skip non-discounted movies
        continue
    original_price = original_price.get_text()

    # Discounted price
    price = movie.find("span", attrs={"class": "VfPpfd ZdBevf i5DZme"}).get_text()

    # Relative link to movie detail page
    link = movie.find("a", attrs={"class": "JC71ub"})["href"]

    print(f"Title: {title}")
    print(f"Original Price: {original_price}")
    print(f"Discounted Price: {price}")
    print("Link:", "https://play.google.com" + link)
    print("-" * 100)

# ==================================================
# 7️⃣ Verify User-Agent detection (learning purpose)
# ==================================================

# This section demonstrates how to confirm
# that the custom User-Agent is actually applied

browser.get("https://www.whatismybrowser.com/detect/what-is-my-user-agent/")

# NOTE:
# In Selenium 4, the old find_element_by_* methods are deprecated.
# They may still work in some environments, but modern code should use By.
# This example keeps the original form for learning comparison purposes.

detected_value = browser.find_element_by_id("detected_value")
print("Detected User-Agent:")
print(detected_value.text)

# ==================================================
# 8️⃣ Close the browser
# ==================================================

browser.quit()

"""
🧠 Key Takeaways

- Headless mode allows Selenium to run without opening a visible browser
- Window size must be explicitly defined in headless environments
- User-Agent customization helps mimic real browser behavior
- Infinite scroll logic works the same in headless and normal modes
- Screenshots can still be captured without a visible UI
- Selenium controls loading; BeautifulSoup handles parsing
"""
