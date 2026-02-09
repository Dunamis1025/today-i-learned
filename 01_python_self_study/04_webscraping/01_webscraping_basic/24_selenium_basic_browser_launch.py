"""
📌 Selenium Basic Example
(Environment Setup → Common Pitfalls → Old vs New Driver Handling → Browser Launch)

This script documents my first successful Selenium setup
using Selenium 4 and modern ChromeDriver management.

Rather than only showing the final working code,
this file intentionally records:
- the installation order
- common beginner mistakes
- and the difference between legacy and modern Selenium usage

--------------------------------------------------
🧭 Setup & Learning Flow
--------------------------------------------------

1️⃣ Installed Selenium via command prompt:
   pip install selenium

2️⃣ Encountered an error:
   ModuleNotFoundError: No module named 'selenium'

   → Cause:
     Selenium was installed in the system Python,
     but the script was executed inside a virtual environment (.venv).

3️⃣ Solution:
   Installed Selenium again inside the active virtual environment:
   pip install selenium

   (Note: I did NOT use 'pip install -U selenium'.
    The installation still succeeded because the latest version
    was installed by default.)

4️⃣ Verified installation:
   pip show selenium
   → Confirmed Selenium 4.x was installed correctly.

--------------------------------------------------
🧠 Why chromedriver.exe exists in older tutorials
--------------------------------------------------

In older Selenium versions (Selenium 3.x and earlier):

- Users had to manually download chromedriver.exe
- The driver file was placed inside the project folder
- The browser was launched like this:

    webdriver.Chrome("./chromedriver.exe")

This is why older tutorials often show:
- a visible chromedriver.exe file in the workspace
- manual version matching between Chrome and ChromeDriver

--------------------------------------------------
🚀 Why chromedriver.exe is NOT needed here
--------------------------------------------------

With Selenium 4.x (current standard):

- ChromeDriver is managed automatically by Selenium
- webdriver.Chrome() detects the installed Chrome version
- The correct driver is downloaded and cached internally
- No executable file appears in the project directory

Therefore:
- chromedriver.exe is not visible in this workspace
- No manual path configuration is required
- This is the recommended and modern approach

--------------------------------------------------
💡 Key Takeaways
--------------------------------------------------

- Manual ChromeDriver downloads are legacy behavior.
- webdriver.Chrome() is sufficient in Selenium 4+.
- A delay (time.sleep) is required to keep the browser open,
  otherwise it closes immediately when the script finishes.

📅 Learning context:
- Selenium 4.x
- Latest version of Google Chrome
"""

# --------------------------------------------------
# 1️⃣ Import webdriver from Selenium
#    → Used to control the Chrome browser via Python
# --------------------------------------------------
from selenium import webdriver

# --------------------------------------------------
# 2️⃣ Import time module
#    → Used to pause execution so the browser stays open
# --------------------------------------------------
import time


# --------------------------------------------------
# 3️⃣ Launch the Chrome browser (modern Selenium approach)
#
# No chromedriver.exe path is specified here.
# Selenium automatically manages the correct driver version.
# --------------------------------------------------
driver = webdriver.Chrome()


# --------------------------------------------------
# 4️⃣ Navigate to the Naver homepage
#
# driver.get(URL)
# → Equivalent to typing the URL into the address bar
# --------------------------------------------------
driver.get("https://www.naver.com")


# --------------------------------------------------
# 5️⃣ Keep the browser open for inspection
#
# Without this delay:
# - The script finishes immediately
# - The browser opens briefly and closes right away
# --------------------------------------------------
time.sleep(10)


# --------------------------------------------------
# (Optional)
# Explicitly close the browser when finished:
#
# driver.quit()
# --------------------------------------------------
