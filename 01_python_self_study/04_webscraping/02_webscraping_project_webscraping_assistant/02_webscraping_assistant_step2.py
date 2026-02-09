"""
📌 Project: Personal Web Scraping Assistant (Step 2)

This file is NOT intended for production automation.
Its purpose is to:

👉 Understand the basic workflow of web scraping
👉 Practice using requests + BeautifulSoup together
👉 Learn how to read HTML structure and extract information
👉 Build scraping logic step by step using functions

⚠️ Important Notes
- This code follows the structure of early 2020s tutorials
- Due to frequent changes in Naver's HTML structure,
  some selectors may no longer work correctly
- The goal is NOT accurate results,
  but understanding the scraping mindset and flow
"""

# ==================================================
# 1️⃣ Required libraries
# ==================================================
import requests
from bs4 import BeautifulSoup


# ==================================================
# 2️⃣ Common helper function
#    URL → BeautifulSoup object
# ==================================================
def create_soup(url):
    """
    Sends an HTTP request to the given URL
    and returns a BeautifulSoup object
    for HTML parsing.
    """
    res = requests.get(url)
    res.raise_for_status()  # Raise an error if the request fails
    soup = BeautifulSoup(res.text, "lxml")
    return soup


# ==================================================
# 3️⃣ Scrape today's weather information
# ==================================================
def scrape_weather():
    print("[Today's Weather]")

    url = (
        "https://search.naver.com/search.naver"
        "?where=nexearch&query=Seoul+weather"
    )
    soup = create_soup(url)

    # ----------------------------------------------
    # Weather description (e.g. Cloudy, warmer than yesterday)
    # ----------------------------------------------
    cast = soup.find("p", attrs={"class": "cast_txt"}).get_text()

    # ----------------------------------------------
    # Current / min / max temperature
    # ----------------------------------------------
    curr_temp = (
        soup.find("p", attrs={"class": "info_temperature"})
        .get_text()
        .replace("도씨", "")
    )

    min_temp = soup.find("span", attrs={"class": "min"}).get_text()
    max_temp = soup.find("span", attrs={"class": "max"}).get_text()

    # ----------------------------------------------
    # Rain probability
    # ----------------------------------------------
    morning_rain_rate = (
        soup.find("span", attrs={"class": "point_time morning"})
        .get_text()
        .strip()
    )

    afternoon_rain_rate = (
        soup.find("span", attrs={"class": "point_time afternoon"})
        .get_text()
        .strip()
    )

    # ----------------------------------------------
    # Fine dust information
    # ----------------------------------------------
    dust = soup.find("dl", attrs={"class": "indicator"})
    pm10 = dust.find_all("dd")[0].get_text()   # Fine dust
    pm25 = dust.find_all("dd")[1].get_text()   # Ultra-fine dust

    # ----------------------------------------------
    # Output
    # ----------------------------------------------
    print(cast)
    print("Current {} (Min {} / Max {})".format(curr_temp, min_temp, max_temp))
    print("Morning {} / Afternoon {}".format(morning_rain_rate, afternoon_rain_rate))
    print()
    print("Fine Dust {}".format(pm10))
    print("Ultra Fine Dust {}".format(pm25))
    print()


# ==================================================
# 4️⃣ Scrape headline news
# ==================================================
def scrape_headline_news():
    print("[Headline News]")

    url = "https://news.naver.com"
    soup = create_soup(url)

    # Get only the top 3 headlines
    news_list = (
        soup.find("ul", attrs={"class": "hdline_article_list"})
        .find_all("li", limit=3)
    )

    for index, news in enumerate(news_list):
        title = news.find("a").get_text().strip()
        link = url + news.find("a")["href"]

        print("{}. {}".format(index + 1, title))
        print("   (Link : {})".format(link))

    print()


# ==================================================
# 5️⃣ Entry point
# ==================================================
if __name__ == "__main__":
    # scrape_weather()        # Fetch today's weather
    scrape_headline_news()   # Fetch headline news
