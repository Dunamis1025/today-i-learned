import requests
from bs4 import BeautifulSoup

# ==================================================
# Purpose of this file
# --------------------------------------------------
# This example is designed to review the core concepts
# of web scraping using requests and BeautifulSoup.
#
# The focus is NOT on scraping a specific real service,
# but on understanding:
# - How HTML is fetched from a server
# - How BeautifulSoup parses HTML into a DOM tree
# - How to extract repeated elements safely
# ==================================================


# --------------------------------------------------
# 1. Practice URL (static HTML page)
# --------------------------------------------------
# This site provides static HTML content without
# JavaScript-based rendering, making it ideal for
# learning and practice with BeautifulSoup.
url = "https://quotes.toscrape.com/"


# --------------------------------------------------
# 2. Send an HTTP request
# --------------------------------------------------
# requests.get() asks the server to return the HTML
# content of the given URL.
res = requests.get(url)

# If the request fails (e.g. 404 or 500),
# an exception will be raised immediately.
res.raise_for_status()


# --------------------------------------------------
# 3. Parse the HTML document
# --------------------------------------------------
# res.text contains the raw HTML as a string.
# The "lxml" parser converts this string into
# a structured DOM tree that we can navigate.
soup = BeautifulSoup(res.text, "lxml")


# --------------------------------------------------
# 4. Find repeated elements
# --------------------------------------------------
# On this page, each quote is stored inside:
# <span class="text"> ... </span>
#
# find_all() returns a list of all matching elements.
quotes = soup.find_all("span", attrs={"class": "text"})


# --------------------------------------------------
# 5. Extract and print text content
# --------------------------------------------------
# Since quotes is a list, we iterate through it.
# get_text() removes the HTML tags and returns
# only the readable text inside the element.
for quote in quotes:
    print(quote.get_text())
