# HTTP GET vs POST (Web Scraping Basics)

## One-line Summary
**GET requests retrieve data.  
POST requests send data to be processed.**

---

## What is an HTTP request?

When a browser or a Python script communicates with a server,  
it sends an **HTTP request**.

Among many request types, **GET** and **POST** are the most common  
and the most important for web scraping.

---

## GET Method

### Concept
- Used to **request data from a server**
- Request information is included in the **URL**

### Simple analogy
> “Please show me this page.”

### Key characteristics
- Parameters are visible in the URL  
- Can be bookmarked  
- Can be cached by the browser  
- Should not change server data (read-only)

### Example URL
https://example.com/search?q=python&page=1

csharp
Copy code

### Python example
```python
import requests

url = "https://example.com/search"
params = {
    "q": "python",
    "page": 1
}

response = requests.get(url, params=params)
print(response.text)
GET in web scraping
Most commonly used method

Ideal for:

Public pages

Lists, rankings, articles

Pages that open directly via URL

Query Parameters and params in GET Requests
What are query parameters?
Query parameters are additional pieces of information
attached to the end of a URL to tell the server how to respond.

They appear after ? in the URL and are written as key=value pairs.

Basic structure
arduino
Copy code
https://example.com/path?key=value&key2=value2
? → start of query parameters

key=value → condition or option

& → separator between parameters

Example
arduino
Copy code
https://example.com/search?q=python&page=2
q=python → search keyword

page=2 → page number

Why use params in requests.get()?
Instead of manually writing query parameters into the URL,
Python’s requests library allows using a dictionary via params.

❌ Not recommended
python
Copy code
url = "https://example.com/search?q=python&page=1"
requests.get(url)
Problems:

Poor readability

Hard to manage when parameters increase

Manual handling of special characters

✅ Recommended
python
Copy code
params = {
    "q": "python",
    "page": 1
}

requests.get(url, params=params)
Benefits:

Cleaner and more readable

Automatic URL encoding

Standard practice in real-world projects

What actually happens internally?
python
Copy code
requests.get(url, params=params)
is automatically converted into:

arduino
Copy code
https://example.com/search?q=python&page=1
When query parameters are commonly used
Search keywords

Page numbers

Filters and sorting options

Result limits

Example:

python
Copy code
params = {
    "keyword": "laptop",
    "sort": "price",
    "limit": 20
}
Resulting URL:

bash
Copy code
?keyword=laptop&sort=price&limit=20
POST Method
Concept
Used to send data to the server for processing

Data is sent inside the request body, not the URL

Simple analogy
“Here is my form. Please process it.”

Key characteristics
Data is not visible in the URL

Cannot be bookmarked

Not cached by default

Often used for login, search forms, submissions

Python example
python
Copy code
import requests

url = "https://example.com/login"
data = {
    "username": "test_user",
    "password": "password123"
}

response = requests.post(url, data=data)
print(response.text)
POST in web scraping
Commonly used when:

Login is required

Forms are submitted

The site uses internal APIs

GET vs POST Comparison
Feature	GET	POST
Purpose	Retrieve data	Send data
Data location	URL (query parameters)	Request body
Visible in URL	Yes	No
Bookmarkable	Yes	No
Cacheable	Yes	No
Common in scraping	Very common	Less common

Why GET Sometimes Fails in Scraping
Sometimes:

requests.get() returns empty or incomplete data

But the browser shows the full page

This usually happens because:

The page uses JavaScript

Data is fetched via POST-based APIs

Login, cookies, or sessions are required

In such cases, checking the browser’s Network tab is essential.

Key Takeaway
GET = ask the server to show data

POST = send data to the server to handle

Query parameters = conditions attached to GET requests

Understanding these concepts is crucial for:

Web scraping

API usage

Login automation

Dynamic websites

