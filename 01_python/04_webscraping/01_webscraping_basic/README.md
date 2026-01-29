# Web Scraping Basics

This folder contains **study notes and practice code focused on the fundamentals of web scraping**.

Rather than being a collection of “perfectly working scripts,”  
these files are intended to explain **how web scraping works**, **why certain approaches are used**,  
and **how to think about scraping problems** from the ground up.

All code and notes were written by hand as part of the learning process,  
with the goal of building a solid foundation rather than quick results.

---

## 📌 Purpose of This Folder

- Build a **strong conceptual foundation** for web scraping
- Understand the full flow from HTTP request → HTML → parsing
- Serve as a **personal reference notebook** that I can return to in the future
- Help recall concepts more effectively by revisiting **code I personally typed and annotated**

While online resources and tools like ChatGPT are helpful,  
reviewing my own notes and experiments helps reinforce long-term understanding.

---

## 🧱 Topics Covered

This folder includes practice files and notes related to:

- Basic HTML structure (`html`, `head`, `body`)
- Core HTTP concepts (`GET`, `POST`)
- Sending requests using the `requests` library
- Understanding response objects and status codes
- HTML parsing fundamentals with `BeautifulSoup`
- Tag selection, attribute selection, and text extraction
- List pages vs detail pages
- Limitations of static web scraping
- **Why web scraping fails on JavaScript-rendered websites**

---

## ⚠️ Important Notes

- Some examples are based on **lecture materials from around 2020**
- As a result, certain scripts may no longer work as expected due to:
  - Website structure changes
  - Increased use of JavaScript rendering
  - Bot detection and CAPTCHA
  - Policy or service changes

These files are **not meant to demonstrate up-to-date scraping targets**,  
but rather to preserve **the core principles and thought processes** behind web scraping.

---

## 🧠 How to Use This Folder (For Future Me)

- It is okay if a script does not run successfully
- Focus instead on questions like:
  - What assumptions does this code make?
  - Why did this approach work in the past?
  - Why does it fail today?
  - How would I redesign this using Selenium or other tools?

This folder is a **thinking notebook**, not a solution archive.

---

## 📂 File Organization

- Files are numbered to reflect the learning sequence
- Each file focuses on a single concept or experiment
- Comments are used extensively to capture context and reasoning at the time of writing

---

## 🔗 Next Steps

- `02_webscraping_project_assistant`  
  → Applying these fundamentals in more practical, project-oriented examples
- Advanced topics such as Selenium, automation, and dynamic pages  
  are covered in later folders
