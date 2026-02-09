"""
Web Scraping Basics: Parser, HTML Attributes, and HTTP Errors

This file summarizes fundamental web scraping concepts using
requests and BeautifulSoup.

The goal of this example is not to scrape a specific website,
but to understand how HTML documents are fetched, parsed,
and explored in Python.

Key concepts covered:
- What a parser is
- How HTML attributes are represented in BeautifulSoup
- The role of href in web scraping
- Why HTTP errors (404) occur
"""

# ==================================================
# 1. Parser
# ==================================================
# A parser is a tool that analyzes a document and converts it
# into a structured format that a program can understand.
#
# In web scraping:
# - HTML is originally just a long string of text
# - A parser converts it into a tree-like structure
# - This allows us to search for tags, attributes, and text
#
# BeautifulSoup uses parsers such as "lxml" to process HTML.


# ==================================================
# 2. HTML Attributes and attrs Dictionary
# ==================================================
# HTML tags can contain attributes such as:
# - href
# - class
# - id
#
# Example HTML:
# <a href="/webtoon/list" class="link">Webtoon</a>
#
# In BeautifulSoup:
# - All attributes of a tag are stored in a dictionary called attrs
# - This allows easy access to attribute values
#
# Example:
# tag.attrs
# tag["href"]


# ==================================================
# 3. href Attribute
# ==================================================
# The href attribute specifies the destination URL of a link.
#
# It is one of the most important attributes in web scraping
# because it allows navigation from one page to another.
#
# In practice:
# - a tag → title or clickable text
# - href → link to another page


# ==================================================
# 4. HTTP 404 Error
# ==================================================
# A 404 error means that the requested URL does not exist on the server.
#
# This often happens in web scraping because:
# - Website structures change over time
# - Old URLs become invalid
#
# Using raise_for_status() helps detect these problems immediately
# instead of failing silently.


# ==================================================
# 5. Key Takeaways
# ==================================================
# - Web scraping is about understanding HTML structure
# - Code breaking due to site changes is normal
# - Errors are signals, not failures
# - The most important skill is adapting to structure changes
