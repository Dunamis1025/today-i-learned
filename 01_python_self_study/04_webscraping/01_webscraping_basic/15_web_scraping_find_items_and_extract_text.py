"""
📌 What I Learned: Finding Item Lists and Extracting Text with BeautifulSoup

In this lesson, I focused on two core web scraping skills:

1. Finding a list of repeated elements (items) from HTML
2. Extracting specific text from a nested tag inside each item

This is a fundamental pattern used in almost every web scraping project.
"""

import re
from bs4 import BeautifulSoup


# ------------------------------------------------------------
# 1. Sample HTML structure (conceptual example)
# ------------------------------------------------------------
# <li class="search-product">
#     <div class="name">Product Title</div>
# </li>
#
# Multiple <li> elements represent a list of products.
# ------------------------------------------------------------


# ------------------------------------------------------------
# 2. Finding multiple items using find_all()
# ------------------------------------------------------------
# soup.find_all() returns a LIST of matching elements.
#
# We search for:
# - tag: <li>
# - attribute: class
# - pattern: class name starts with "search-product"
# ------------------------------------------------------------

items = soup.find_all(
    "li",
    attrs={"class": re.compile("^search-product")}
)


# ------------------------------------------------------------
# 3. Why re.compile() is used here
# ------------------------------------------------------------
# Class names in real HTML are often not exact.
#
# Examples:
# - search-product
# - search-product-wrap
# - search-product-item
#
# Using a regex pattern allows flexible matching.
# ------------------------------------------------------------


# ------------------------------------------------------------
# 4. Extracting text from a nested tag
# ------------------------------------------------------------
# items[0]        -> the first product item
# .find("div")    -> find a child <div> tag
# attrs={"class": "name"} -> target the product name
# .get_text()     -> extract readable text
# ------------------------------------------------------------

product_name = (
    items[0]
    .find("div", attrs={"class": "name"})
    .get_text()
)

print(product_name)


# ------------------------------------------------------------
# 5. Key takeaways
# ------------------------------------------------------------
# - find_all() is used to collect repeated elements as a list
# - Regex helps when class names are not fixed
# - find() searches inside a single element
# - get_text() extracts human-readable content
#
# This pattern applies to:
# - product lists
# - article lists
# - comment sections
# - search results
# ------------------------------------------------------------
