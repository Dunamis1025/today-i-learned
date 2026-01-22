import requests
import re
from bs4 import BeautifulSoup

# --------------------------------------------------
# 1️⃣ Set User-Agent header to mimic a real browser
#    (basic practice to reduce bot blocking)
# --------------------------------------------------
headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/143.0.0.0 Safari/537.36"
}

# --------------------------------------------------
# 2️⃣ Loop through search result pages (page 1 to 5)
# --------------------------------------------------
for page in range(1, 6):

    # Search URL with dynamic page number
    url = (
        "https://www.coupang.com/np/search?"
        "q=%EB%85%B8%ED%8A%B8%EB%B6%81"
        "&traceId=mkk9mpq8"
        "&channel=user"
        f"&page={page}"
    )

    # --------------------------------------------------
    # 3️⃣ Send HTTP GET request and receive HTML response
    # --------------------------------------------------
    response = requests.get(url, headers=headers)

    # Raise an exception if HTTP error occurs (403, 404, etc.)
    response.raise_for_status()

    # --------------------------------------------------
    # 4️⃣ Parse HTML into DOM structure using BeautifulSoup
    # --------------------------------------------------
    soup = BeautifulSoup(response.text, "lxml")

    # --------------------------------------------------
    # 5️⃣ Extract all product list items
    #    (li tags with class starting with 'search-product')
    # --------------------------------------------------
    items = soup.find_all(
        "li",
        attrs={"class": re.compile("^search-product")}
    )

    # --------------------------------------------------
    # 6️⃣ Iterate through each product and apply filters
    # --------------------------------------------------
    for item in items:

        # ❌ Skip sponsored (advertisement) products
        ad_badge = item.find("span", attrs={"class": "ad-badge-text"})
        if ad_badge:
            continue

        # Product name
        name = item.find("div", attrs={"class": "name"}).get_text()

        # ❌ Exclude Apple products
        if "Apple" in name:
            continue

        # Product price
        price = item.find(
            "strong",
            attrs={"class": "price-value"}
        ).get_text()

        # Rating score
        rating = item.find("em", attrs={"class": "rating"})
        if rating:
            rating = rating.get_text()
        else:
            # Skip products without rating
            continue

        # Number of reviews
        review_count = item.find(
            "span",
            attrs={"class": "rating-total-count"}
        )
        if review_count:
            # Format example: "(123)" → remove parentheses
            review_count = review_count.get_text()[1:-1]
        else:
            continue

        # Product detail page link
        link = item.find(
            "a",
            attrs={"class": "search-product-link"}
        )["href"]

        # --------------------------------------------------
        # 7️⃣ Final filter:
        #    - Rating >= 4.5
        #    - Review count >= 100
        # --------------------------------------------------
        if float(rating) >= 4.5 and int(review_count) >= 100:
            print(f"Product Name : {name}")
            print(f"Price        : {price}")
            print(f"Rating       : {rating} ({review_count} reviews)")
            print("Link         : https://www.coupang.com" + link)
            print("-" * 100)
