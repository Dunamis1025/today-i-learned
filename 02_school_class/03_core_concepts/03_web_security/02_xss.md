# Cross-Site Scripting (XSS)

## What is XSS?

Cross-Site Scripting (XSS) is a web security vulnerability that allows an attacker to inject malicious script code, usually JavaScript, into a web page viewed by other users.

In simple words, XSS happens when a website accepts untrusted user input and shows it in the browser without proper filtering or escaping.

Because the browser thinks the script is part of the normal website, it executes the code.

---

## Easy Explanation

Imagine a website has a comment box.

A normal user writes:

> This website is helpful.

But an attacker writes something like:

```html
<script>alert('Hacked')</script>

# Cross-Site Scripting (XSS)

## What is XSS?

Cross-Site Scripting (XSS) is a web security vulnerability that allows an attacker to inject malicious script code, usually JavaScript, into a web page viewed by other users.

In simple words, XSS happens when a website accepts untrusted user input and shows it in the browser without proper filtering or escaping.

Because the browser thinks the script is part of the normal website, it executes the code.

---

## Easy Explanation

Imagine a website has a comment box.

A normal user writes:

> This website is helpful.

But an attacker writes something like:

```html
<script>alert('Hacked')</script>
