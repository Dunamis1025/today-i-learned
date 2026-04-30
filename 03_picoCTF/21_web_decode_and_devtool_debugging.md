# 21_web_decode_and_devtool_debugging.md

## Challenge Information
* **Source:** picoCTF 2024
* **Category:** Web Exploitation
* **Difficulty:** Easy
* **Learning Objectives:** Web Inspector (DevTools) proficiency, Base64 decoding, and troubleshooting browser security features.

## Problem Description
The challenge provides a website and asks if you know how to use the **Web Inspector**. The goal is to find a hidden flag, which may or may not be encoded, by exploring the web page's source code and included files.

## Solution Steps

### 1. Exploration and Navigation
* Launched the challenge instance and navigated through the site menu (**Home, About, Contact**).
* Recognized the hint **"Keep Navigating"** on the home page, suggesting the flag is likely hidden in a sub-page.

### 2. Inspecting the Source Code
* Navigated to the **'About'** page and opened the **Browser Developer Tools (F12)**.
* Inspected the **Elements** tab and found a suspicious `section` tag with a unique attribute:
    * `<section class="about" notify_true="cGljb0NURnt3ZWJfc3VjYzNzc2Z1bGx5X2QzYzBkZWRfZGYwZGE3Mjd9">`

### 3. Decoding the Flag
* Identified the string as **Base64** encoding due to its character set and structure.
* **Troubleshooting Encountered:**
    * **CyberChef Issue:** Attempted decoding but initially received garbled output due to accidental character insertion (e.g., an extra 'i') during manual copying.
    * **Browser Console Limitation:** Tried using the `atob()` function in the DevTools console, but the browser blocked pasting for security (Self-XSS protection).
    * **Webshell Limitation:** Attempted `atob()` in the Linux-based Webshell, which resulted in a `syntax error` because `atob()` is a JavaScript function, not a Bash command.

### 4. Resolution
* **DevTools Bypass:** Typed `allow pasting` in the console to unlock the paste functionality.
* **Verification:** Re-extracted the clean string directly from the HTML elements to ensure data integrity.
* **Final Decoding:** Used **CyberChef** (From Base64) with the correct string:
    * **Input:** `cGljb0NURnt3ZWJfc3VjYzNzc2Z1bGx5X2QzYzBkZWRfZGYwZGE3Mjd9`
    * **Output:** `picoCTF{web_succ3ssfully_d3c0ded_df0da727}`

## Key Takeaways
1. **Source of Truth:** Always copy strings directly from the raw HTML elements to avoid human error or invisible character insertion.
2. **DevTools Security:** Modern browsers require an explicit `allow pasting` command to enable code execution in the console for certain environments.
3. **Tool Context:** Use `atob()` for JavaScript (Browser) and `echo "string" | base64 -d` for Linux (Terminal/Webshell).
