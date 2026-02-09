"""
📌 Quiz: Real Estate Listing Scraping
(Legacy Approach + Failure Analysis)

This script documents a real estate scraping exercise
originally taught around 2020 using requests + BeautifulSoup.

==================================================
❗ IMPORTANT (Current Reality)
==================================================
As of 2024–2026, this approach no longer works on:

- Korean real estate platforms (Daum, Naver, Zigbang, Dabang)
- Australian real estate platforms:
  - realestate.com.au
  - domain.com.au
  - allhomes.com.au

I personally tested the same approach on all of the above,
and every attempt failed for the same fundamental reasons.

👉 Common outcome:
- The HTTP response does NOT contain actual listing data
- Real data is loaded only after JavaScript execution
- Listings are fetched via protected internal APIs
- Some sites immediately return blocked or skeleton HTML

Therefore, this file is NOT intended to succeed.
It exists to document *why* the old approach fails today.
"""

import requests
from bs4 import BeautifulSoup

# ==================================================
# 1️⃣ Page request (legacy approach)
# ==================================================
# Around 2020, many websites returned fully rendered HTML
# directly from the server.
# In that environment, requests + BeautifulSoup was sufficient.

url = "https://www.zigbang.com/home/apt/danjis/38487"
response = requests.get(url)

# Raise an exception if HTTP status is not OK
response.raise_for_status()

# ==================================================
# 2️⃣ Parse HTML
# ==================================================
# Parse the returned HTML document.
# Historically, listing data existed directly inside the HTML.

soup = BeautifulSoup(response.text, "lxml")

# ==================================================
# 3️⃣ (Optional) Inspect HTML structure
# ==================================================
# Developers often saved the HTML output to inspect
# the DOM structure when selectors failed.

# with open("legacy_real_estate.html", "w", encoding="utf-8") as f:
#     f.write(soup.prettify())

# ==================================================
# 4️⃣ Locate listing table (legacy assumption)
# ==================================================
# ❗ This is the main failure point today
#
# Past assumption:
# - Listing data exists in <table class="tbl">
#
# Current reality:
# - The table does not exist in static HTML
# - DOM is populated only after JavaScript execution
# - requests cannot access dynamically rendered content

table = soup.find("table", attrs={"class": "tbl"})

if not table:
    print("❌ Listing table not found.")
    print("👉 This site is very likely JavaScript-rendered.")
    print("👉 Selenium / Playwright or API analysis is required.")
    exit()

tbody = table.find("tbody")
rows = tbody.find_all("tr")

# ==================================================
# 5️⃣ Output listing data (legacy format)
# ==================================================
# Output format follows the original lecture requirement.

for index, row in enumerate(rows):
    cols = row.find_all("td")

    print(f"======= Listing {index + 1} =======")
    print("Transaction :", cols[0].get_text(strip=True))
    print("Area :", cols[1].get_text(strip=True), "(Supply / Net)")
    print("Price :", cols[2].get_text(strip=True), "(10,000 KRW)")
    print("Building :", cols[3].get_text(strip=True))
    print("Floor :", cols[4].get_text(strip=True))

"""
==================================================
📌 Final Summary
==================================================

Why this approach fails across both Korea and Australia:

1️⃣ No real data in static HTML
2️⃣ JavaScript-driven rendering
3️⃣ Internal API calls with authentication tokens
4️⃣ Bot-detection and traffic control policies
5️⃣ High commercial value of real estate data

Conclusion:
- requests + BeautifulSoup scraping is now
  a historical learning reference only

Modern alternatives:
- Selenium / Playwright for browser automation
- Network tab–based API analysis
- Official APIs or licensed data sources

This file is intentionally preserved as:
👉 a record of failure
👉 a documentation of architectural change
👉 a mindset transition in modern web scraping
"""
