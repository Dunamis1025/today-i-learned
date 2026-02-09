📘 Web Scraping Basics
Virtual Environments, Parsers, and Why Things Break
1️⃣ What This Lesson Is Really About

At first glance, this lesson looks like a simple web scraping exercise.

However, the real goal of this stage is:

Understanding how Python environments, libraries, and parsers actually work together.

This knowledge is essential not only for web scraping,
but for any real Python project.

2️⃣ What Is a Virtual Environment?
🔹 One-line definition

A virtual environment is an isolated Python environment created for a specific project.

Each virtual environment has:

Its own Python interpreter

Its own installed libraries

No interference with other projects

🔹 Why Virtual Environments Are Necessary

Without virtual environments:

Project A may require requests==2.25

Project B may require requests==2.32

Project C may not need requests at all

Using a single global Python environment causes:

Version conflicts

Unexpected runtime errors

Difficult debugging

Virtual environments solve this by:

Separating dependencies per project

Making environments reproducible

Preventing library conflicts

🔹 When Should You Use a Virtual Environment?

✅ Any project that installs libraries
✅ Web scraping, data analysis, automation
✅ Even small practice projects

👉 Using a virtual environment should be a default habit.

3️⃣ The First Error: ModuleNotFoundError
❌ Error message
ModuleNotFoundError: No module named 'requests'

❗ Common misunderstanding

“I already installed requests”

“The code must be wrong”

✅ Actual cause

The Python interpreter running the script
was different from the Python interpreter where requests was installed.

In short:

pip install requests was executed in one Python

VS Code executed another Python (inside .venv)

🔹 Correct installation method (best practice)
.\.venv\Scripts\python.exe -m pip install requests


This explicitly installs the library into the virtual environment used by the project.

4️⃣ What Is lxml and Why Is It Needed?
🔹 What is lxml?

lxml is a fast and powerful HTML/XML parsing library.

BeautifulSoup itself does not parse HTML directly.
Instead, it relies on parser libraries, such as:

html.parser (built-in, slower)

lxml (fast, reliable, widely used)

xml (for XML documents)

🔹 The Second Error Explained
soup = BeautifulSoup(res.text, "lxml")


Error:

FeatureNotFound: Couldn't find a tree builder with the features you requested: lxml


Meaning:

BeautifulSoup was instructed to use lxml,
but lxml was not installed in the environment.

🔹 Solution
.\.venv\Scripts\python.exe -m pip install lxml

5️⃣ Final Working Example (English Website)
import requests
from bs4 import BeautifulSoup

url = "https://example.com"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
print(soup.title)

Output
<title>Example Domain</title>


This confirms that:

requests is installed correctly

BeautifulSoup is working

lxml is available

The virtual environment is properly configured

6️⃣ What I Actually Learned Today

❌ What it looks like I learned:

How to scrape a webpage title

⭕ What I truly learned:

How virtual environments work

How Python, pip, and VS Code are connected

How to diagnose library-related errors

The role of parsers like lxml

7️⃣ Why This Knowledge Matters

With this understanding:

Library errors become easy to fix

Debugging becomes systematic

Web scraping becomes reliable

The same workflow applies to real-world projects

🔖 Final Takeaway

Today was not about scraping a website.
It was about learning how to control Python environments correctly.
