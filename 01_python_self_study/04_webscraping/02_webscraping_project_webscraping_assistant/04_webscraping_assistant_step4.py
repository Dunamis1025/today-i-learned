"""
📌 Project: Personal Web Scraping Assistant (Step 4 – Final)

This file represents the final step of a learning-focused
web scraping project.

It is NOT intended for production automation.

🎯 Learning goals of this step:
- Review the full scraping workflow using requests + BeautifulSoup
- Handle real-world HTML variations and uncertainty
- Use regular expressions to match dynamic element IDs
- Split dynamic content safely using integer division
- Record scraping logic and decision-making for future reference

⚠️ Important notes:
- Naver and Hackers websites frequently change their HTML structure
- This code may not work correctly at runtime
- Accuracy is NOT the goal
- Preserving scraping logic and thought process IS the goal
"""

# ==================================================
# 1️⃣ Required libraries
# ==================================================
import re                  # For regular expression matching
import requests
from bs4 import BeautifulSoup


# ==================================================
# 2️⃣ Common helper: URL → BeautifulSoup object
# ==================================================
def create_soup(url):
    """
    Sends an HTTP request to the given URL and
    converts the response HTML into a BeautifulSoup object.
    """
    res = requests.get(url)
    res.raise_for_status()  # Raise an exception if the request fails
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
# 4️⃣ Weather scraping
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
# 5️⃣ Headline news scraping
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
# 6️⃣ IT news scraping (conditional structure handling)
# ==================================================
def scrape_it_news():
    print("[IT News]")

    url = "https://news.naver.com/breakingnews/section/105/230"
    soup = create_soup(url)

    # Fetch only 3 IT news articles
    news_list = soup.find("ul", attrs={"class": "type06_headline"}).find_all("li", limit=3)

    for index, news in enumerate(news_list):
        # Default assumption: use the first <a> tag
        a_idx = 0

        # Check whether the news item includes an image
        img = news.find("img")
        if img:
            # Image-based news may require selecting the second <a> tag
            a_idx = 1

        # Use a variable to simplify complex logic
        a_tag = news.find_all("a")[a_idx]
        title = a_tag.get_text().strip()
        link = a_tag["href"]

        print_news(index, title, link)

    print()


# ==================================================
# 7️⃣ Daily English conversation scraping
# ==================================================
def scrape_english():
    """
    🎯 Goal:
    Scrape daily English conversation examples from Hackers.

    🧠 Key ideas:
    - The number of sentences may change daily
    - English and Korean sentences are mixed in a single list
    - The list is split into two halves dynamically
    - Integer division (//) prevents decimal index issues
    """
    print("[Today's English Conversation]")

    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english"
    soup = create_soup(url)

    # Find all div elements whose id starts with "conv_kor_t"
    sentences = soup.find_all("div", attrs={"id": re.compile("^conv_kor_t")})

    # Determine the midpoint safely using integer division
    half = len(sentences) // 2

    print("English Script")
    for sentence in sentences[half:]:
        print(sentence.get_text().strip())

    print()
    print("Korean Script")
    for sentence in sentences[:half]:
        print(sentence.get_text().strip())

    print()


# ==================================================
# 8️⃣ Entry point
# ==================================================
if __name__ == "__main__":
    scrape_weather()        # Weather information
    scrape_headline_news()  # Headline news
    scrape_it_news()        # IT news
    scrape_english()        # Daily English conversation
