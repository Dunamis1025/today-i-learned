"""
📌 Selenium REPL Practice Notes - Daum Search Automation (Basics)

This file is NOT an auto-run script.
👉 It is a learning note written while practicing Selenium
👉 line by line in the Python REPL (>>> prompt)
👉 so that the concepts are easy to recall later.

=================================================
🎯 Key Learning Goals
=================================================
1️⃣ Understand what Python REPL is
2️⃣ Understand the role of the Selenium browser object
3️⃣ Clearly distinguish DOM / node / element concepts
4️⃣ Understand that an element is only valid while attached to the current DOM
5️⃣ Experience why elements must be re-located after page navigation

This file is:
❌ NOT meant for direct execution
⭕ Meant for concept review and GitHub notes
"""

# ==================================================
# 0️⃣ Python REPL Basics
# ==================================================

"""
📌 What is Python REPL?

REPL = Read – Eval – Print – Loop

It is an interactive execution environment where Python
reads your code line by line and responds immediately.

When you type `python` in a terminal and see:
>>> 
You are in REPL mode.

Example:
>>> 1 + 2
3
>>> x = 10
>>> x * 3
30

REPL is not for writing finished programs.
It is for experimenting and having a conversation with Python.
"""

"""
🔁 What each letter in REPL means

R = Read
👉 Python reads the line you just typed as text.

E = Eval (Evaluate)
👉 Python interprets the meaning of the code and executes it.
👉 This is where syntax errors and runtime errors are decided.

P = Print
👉 If the code produces a result, Python prints it to the screen.

L = Loop
👉 Python goes back to the >>> prompt and waits for the next line.

📌 One sentence to remember:
REPL is a loop where Python keeps reading, evaluating,
printing results, and waiting for your next command.
"""

"""
🔁 The "E" in REPL = Eval (Most Important)

Eval stands for Evaluate.

During the Eval step, Python:
- checks if the syntax is valid,
- executes the code,
- calculates the result,
- and decides whether an error occurs.

📌 One sentence to remember:
Eval = "The moment where Python decides the fate of the code,
including whether it will fail or succeed."
"""

# ==================================================
# 1️⃣ DOM / node / element Concepts (Very Important)
# ==================================================

"""
📌 DOM (Document Object Model)

DOM is:
👉 a tree structure created by the browser in memory
👉 after reading the HTML of a web page.

Think of it as a tree:
- DOM = the entire tree
- node = each individual piece of the tree
"""

"""
📌 What is a node?

A node is:
👉 the smallest unit that makes up the DOM tree.

Example HTML:
<html>
  <body>
    <input name="q" />
    <button>Search</button>
  </body>
</html>

DOM tree representation:
Document
 └─ html      (node)
    └─ body   (node)
       ├─ input   (node)
       └─ button (node)

👉 Every tag becomes a node in the DOM.
"""

"""
📌 What is an element?

An element is:
👉 a node that corresponds to an HTML tag.

In Selenium:
element =
👉 a reference (handle) to an element node
👉 that currently exists in the DOM tree.

Important:
- The element variable does NOT store HTML itself.
- It only points to a node inside the current DOM.
"""

"""
📌 Why do we say "an element attached to the DOM at that moment"?

Example:
elem = browser.find_element(By.NAME, "q")

This means:
👉 Selenium searches the current DOM,
👉 finds the input node with name="q",
👉 and gives you a reference to that node.

When page navigation occurs:
- the old DOM is destroyed
- all old nodes are removed
- the element reference becomes invalid (stale)

That is why:
Page navigation = DOM replacement
DOM replacement = node removal
Node removal = element becomes invalid
"""

# ==================================================
# 2️⃣ Selenium Required Imports
# ==================================================

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# ==================================================
# 3️⃣ Create Browser Object
# ==================================================

# The browser object is NOT created automatically.
# You must explicitly create it using webdriver.
browser = webdriver.Chrome()

# Open Daum main page
browser.get("https://www.daum.net")


# ==================================================
# 4️⃣ Locate Search Input Element and Type Keyword
# ==================================================

# elem represents an element node currently attached to the DOM
elem = browser.find_element(By.NAME, "q")

elem.send_keys("Nado Coding")
elem.send_keys(Keys.ENTER)


# ==================================================
# 5️⃣ Re-locate Element After Page Navigation
# ==================================================

# Page navigation replaces the DOM,
# so the previous element reference is no longer valid.
elem = browser.find_element(By.XPATH, '//*[@id="daumBtnSearch"]')

elem.click()


# ==================================================
# 6️⃣ End Practice
# ==================================================

browser.quit()


"""
=================================================
❗ Final Key Takeaways
=================================================

✅ DOM = the web page structure tree created by the browser
✅ node = the smallest building block of the DOM
✅ element = a node corresponding to an HTML tag
✅ Selenium element = a reference to a node attached to the current DOM

📌 Core rule:
Page navigation = DOM replacement
DOM replacement = node removal
Node removal = element becomes invalid
Invalid element = must call find_element again

This file serves as a conceptual checkpoint
before moving on to real Selenium automation.
"""
