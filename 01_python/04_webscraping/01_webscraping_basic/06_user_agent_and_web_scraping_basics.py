📘 Web Scraping Basics – Understanding User-Agent
1️⃣ One-line Summary

Setting a User-Agent allows Python to access web pages “like a real browser” and retrieve proper HTML content for web scraping.

2️⃣ Why This Topic Matters

When using Python’s requests module, it may seem easy to fetch a web page’s HTML.

However, in real-world scenarios:

Some websites block requests that look like bots

Requests without proper headers may return:

Broken or incomplete HTML

Empty content

A completely different page than what browsers receive

To solve this, we need to understand and use User-Agent headers.

3️⃣ What Is a User-Agent?

A User-Agent is an HTTP request header that tells a website:

“What browser and operating system is making this request.”

Example:

Mozilla/5.0 (Windows NT 10.0; Win64; x64)
AppleWebKit/537.36 (KHTML, like Gecko)
Chrome/143.0.0.0 Safari/537.36


This means:

Windows 10 (64-bit)

Chrome browser

A normal human browsing environment

In other words:
👉 “I am a real Chrome user, not a bot.”

4️⃣ Why User-Agent Is Important for Web Scraping

Websites often protect themselves against:

Automated scraping

Excessive traffic

Data abuse

If a request has no User-Agent (or a suspicious one), the server may:

Block the request

Return incomplete HTML

Serve a bot-detection page

By setting a proper User-Agent:

The server treats the request like a normal browser visit

The full HTML page is returned

Web scraping becomes possible

5️⃣ How to Find Your User-Agent

You can check your current browser’s User-Agent at:

https://www.whatismybrowser.com/

Copy the string shown in the blue box and use it in your Python code.
6️⃣ Example Code – Using User-Agent with requests
import requests

# Target website URL
url = "http://nadocoding.tistory.com"

# User-Agent copied from the browser
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/143.0.0.0 Safari/537.36"
    )
}

# Send HTTP request with User-Agent
res = requests.get(url, headers=headers)

# Raise an error if the request failed
res.raise_for_status()

# Save the HTML content to a file
with open("nadocoding.html", "w", encoding="utf8") as f:
    f.write(res.text)

7️⃣ Key Learning Points

Setting "User-Agent" helps avoid bot blocking

Proper HTML allows:

Searching content with Ctrl + F in VS Code

Matching what you see in Chrome DevTools

This step is preparation for real web scraping

Data extraction comes in the next stage

8️⃣ Why Learning This Is Useful

Without understanding User-Agent:

Scraping may suddenly fail

Debugging becomes confusing

You won’t know whether the issue is Python or the website

With this knowledge:

User-Agent becomes the first thing to check

Troubleshooting becomes much faster

You can scrape more websites reliably

9️⃣ Learning Roadmap Position

Current progress:

✅ HTTP requests with requests

✅ User-Agent handling

✅ Saving HTML locally

Next steps:

🔜 BeautifulSoup

🔜 HTML tag analysis

🔜 Extracting real data

🔖 Final Takeaway

User-Agent is a required setting for web scraping.
If HTML looks strange, check the User-Agent first.
