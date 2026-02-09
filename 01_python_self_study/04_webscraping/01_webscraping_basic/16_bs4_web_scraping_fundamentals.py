"""
📌 What I Learned: Web Scraping Product Data with BeautifulSoup

This script demonstrates the core workflow of web scraping in Python:

1. Sending HTTP requests with custom headers
2. Parsing HTML documents using BeautifulSoup
3. Extracting structured data from repeated elements
4. Handling missing data safely to avoid runtime errors

Note:
The scraping logic in this file was originally practiced using a real-world
e-commerce website. However, many commercial sites actively block bots.

For reliable practice and testing, the same logic can be applied to
scraping-friendly websites such as:
- https://books.toscrape.com
- https://quotes.toscrape.com

The goal of this script is to learn scraping fundamentals,
not to bypass website protections.
"""

# ==================================================
# 1️⃣ Required Libraries
# ==================================================
import requests                  # Send HTTP requests
import re                        # Regular expressions for flexible matching
from bs4 import BeautifulSoup    # Parse HTML content


# ==================================================
# 2️⃣ Target URL & Headers
# ==================================================
# Example: Product search page (used for learning purposes)
url = "https://www.coupang.com/np/search?q=laptop&page=1"

# User-Agent header to simulate a real browser request
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}

# Send HTTP request
response = requests.get(url, headers=headers)
response.raise_for_status()  # Raise an error if the request is blocked


# ==================================================
# 3️⃣ Parse HTML
# ==================================================
soup = BeautifulSoup(response.text, "lxml")


# ==================================================
# 4️⃣ Locate Repeated Product Elements
# ==================================================
# Each product is contained in an <li> element
# whose class name starts with "search-product"
items = soup.find_all(
    "li",
    attrs={"class": re.compile("^search-product")}
)


# ==================================================
# 5️⃣ Extract Product Information Safely
# ==================================================
for item in items:
    # Product name
    name_tag = item.find("div", attrs={"class": "name"})
    name = name_tag.get_text() if name_tag else "Name not available"

    # Product price
    price_tag = item.find("strong", attrs={"class": "price-value"})
    price = price_tag.get_text() if price_tag else "Price not available"

    # Star rating
    rating_tag = item.find("em", attrs={"class": "rating"})
    rating = rating_tag.get_text() if rating_tag else "No rating"

    # Number of reviews
    review_count_tag = item.find(
        "span", attrs={"class": "rating-total-count"}
    )
    review_count = (
        review_count_tag.get_text()
        if review_count_tag else "No reviews"
    )

    # Output extracted data
    print(name, price, rating, review_count)

## 📌 Web Scraping Practice with BeautifulSoup

This project demonstrates the fundamental structure of web scraping in Python.

### Key Concepts Learned

- Sending HTTP requests using `requests`
- Using custom headers (User-Agent) to mimic browser behavior
- Parsing HTML documents with `BeautifulSoup`
- Extracting repeated elements using `find()` and `find_all()`
- Using regular expressions for flexible class matching
- Handling missing data safely to prevent runtime errors

### Important Note

Commercial websites often block automated requests.
The purpose of this project is **to understand scraping logic**, not to bypass protections.

The same techniques shown here can be reliably practiced on scraping-friendly sites such as:
- https://books.toscrape.com
- https://quotes.toscrape.com
