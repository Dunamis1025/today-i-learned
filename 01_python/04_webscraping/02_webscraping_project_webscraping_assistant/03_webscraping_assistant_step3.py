"""
📌 Project: Personal Web Scraping Assistant (Step 3 – IT News)

This file is part of a learning-focused web scraping project.
It is NOT intended for production automation.

✅ Key learning points in this step:
1) Refactoring repeated logic into reusable functions
   - create_soup(url)
   - print_news(index, title, link)

2) Handling conditional HTML structures
   - Some news articles include images (<img>)
   - When an image exists, the target <a> tag structure changes
   - A conditional index (a_idx) is used to select the correct <a> tag

3) Improving readability with intermediate variables
   - Assigning complex selections to variables like `a_tag`
   - Makes the code easier to read, debug, and revisit later

⚠️ Notes:
- Naver News frequently changes its HTML structure
- This code may no longer work correctly at runtime
- The goal is to preserve scraping logic and thought process,
  not guaranteed execution
"""

# ==================================================
# 1️⃣ Required libraries
# ==================================================
import requests
from bs4 import BeautifulSoup


# ==================================================
# 2️⃣ Common helper: URL → BeautifulSoup object
# ==================================================
def create_soup(url):
    """
    Sends an HTTP request to the given URL
    and converts the response HTML into
    a BeautifulSoup object.
    """
    res = requests.get(url)
    res.raise_for_status()  # Raise an exception on request failure
    soup = BeautifulSoup(res.text, "lxml")
    return soup


# ==================================================
# 3️⃣ Common helper: unified news output format
# ==================================================
def print_news(index, title, link):
    """
    Prints news items in a consistent format.
    index starts from 0, so +1 is applied for display.
    """
    print("{}. {}".format(index + 1, title))
    print("  (Link : {})".format(link))


# ==================================================
# 4️⃣ Weather scraping (review from previous step)
# ==================================================
def scrape_weather():
    print("[Today's Weather]")

    url = "https://search.naver.com/search.naver?where=nexearch&query=Seoul+weather"
    soup = create_soup(url)

    # ----------------------------------------------
    # Weather description (e.g. Cloudy, warmer than yesterday)
    # ----------------------------------------------
    cast = soup.find("p", attrs={"class": "cast_txt"}).get_text()

    # ----------------------------------------------
    # Current / minimum / maximum temperature
    # ----------------------------------------------
    curr_temp = soup.find("p", attrs={"class": "info_temperature"}).get_text().replace("도씨", "")
    min_temp = soup.find("span", attrs={"class": "min"}).get_text()
    max_temp = soup.find("span", attrs={"class": "max"}).get_text()

    # ----------------------------------------------
    # Rain probability (morning / afternoon)
    # ----------------------------------------------
    morning_rain_rate = soup.find("span", attrs={"class": "point_time morning"}).get_text().strip()
    afternoon_rain_rate = soup.find("span", attrs={"class": "point_time afternoon"}).get_text().strip()

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
# 5️⃣ Headline news scraping (review)
# ==================================================
def scrape_headline_news():
    print("[Headline News]")

    base_url = "https://news.naver.com"
    soup = create_soup(base_url)

    # Fetch only the top 3 headline articles
    news_list = soup.find("ul", attrs={"class": "hdline_article_list"}).find_all("li", limit=3)

    for index, news in enumerate(news_list):
        title = news.find("a").get_text().strip()
        link = base_url + news.find("a")["href"]
        print_news(index, title, link)

    print()


# ==================================================
# 6️⃣ IT news scraping (main focus of this step)
# ==================================================
def scrape_it_news():
    """
    🎯 Goal:
    Fetch and display the top 3 IT-related news articles.

    🧠 Key concept:
    - Some news items include an image (<img>)
    - When an image exists, multiple <a> tags may be present
    - The desired title/link may not be in the first <a> tag
    - A conditional index (a_idx) is used to select the correct <a>
    """
    print("[IT News]")

    url = "https://news.naver.com/breakingnews/section/105/230"
    soup = create_soup(url)

    # Get only 3 IT news articles
    news_list = soup.find("ul", attrs={"class": "type06_headline"}).find_all("li", limit=3)

    for index, news in enumerate(news_list):
        # Default assumption: use the first <a> tag
        a_idx = 0

        # ------------------------------------------
        # Conditional handling for image-based news
        # ------------------------------------------
        img = news.find("img")
        if img:
            # If an image exists, the desired <a> tag
            # may be the second one
            a_idx = 1

        # ------------------------------------------
        # Use a variable to simplify complex logic
        # ------------------------------------------
        a_tag = news.find_all("a")[a_idx]

        title = a_tag.get_text().strip()
        link = a_tag["href"]

        print_news(index, title, link)

    print()


# ==================================================
# 7️⃣ Entry point
# ==================================================
if __name__ == "__main__":
    # scrape_weather()        # Today's weather
    # scrape_headline_news()  # Headline news
    scrape_it_news()          # IT news
