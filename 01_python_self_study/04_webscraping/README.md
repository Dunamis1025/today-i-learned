# 🕸️ Web Scraping (Python)

This folder contains my **complete learning journey of web scraping with Python**.

It is intentionally structured into:
- **fundamentals**
- **a learning-focused project**

rather than a single monolithic scraper.

⚠️ Important  
Most scripts in this folder are **not expected to work indefinitely**.  
Web scraping breaks by nature — and understanding *why* is part of the lesson.

---

## 🎯 Purpose of This Folder

The goal of this folder is to:

- Understand **how web scraping works**
- Learn how to **read and reason about HTML**
- Experience **why scraping fails in real-world websites**
- Build judgment about **when scraping is appropriate**
- Prepare for the transition to **automation and Selenium**

This is a **learning archive**, not a production toolkit.

---

## 📁 Folder Structure

### 🔹 `01_webscraping_basic/`  
**Web Scraping Fundamentals**

This folder focuses on **core concepts and small experiments**.

Topics covered include:
- How HTTP requests work
- HTML structure (tags, attributes, nesting)
- Using `requests` and `BeautifulSoup`
- Finding elements with `find` / `find_all`
- Handling repeated elements
- Understanding scraping limitations
- Why some pages cannot be scraped with `requests`

This folder acts as a **lab notebook** for fundamentals.

---

### 🔹 `02_webscraping_project_webscraping_assistant/`  
**Learning Project: Personal Web Scraping Assistant**

This folder contains a **step-by-step learning project** that ties
individual concepts together into a single narrative.

Key characteristics:
- Each file represents a learning step
- Code is heavily documented to preserve thought process
- Runtime failure is acceptable and expected
- Emphasis is placed on *why* code is written a certain way

Concepts practiced include:
- Refactoring repeated logic
- Handling inconsistent HTML structures
- Conditional element selection
- Regular expressions in scraping
- Dealing with variable-length content
- Accepting failure as part of scraping

This is not a “tool” — it is a **record of understanding**.

---

## 🧠 What This Folder Teaches

- Scraping is fragile by design
- HTML structure matters more than syntax
- “It worked yesterday” means nothing
- Reading the DOM is a critical skill
- Scraping is often the *wrong* solution
- Automation requires a different mindset

---

## ❌ What This Folder Is NOT

- ❌ A production-ready scraper
- ❌ A reusable crawling framework
- ❌ A guarantee of working scripts

---

## ✅ What This Folder IS

- ✅ A documented learning journey
- ✅ A foundation for browser automation
- ✅ A reference for future Selenium work
- ✅ Proof of understanding web scraping fundamentals

---

## 🚀 Where This Leads Next

This folder intentionally ends here.

The next stage is **Automation**, including:
- Selenium-based scraping
- JavaScript-rendered pages
- Browser control and waits
- Comparing `requests` vs `Selenium`
- Deciding *not* to scrape when inappropriate

This folder marks the **end of web scraping basics**
and the **start of real automation**.

---

📓 *This repository values understanding over execution.*  
🌱 *Each commit represents learning, not just working code.*
