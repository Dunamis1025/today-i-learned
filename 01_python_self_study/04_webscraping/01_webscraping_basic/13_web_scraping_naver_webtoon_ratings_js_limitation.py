import requests
from bs4 import BeautifulSoup

# ============================================================
# Web Scraping Practice Summary
# Topic: Extracting episode ratings from Naver Webtoon (Gauss Electronics)
#
# Learning Objectives:
# 1. Understand how to extract repeated elements from HTML
# 2. Calculate total and average values from scraped data
# 3. Learn why requests + BeautifulSoup fails on JS-rendered pages
#
# Important Note:
# - This code demonstrates the scraping logic correctly.
# - However, it may NOT return results anymore because
#   Naver Webtoon now loads rating data via JavaScript.
# ============================================================


# ------------------------------------------------------------
# 1. Send HTTP request to the webtoon page
# ------------------------------------------------------------
url = "https://comic.naver.com/webtoon/list?titleId=799793"

headers = {
    "User-Agent": "Mozilla/5.0"
}

# requests only fetches the raw HTML returned by the server.
# It does NOT execute JavaScript.
response = requests.get(url, headers=headers)
response.raise_for_status()


# ------------------------------------------------------------
# 2. Create BeautifulSoup object for HTML parsing
# ------------------------------------------------------------
soup = BeautifulSoup(response.text, "lxml")


# ------------------------------------------------------------
# 3. Locate rating elements (historical structure)
# ------------------------------------------------------------
# Previous HTML structure:
#
# <div class="rating_type">
#     <strong>9.98</strong>
# </div>
#
# This structure no longer appears in the raw HTML.

ratings = soup.find_all("div", attrs={"class": "rating_type"})


# ------------------------------------------------------------
# 4. Calculate total rating score
# ------------------------------------------------------------
total_score = 0

for rating in ratings:
    score = rating.find("strong").get_text()
    print(score)
    total_score += float(score)


# ------------------------------------------------------------
# 5. Output results
# ------------------------------------------------------------
print("Total score:", total_score)

if len(ratings) > 0:
    print("Average score:", total_score / len(ratings))
else:
    print("⚠️ No rating data found in the HTML.")
    print("⚠️ This page is rendered using JavaScript.")
