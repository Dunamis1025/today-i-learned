"""
📌 What I learned (Web Scraping Context)

This file focuses on parsing HTML using BeautifulSoup
and understanding the DOM structure used in web scraping.

Key points:
- HTML text is converted into a DOM-like structure
- DOM allows structured searching using tags and attributes
- find() vs find_all() usage
- re.compile() is useful for matching dynamic class names
- Filtering logic is essential in real-world scraping
"""

from bs4 import BeautifulSoup
import re

# Sample HTML for learning purposes
html = """
<ul>
    <li class="search-product">Laptop A</li>
    <li class="search-product ad">Laptop B</li>
    <li class="search-product">Laptop C</li>
</ul>
"""

# Parse HTML into a DOM structure
soup = BeautifulSoup(html, "lxml")

# Find all list items whose class starts with "search-product"
items = soup.find_all(
    "li",
    attrs={"class": re.compile("^search-product")}
)

# Apply filtering logic
for item in items:
    # Exclude advertisement items
    if "ad" in item.get("class", []):
        continue

    print(item.get_text())
