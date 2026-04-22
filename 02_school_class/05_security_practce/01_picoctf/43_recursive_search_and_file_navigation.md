# picoCTF - First Find (General Skills)

## Challenge Description
- **Author:** LT 'SYREAL' JONES
- **Category:** General Skills
- **Difficulty:** Easy
- **Task:** Unzip the provided archive and find the file named `uber-secret.txt` to retrieve the flag.

## Problem Analysis
The challenge provides a ZIP file containing a complex and deeply nested directory structure. Manually navigating through each folder using `cd` and `ls` is inefficient. The goal is to utilize efficient Linux command-line tools to locate a specific file based on its name.

## Solution Steps

### 1. Download and Extract
First, the archive is downloaded from the picoCTF server and extracted.
```bash
# Downloading the file
wget https://artifacts.picoctf.net/c/501/files.zip

# Unzipping the archive
unzip files.zip
```
### 2. Efficient File Searching
Instead of manual traversal, the find command is used to search the entire directory tree starting from the current location.

```bash
# Searching for the specific file name
find . -name "uber-secret.txt"
```
Output: ./files/adequate_books/more_books/.secret/deeper_secrets/deepest_secrets/uber-secret.txt

### 3. Retrieving the Flag
Once the path is identified, the cat command is used to read the content of the file.

```bash
# Reading the file content
cat ./files/adequate_books/more_books/.secret/deeper_secrets/deepest_secrets/uber-secret.txt
```

Key Learning Points
- The find Command: A powerful utility for searching files. The syntax find [path] -name "[filename]" allows for rapid discovery of assets in massive file systems.

- Hidden Directories: Files or folders starting with a dot (.), such as .secret, are hidden by default in Linux but can be traversed and searched easily via CLI.

- Automation over Manual Labor: This challenge reinforces the importance of using terminal tools to automate discovery tasks in cybersecurity forensics.
