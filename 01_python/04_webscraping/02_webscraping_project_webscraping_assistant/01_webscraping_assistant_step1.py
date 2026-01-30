"""
📌 Project: Personal Assistant using Web Scraping (Learning Record)

This project was created based on a web scraping lecture recorded around 2020.
Due to changes in modern websites (HTML structure updates, dynamic rendering,
React-based pages, JavaScript loading, etc.), this code may NOT work correctly
as of 2025 and beyond.

⚠️ Purpose of this project
- The goal is NOT to produce accurate or real-time results
- This file serves as a learning record to remember:
  - how web scraping was structured
  - how requests and BeautifulSoup were used
  - how to read and analyze HTML documents
- This project acts as a foundation for future upgrades
  using Selenium or official APIs

📌 Project Requirements
1️⃣ Scrape today's weather information for Seoul from Naver
2️⃣ Scrape 3 headline news articles
3️⃣ Scrape 3 IT-related news articles
4️⃣ Scrape today's English conversation from Hackers language website
"""

# ==================================================
# 1️⃣ Required libraries
# ==================================================
# requests        : sends HTTP requests to web pages
# BeautifulSoup   : parses and analyzes HTML documents
import requests
from bs4 import BeautifulSoup


# ==================================================
# 2️⃣ Weather scraping function
# ==================================================
def scrape_weather():
    """
    [Today's Weather]
    - Weather condition (e.g. cloudy, sunny)
    - Current temperature
    - Minimum / Maximum temperature
    - Morning / Afternoon rain probability
    - Fine dust / Ultra-fine dust

    ❗ Due to changes in Naver's page structure,
    this function may no longer work as intended.
    """

    print("[Today's Weather]")

    # Naver search result URL for "Seoul weather"
    url = (
        "https://search.naver.com/search.naver"
        "?where=nexearch"
        "&query=서울+날씨"
    )

    # Request the web page
    res = requests.get(url)
    res.raise_for_status()  # Raise an error if the request fails

    # Parse HTML
    soup = BeautifulSoup(res.text, "lxml")

    # --------------------------------------------------
    # ① Weather description (e.g. Cloudy, Sunny)
    # --------------------------------------------------
    # Example HTML:
    # <p class="cast_txt"> Cloudy, 2° warmer than yesterday </p>
    cast = soup.find("p", attrs={"class": "cast_txt"})
    if cast:
        cast = cast.get_text()
    else:
        cast = "(Weather description not available)"

    # --------------------------------------------------
    # ② Current temperature
    # --------------------------------------------------
    curr_temp = soup.find("p", attrs={"class": "info_temperature"})
    if curr_temp:
        curr_temp = curr_temp.get_text().replace("도씨", "")
    else:
        curr_temp = "Current temperature not available"

    # --------------------------------------------------
    # ③ Minimum / Maximum temperature
    # --------------------------------------------------
    min_temp = soup.find("span", attrs={"class": "min"})
    max_temp = soup.find("span", attrs={"class": "max"})

    min_temp = min_temp.get_text() if min_temp else "?"
    max_temp = max_temp.get_text() if max_temp else "?"

    # --------------------------------------------------
    # ④ Rain probability
    # --------------------------------------------------
    morning = soup.find("span", attrs={"class": "point_time morning"})
    afternoon = soup.find("span", attrs={"class": "point_time afternoon"})

    morning = morning.get_text().strip() if morning else "?"
    afternoon = afternoon.get_text().strip() if afternoon else "?"

    # --------------------------------------------------
    # ⑤ Fine dust / Ultra-fine dust
    # --------------------------------------------------
    dust = soup.find("dl", attrs={"class": "indicator"})
    if dust:
        dds = dust.find_all("dd")
        pm10 = dds[0].get_text() if len(dds) > 0 else "?"
        pm25 = dds[1].get_text() if len(dds) > 1 else "?"
    else:
        pm10 = pm25 = "Not available"

    # --------------------------------------------------
    # Output
    # --------------------------------------------------
    print(cast)
    print(f"Current {curr_temp} (Min {min_temp} / Max {max_temp})")
    print(f"Morning {morning} / Afternoon {afternoon}")
    print()
    print(f"Fine dust {pm10}")
    print(f"Ultra-fine dust {pm25}")
    print()


# ==================================================
# 3️⃣ Main execution block
# ==================================================
if __name__ == "__main__":
    """
    This block ensures the code runs only when this file
    is executed directly.

    👉 Planned extensions
    - scrape_news()
    - scrape_it_news()
    - scrape_english_conversation()
    """
    scrape_weather()
