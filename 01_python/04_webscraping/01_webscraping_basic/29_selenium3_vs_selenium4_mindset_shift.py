from selenium import webdriver
from selenium.webdriver.common.by import By

# ==================================================
# ⚠️ This example is written with a Selenium 3 mindset
# - In modern Selenium 4 environments (2024~),
#   this code may not work as expected
# - This file exists for learning and comparison purposes:
#   "This is how it used to be done"
# ==================================================

# ==================================================
# 1️⃣ Launch browser
# ==================================================
# In the Selenium 3 era, it was common to explicitly
# specify the chromedriver.exe path.
browser = webdriver.Chrome()
browser.maximize_window()

# ==================================================
# 2️⃣ Open Naver Flights page
# ==================================================
browser.get("https://flight.naver.com/")

# ==================================================
# 3️⃣ Select departure date
# ==================================================
# ❗ In Selenium 3-style code:
# - Developers often did NOT wait for the page to load
# - Elements were accessed immediately
#
# ❗ It was also common to assume static text
# and rely heavily on LINK_TEXT selectors.
browser.find_element(By.LINK_TEXT, "가는 날").click()

# ==================================================
# 4️⃣ Select dates (index-based approach)
# ==================================================
# ❗ A very common Selenium 3 tutorial pattern:
# - Assume the same text ("27", "28") appears multiple times
# - Use list indexing to distinguish current month vs next month
#
# ⚠️ This approach is extremely fragile and
# tightly coupled to the DOM structure.

# Select 27th and 28th of the current month
browser.find_elements(By.LINK_TEXT, "27")[0].click()  # [0] → current month
browser.find_elements(By.LINK_TEXT, "28")[0].click()  # [0] → current month

# Select 27th and 28th of the next month
browser.find_elements(By.LINK_TEXT, "27")[1].click()  # [1] → next month
browser.find_elements(By.LINK_TEXT, "28")[1].click()  # [1] → next month

# Select 27th of current month + 28th of next month
browser.find_elements(By.LINK_TEXT, "27")[0].click()
browser.find_elements(By.LINK_TEXT, "28")[1].click()

# ==================================================
# 5️⃣ Select destination (Jeju)
# ==================================================
# ❗ Absolute XPath was commonly used in Selenium 3 tutorials
#
# ⚠️ This is extremely brittle:
# if even one div in the hierarchy changes,
# the selector will break.
browser.find_element(
    By.XPATH,
    "//*[@id='__next']/div/main/div[9]/div[2]/div[2]/div[2]/ul[1]/li[1]/button"
).click()

# ==================================================
# 6️⃣ Click flight search button
# ==================================================
# ❗ Assumes the button text matches exactly
browser.find_element(By.LINK_TEXT, "항공권 검색").click()

# ==================================================
# 7️⃣ Print the first search result
# ==================================================
# ❗ Assumes search results are already loaded
# (Little to no waiting logic — typical of older code)
elem = browser.find_element(
    By.XPATH,
    "//*[@id='__next']/div/main/div[4]/div/div[2]/div[2]/div[1]/div/button"
)
print(elem.text)

# ==================================================
# 🔚 Keep browser open (for learning purposes)
# ==================================================
input("Press Enter to close the browser...")
browser.quit()

# ==================================================
# 🔄 Mindset Shift: Selenium 3 → Selenium 4
#
# The key difference is not syntax, but mindset:
# Selenium 3 assumes the page is ready.
# Selenium 4 waits until the page proves it is ready.
# ==================================================

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ==================================================
# 1️⃣ Launch browser
# ==================================================
# With Selenium 4, there is no need to manually specify chromedriver.exe.
# Selenium automatically manages the correct driver
# based on the installed Chrome version.
browser = webdriver.Chrome()
browser.maximize_window()

# Create a WebDriverWait object
# 👉 Waits up to 10 seconds until the given condition is met
wait = WebDriverWait(browser, 10)

# ==================================================
# 2️⃣ Open Naver Flight page
# ==================================================
browser.get("https://flight.naver.com/")

# ==================================================
# 3️⃣ Select destination (Jeju)
# ==================================================
# Naver Flight is a React-based dynamic web application,
# so elements must be waited for until they become clickable.
destination_btn = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), '도착')]"))
)
destination_btn.click()

# Select the destination using text-based matching
# rather than relying on element position.
jeju = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), '제주')]"))
)
jeju.click()

# ==================================================
# 4️⃣ Select departure and return dates
# ==================================================
# The old "Select departure date" text no longer exists.
# Now only a "Departure date" button is provided.
depart_btn = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), '가는 날')]"))
)
depart_btn.click()

# When selecting dates, use the visible text itself
# instead of fixed positions or indexes.
depart_day = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//b[text()='27']"))
)
depart_day.click()

return_day = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//b[text()='28']"))
)
return_day.click()

# ==================================================
# 5️⃣ Click search button
# ==================================================
search_btn = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), '검색')]"))
)
search_btn.click()

# ==================================================
# 🔚 Keep browser open for learning purposes
# ==================================================
input("Press Enter to close the browser...")
browser.quit()
