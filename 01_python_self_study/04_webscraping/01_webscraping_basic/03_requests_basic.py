import requests

# Send an HTTP request to the website
# This is similar to opening the page in a browser,
# but done programmatically using Python
res = requests.get("http://google.com")

# Raise an error if the request was not successful (e.g. 404, 500)
res.raise_for_status()

# The response content is HTML text
# Print its length to understand how much data was received
print(len(res.text))

# Print the raw HTML source of the page
print(res.text)

# Save the downloaded HTML into a local file
# This allows us to open and inspect the page structure manually
with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)
