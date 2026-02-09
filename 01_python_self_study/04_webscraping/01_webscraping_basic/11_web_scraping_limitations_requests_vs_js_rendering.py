"""
[Web Scraping Learning Note]

This file documents an attempted web scraping example using
requests and BeautifulSoup, and explains why it no longer works
for modern, JavaScript-rendered websites.

IMPORTANT:
This example uses Naver Webtoon purely for educational purposes.
The goal is NOT to scrape data successfully,
but to understand the limitations of requests + BeautifulSoup
and how modern websites deliver content.

At the time of writing, this script does NOT return webtoon titles,
and that behavior is expected.
"""

import requests
from bs4 import BeautifulSoup

# ==================================================
# 1. Target URL
# ==================================================
# Naver Webtoon episode list page (PC version)
url = "https://comic.naver.com/webtoon/list?titleId=799793"

# ==================================================
# 2. Send HTTP request
# ==================================================
# Add User-Agent header to mimic a real browser request
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}

res = requests.get(url, headers=headers)

# Raise an exception if the HTTP status code is not 200
res.raise_for_status()

# ==================================================
# 3. Parse HTML response
# ==================================================
# Parse the returned HTML using BeautifulSoup
soup = BeautifulSoup(res.text, "lxml")

# ==================================================
# 4. Attempt to find webtoon title elements
# ==================================================
# In the past, webtoon titles existed inside:
# <td class="title"> elements
cartoons = soup.find_all("td", attrs={"class": "title"})

# ==================================================
# 5. Debugging output
# ==================================================
print("HTTP status code:", res.status_code)
print("HTML length:", len(res.text))
print("Number of title elements found:", len(cartoons))

# Print the first part of the HTML to inspect the actual response
print("\n[HTML preview]")
print(res.text[:500])

# ==================================================
# 6. Defensive coding
# ==================================================
# Always check list length before accessing by index
if cartoons:
    title = cartoons[0].a.get_text(strip=True)
    print("\nFirst webtoon title:", title)
else:
    print(
        "\nNo webtoon titles were found.\n"
        "Possible reasons:\n"
        "1) The page content is rendered by JavaScript\n"
        "2) The request was partially blocked\n"
        "3) The page structure has changed\n"
    )

"""
==================================================
Key Takeaways from This Experiment

1. A SyntaxError may indicate an execution issue,
   not necessarily a code logic problem.

2. An IndexError (list index out of range) usually means
   that no data was found, not that the selector is wrong.

3. A successful HTTP response (200 OK) does NOT guarantee
   that the desired HTML content was returned.

4. Many modern websites (including Naver)
   use JavaScript to render content dynamically.

5. requests + BeautifulSoup only work reliably
   when the server returns fully rendered HTML.

6. For JavaScript-rendered pages,
   browser automation tools such as Selenium are required.

Purpose of this file:
To clearly document why a common scraping approach fails
and to record the reasoning process for future reference.
==================================================
"""
