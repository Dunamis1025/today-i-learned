import requests
from bs4 import BeautifulSoup

# --------------------------------------------------
# 1️⃣ Send request to Daum search page
#    - Search query: "2019 movie ranking"
#    - User-Agent is required to mimic a real browser
# --------------------------------------------------
url = "https://search.daum.net/search?w=tot&q=2019%EB%85%84%20%EC%98%81%ED%99%94%20%EC%88%9C%EC%9C%84"
headers = {
    "User-Agent": "Mozilla/5.0"
}

res = requests.get(url, headers=headers)
res.raise_for_status()  # Raise an error if the request fails

# --------------------------------------------------
# 2️⃣ Parse HTML
#    - Convert raw HTML text into a navigable DOM structure
# --------------------------------------------------
soup = BeautifulSoup(res.text, "lxml")

# --------------------------------------------------
# 3️⃣ Attempt to find movie poster images
#    - Look for img tags with class="thumb_img"
# --------------------------------------------------
images = soup.find_all("img", attrs={"class": "thumb_img"})

# --------------------------------------------------
# 4️⃣ Try to extract image URLs
# --------------------------------------------------
for image in images:
    image_url = image.get("src")

    # If the URL starts with "//", convert it to an absolute URL
    if image_url and image_url.startswith("//"):
        image_url = "https:" + image_url

    print(image_url)

# --------------------------------------------------
# 5️⃣ Debugging: print part of the received HTML
#    - Used to verify whether movie poster elements
#      actually exist in the server-rendered HTML
# --------------------------------------------------
print(soup.prettify()[:1000])

"""
📌 Learning Summary

- requests and BeautifulSoup are working correctly
- However, Daum movie ranking pages render movie posters
  dynamically using JavaScript
- requests cannot execute JavaScript
- As a result, movie poster elements are not included
  in the HTML returned by the server
- Therefore, BeautifulSoup cannot find the expected img tags

👉 Conclusion:
This example demonstrates a real-world limitation of
using requests + BeautifulSoup on JavaScript-rendered pages
"""
