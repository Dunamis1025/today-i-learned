import requests
from bs4 import BeautifulSoup

"""
Web Scraping Basics: Sibling Navigation in HTML

This file focuses on understanding how sibling relationships
work in HTML documents and how BeautifulSoup can be used
to navigate between them.

Rather than scraping a specific website, this example
explains the concept of sibling traversal and when it is useful
in real-world web scraping scenarios.
"""

# ==================================================
# 1. Fetching a Web Page
# ==================================================
# requests is used to fetch the raw HTML of a web page.
# raise_for_status() helps detect HTTP errors such as 404 early.

url = "https://example.com"
res = requests.get(url)
res.raise_for_status()

# ==================================================
# 2. Parsing HTML
# ==================================================
# BeautifulSoup converts the HTML text into a navigable tree structure (DOM).
# The parser (lxml) helps interpret HTML efficiently.

soup = BeautifulSoup(res.text, "lxml")

# ==================================================
# 3. What Are Siblings in HTML?
# ==================================================
# Siblings are elements that share the same parent element.
#
# Example HTML structure:
#
# <ul>
#   <li>Item 1</li>
#   <li>Item 2</li>
#   <li>Item 3</li>
# </ul>
#
# In this structure, all <li> elements are siblings.

# ==================================================
# 4. Accessing Siblings
# ==================================================
# next_sibling / previous_sibling:
# - Move to adjacent nodes in the document
# - May include whitespace or newline nodes
#
# Because of this, these attributes often require multiple calls
# to reach the actual HTML element.

# Example (conceptual):
# first_item.next_sibling.next_sibling

# ==================================================
# 5. Safer Sibling Navigation
# ==================================================
# BeautifulSoup provides helper methods that skip non-element nodes.
#
# find_next_sibling(tag_name)
# find_previous_sibling(tag_name)
#
# These methods are more reliable and commonly used in practice.

# Example use case:
# - Navigating ranking lists
# - Iterating through article lists
# - Processing repeated product or post entries

# ==================================================
# 6. Accessing All Siblings
# ==================================================
# find_next_siblings(tag_name)
# - Returns a list of all sibling elements after the current one
#
# This is useful when you want to process multiple items
# in sequence without manually traversing one by one.

# ==================================================
# 7. Parent Relationship
# ==================================================
# parent:
# - Accesses the parent element of the current tag
#
# Understanding parent-child-sibling relationships is essential
# for navigating complex HTML structures.

# ==================================================
# 8. Text-Based Element Search
# ==================================================
# Elements can also be found using their visible text.
#
# Example (conceptual):
# soup.find("a", text="Sample Article Title")
#
# This approach depends heavily on page content and may break
# if the text changes.

# ==================================================
# Key Takeaways
# ==================================================
# - Siblings are elements that share the same parent
# - Sibling navigation is useful for lists and rankings
# - find_next_sibling() is safer than next_sibling
# - HTML structures often change, but relationships remain
# - Understanding structure matters more than exact selectors
