"""
📌 What I learned (Web Scraping Context)

This file focuses on how HTTP requests and responses work
in real web scraping scenarios.

Key points:
- requests.get() returns a response object
- The response object contains status code and HTML text
- raise_for_status() helps detect request failures early
- Headers (User-Agent) are required to mimic a real browser
"""

import requests

# Target URL (example site for learning purposes)
url = "https://example.com"

# User-Agent header to mimic a real browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

# Send HTTP GET request
res = requests.get(url, headers=headers)

# Raise an error immediately if the request failed
res.raise_for_status()

# Inspect the response
print("Status Code:", res.status_code)
print("HTML Preview:")
print(res.text[:200])
