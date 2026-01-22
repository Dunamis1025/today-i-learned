import requests
from bs4 import BeautifulSoup

# ==================================================
# 📌 Purpose
# Practice web scraping by attempting to download
# the TOP 5 movie poster images for each year
# from 2015 to 2019 based on Daum search results.
#
# ⚠️ Note:
# Daum's page structure has changed since this
# example was originally taught, so the scraping
# no longer returns valid results.
#
# The goal of this script is to understand the
# overall scraping workflow, not to obtain
# working results.
# ==================================================

# --------------------------------------------------
# 1️⃣ Loop through years 2015 ~ 2019
# --------------------------------------------------
for year in range(2015, 2020):

    # --------------------------------------------------
    # 2️⃣ Build Daum search URL
    #    Example query: "2015년 영화순위"
    # --------------------------------------------------
    url = (
        "https://search.daum.net/search"
        "?w=tot"
        "&q={}년영화순위"
        "&DA=MOR"
        "&rtmaxcoll=MOR"
    ).format(year)

    # --------------------------------------------------
    # 3️⃣ Request HTML page
    # --------------------------------------------------
    res = requests.get(url)
    res.raise_for_status()  # Stop immediately if request fails

    # --------------------------------------------------
    # 4️⃣ Parse HTML into DOM structure
    # --------------------------------------------------
    soup = BeautifulSoup(res.text, "lxml")

    # --------------------------------------------------
    # 5️⃣ Find movie poster image tags
    # --------------------------------------------------
    images = soup.find_all("img", attrs={"class": "thumb_img"})

    # --------------------------------------------------
    # 6️⃣ Download only top 5 images per year
    # --------------------------------------------------
    for idx, image in enumerate(images):

        # Extract image URL
        image_url = image["src"]

        # --------------------------------------------------
        # 7️⃣ Handle protocol-relative URLs (//...)
        # --------------------------------------------------
        if image_url.startswith("//"):
            image_url = "https:" + image_url

        print(image_url)

        # --------------------------------------------------
        # 8️⃣ Download image file
        # --------------------------------------------------
        image_res = requests.get(image_url)
        image_res.raise_for_status()

        # --------------------------------------------------
        # 9️⃣ Save image locally
        #    Example: movie_2015_1.jpg
        # --------------------------------------------------
        file_name = "movie_{}_{}.jpg".format(year, idx + 1)

        with open(file_name, "wb") as f:
            f.write(image_res.content)

        # --------------------------------------------------
        # 🔟 Limit to top 5 images
        # --------------------------------------------------
        if idx >= 4:
            break
