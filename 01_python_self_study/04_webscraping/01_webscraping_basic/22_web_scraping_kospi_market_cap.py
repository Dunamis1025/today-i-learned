import csv
import requests
from bs4 import BeautifulSoup

# ==========================================================
# 📌 Naver Finance - Scraping KOSPI Market Cap Rankings
# ==========================================================
# This script scrapes stock data from Naver Finance,
# specifically the KOSPI market (sosok=0),
# and extracts market capitalization ranking data.
#
# Key learning points:
# - Sending HTTP requests using requests
# - Parsing HTML with BeautifulSoup
# - Understanding table / tbody / tr / td structures
# - Cleaning unnecessary whitespace like \n and \t
# ==========================================================


# Base URL for KOSPI market cap ranking pages
# Page numbers are appended to this URL
url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="


# Define page range
# Currently set to page 1 only for practice
# (Can be extended to range(1, 51) later)
for page in range(1, 2):

    # ------------------------------------------------------
    # 1️⃣ Send HTTP GET request
    # ------------------------------------------------------
    # requests.get():
    #   - Sends an HTTP GET request to the specified URL
    #
    # url + str(page):
    #   - url is a string
    #   - page is an integer
    #   - Integers must be converted to strings before concatenation
    #
    # Example:
    #   page = 1
    #   Final URL:
    #   https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page=1
    res = requests.get(url + str(page))


    # ------------------------------------------------------
    # 2️⃣ Stop immediately if the request failed
    # ------------------------------------------------------
    # res.raise_for_status():
    #
    # - Raises an exception if the HTTP response status
    #   is not 200 (OK)
    #
    # This prevents silent failures such as:
    # - 404 (Not Found)
    # - 403 (Forbidden)
    # - 500 (Server Error)
    res.raise_for_status()


    # ------------------------------------------------------
    # 3️⃣ Parse HTML (string → structured DOM)
    # ------------------------------------------------------
    # res.text:
    #   - Raw HTML content returned from the server
    #
    # BeautifulSoup(..., "lxml"):
    #   - Converts HTML into a DOM tree
    #   - Makes it easy to search and navigate elements
    soup = BeautifulSoup(res.text, "lxml")


    # ------------------------------------------------------
    # 4️⃣ Get all table rows (tr) containing stock data
    # ------------------------------------------------------
    # HTML structure:
    #
    # <table class="type_2">
    #   <tbody>
    #     <tr> ... </tr>   ← actual stock data rows
    #     <tr> ... </tr>
    #   </tbody>
    # </table>
    #
    # Steps:
    # 1) Find table with class="type_2"
    # 2) Move into tbody
    # 3) Extract all tr elements
    data_rows = (
        soup
        .find("table", attrs={"class": "type_2"})
        .find("tbody")
        .find_all("tr")
    )


    # ------------------------------------------------------
    # 5️⃣ Process each row (each stock entry)
    # ------------------------------------------------------
    # for loop is used because:
    # - Each <tr> represents one stock
    # - We want to process all stocks sequentially
    for row in data_rows:

        # --------------------------------------------------
        # 6️⃣ Extract all columns (td) from the row
        # --------------------------------------------------
        # Each td represents a single data field
        # (rank, stock name, price, etc.)
        columns = row.find_all("td")


        # --------------------------------------------------
        # 7️⃣ Skip meaningless rows
        # --------------------------------------------------
        # len(columns):
        # - Counts how many td elements exist in the row
        #
        # Reason:
        # - The table includes empty rows, ads,
        #   and separator rows with no actual data
        #
        # If td count is 1 or less,
        # this row does not contain valid stock data
        if len(columns) <= 1:
            continue   # Skip to the next row


        # --------------------------------------------------
        # 8️⃣ Extract and clean text data
        # --------------------------------------------------
        # get_text(strip=True):
        # - Extracts text inside the tag only
        # - strip=True automatically removes:
        #   leading/trailing whitespace,
        #   newlines (\n),
        #   and tabs (\t)
        #
        # List comprehension:
        # - Applies the same cleanup to all td elements
        data = [column.get_text(strip=True) for column in columns]


        # --------------------------------------------------
        # 9️⃣ Print result (for verification)
        # --------------------------------------------------
        print(data)
