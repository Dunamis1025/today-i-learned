import csv                      # Module for saving data as a CSV file
import time                     # Module for adding short delays between requests (server etiquette)
import requests                 # Module for fetching web pages (HTML)
from bs4 import BeautifulSoup   # Module for parsing and analyzing HTML

# ==========================================================
# 📌 Goal
# Scrape the top KOSPI market-cap stocks from Naver Finance
# (pages 1 to 5) and save the data into a CSV file.
#
# ✅ Key points
# - Fetch HTML using requests
# - Parse table data using BeautifulSoup
# - Save results to CSV (utf-8-sig to prevent Excel encoding issues)
# ==========================================================

# ----------------------------------------------------------
# 1) Base URL for Naver Finance KOSPI market-cap pages
#    Only the page number changes (1 ~ 5)
# ----------------------------------------------------------
BASE_URL = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

# ----------------------------------------------------------
# 2) User-Agent header
#    Makes the request look like it comes from a real browser
#    (basic etiquette to reduce the chance of being blocked)
# ----------------------------------------------------------
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/143.0.0.0 Safari/537.36"
    )
}

# ----------------------------------------------------------
# 3) Output CSV file name
#    ✅ utf-8-sig prevents Korean text from breaking in Excel
#    ✅ newline="" prevents extra blank lines
# ----------------------------------------------------------
filename = "kospi_market_cap_top_200.csv"

# ----------------------------------------------------------
# 4) Open CSV file in write mode
#    Using 'with' ensures the file is closed automatically
# ----------------------------------------------------------
with open(filename, "w", encoding="utf-8-sig", newline="") as f:

    # ------------------------------------------------------
    # 5) Create CSV writer
    #    - writerow(): writes a single row
    # ------------------------------------------------------
    writer = csv.writer(f)

    # ------------------------------------------------------
    # 6) Write CSV header
    #    Column names are based on the table shown on Naver
    # ------------------------------------------------------
    header = [
        "Rank", "Company", "Current Price", "Change", "Change Rate",
        "Par Value", "Market Cap", "Outstanding Shares", "Foreign Ownership",
        "Volume", "PER", "ROE"
    ]
    writer.writerow(header)

    # ------------------------------------------------------
    # 7) Loop through pages 1 to 5
    # ------------------------------------------------------
    for page in range(1, 6):

        # --------------------------------------------------
        # 7-1) Build page-specific URL
        # --------------------------------------------------
        url = BASE_URL + str(page)

        # --------------------------------------------------
        # 7-2) Send HTTP GET request
        # --------------------------------------------------
        res = requests.get(url, headers=headers)

        # --------------------------------------------------
        # 7-3) Raise an error if the request failed
        # --------------------------------------------------
        res.raise_for_status()

        # --------------------------------------------------
        # 7-4) Parse the HTML into a DOM structure
        # --------------------------------------------------
        soup = BeautifulSoup(res.text, "lxml")

        # --------------------------------------------------
        # 7-5) Locate the main data table
        #    The target table has class="type_2"
        # --------------------------------------------------
        table = soup.find("table", attrs={"class": "type_2"})

        # If the table structure changes, skip this page
        if table is None:
            print(f"[Warning] Table not found on page {page}")
            continue

        # --------------------------------------------------
        # 7-6) Extract all rows inside <tbody>
        # --------------------------------------------------
        tbody = table.find("tbody")
        rows = tbody.find_all("tr")

        # --------------------------------------------------
        # 7-7) Extract data from each row
        # --------------------------------------------------
        for row in rows:

            cols = row.find_all("td")

            # Skip empty or separator rows
            if len(cols) <= 1:
                continue

            # Clean and extract text from each column
            data = [col.get_text(strip=True) for col in cols]

            # Write one row of stock data
            writer.writerow(data)

        # --------------------------------------------------
        # 7-8) Progress output
        # --------------------------------------------------
        print(f"✅ Page {page} saved")

        # --------------------------------------------------
        # 7-9) Short delay to reduce server load (polite scraping)
        # --------------------------------------------------
        time.sleep(0.3)

print(f"\n🎉 Done! Data saved to '{filename}'")
print("📌 The file should open correctly in Excel using utf-8-sig encoding.")
