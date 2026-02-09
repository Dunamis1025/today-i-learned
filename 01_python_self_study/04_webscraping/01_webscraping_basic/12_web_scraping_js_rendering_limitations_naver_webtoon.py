import requests
from bs4 import BeautifulSoup

# ============================================================
# Web Scraping Study Notes
# Topic: Limitations of requests + BeautifulSoup
#        on JavaScript-rendered pages
#
# Example site: Naver Webtoon (Gauss Electronics)
# ============================================================

# ------------------------------------------------------------
# 1. Goal of this experiment
# ------------------------------------------------------------
# - Automatically collect webtoon titles and links
#   from a Naver Webtoon series page.
#
# - Since the episode list is clearly visible
#   in the browser, it is easy to assume that
#   the data also exists directly in the HTML.
# ------------------------------------------------------------

url = "https://comic.naver.com/webtoon/list?titleId=799793"

# ------------------------------------------------------------
# 2. Sending a request with requests
# ------------------------------------------------------------
# requests sends an HTTP request to the server
# and retrieves only the raw HTML response.
#
# ⚠️ It does NOT execute JavaScript like a browser.
# ------------------------------------------------------------
res = requests.get(url)
res.raise_for_status()  # Raise an error for HTTP issues

# ------------------------------------------------------------
# 3. Parsing the HTML with BeautifulSoup
# ------------------------------------------------------------
soup = BeautifulSoup(res.text, "lxml")

# ------------------------------------------------------------
# 4. Selector used during the original lesson
# ------------------------------------------------------------
# In the past, Naver Webtoon pages had a structure
# where each episode title was inside:
#
# <td class="title">
#   <a href="...">Episode Title</a>
# </td>
#
# Therefore, the selector below used to work correctly.
# ------------------------------------------------------------
cartoons = soup.find_all("td", attrs={"class": "title"})

print("Number of webtoon elements found:", len(cartoons))

# ------------------------------------------------------------
# 5. Result analysis
# ------------------------------------------------------------
# Currently, len(cartoons) == 0
#
# ❌ This does NOT mean the code is wrong
# ❌ This does NOT mean BeautifulSoup is misused
#
# ✔️ Reason:
#   - Naver Webtoon uses JavaScript to render content dynamically
#   - The server response HTML does NOT contain episode data
#   - The browser executes JavaScript and renders the list afterward
# ------------------------------------------------------------

if cartoons:
    # This block would work for static HTML pages
    for cartoon in cartoons:
        title = cartoon.a.get_text(strip=True)
        link = "https://comic.naver.com" + cartoon.a["href"]
        print(title, link)
else:
    print("No webtoon titles were found.")
    print("This page is rendered dynamically using JavaScript.")
    print("requests + BeautifulSoup alone cannot extract this data.")

# ------------------------------------------------------------
# 6. Key takeaways from this experiment
# ------------------------------------------------------------
# 1) requests retrieves only raw HTML (no JavaScript execution)
# 2) What you see in the browser ≠ what the server sends
# 3) An empty find_all result can lead to IndexError
# 4) Before scraping, always check:
#    - View Page Source
#    - Compare with Elements tab
#    - Whether the page is static or JS-rendered
#
# 5) Possible solutions (conceptual overview):
#    - Use Selenium
#    - Check for an official API
#    - Practice with static HTML pages
# ------------------------------------------------------------
