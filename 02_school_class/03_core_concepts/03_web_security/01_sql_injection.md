# SQL Injection (SQLi) Deep Dive

## 1. What is SQL Injection?
**SQL Injection (SQLi)** is a web security vulnerability that allows an attacker to interfere with the queries that an application makes to its database. It typically occurs when an attacker inputs malicious SQL code into an input field, which is then executed by the server.

---

## 2. How it Works
When an application uses unvalidated user input directly in a SQL query, an attacker can change the query's logic.

**Example (Vulnerable Code):**
`SELECT * FROM users WHERE username = 'admin' AND password = '`**`' OR '1'='1`**`';`

In this case, because `'1'='1'` is always true, the attacker can log in without a valid password.

---

## 3. Types of SQL Injection

### ① In-band SQLi (Classic)
The attacker uses the same communication channel to launch the attack and gather results.
* **Error-based:** Forcing the database to produce error messages that reveal structural information.
* **Union-based:** Using the `UNION` operator to combine results from multiple tables and exfiltrate data.

### ② Inferential SQLi (Blind SQLi)
The server doesn't return data directly. The attacker observes the server's response patterns to reconstruct the database structure.
* **Boolean-based:** Checking if the page content changes based on a TRUE/FALSE query result.
* **Time-based:** Making the database wait for a specified duration if a condition is true to confirm data existence.

### ③ Out-of-band SQLi
Used when the attacker cannot use the same channel to launch the attack and gather results, relying on the database's ability to make external HTTP or DNS requests.

---

## 4. Impact of SQL Injection
* **Data Theft:** Stealing sensitive data like passwords, credit card numbers, or personal info.
* **Data Manipulation:** Modifying or deleting database records without authorization.
* **Authentication Bypass:** Gaining access as administrative users without credentials.
* **Remote Code Execution:** In some cases, gaining full control over the underlying database server.

---

## 5. How to Prevent SQL Injection

### ✅ Prepared Statements (Parameterized Queries)
This is the most effective defense. Instead of building a query string with user input, parameters are sent separately so the database treats them as data, not code.

### ✅ Input Validation & Sanitization
Never trust user input. Use allow-lists to permit only expected characters or formats (e.g., numeric-only for ID fields).

### ✅ Principle of Least Privilege (PoLP)
The database account used by the web application should only have the minimum permissions it absolutely needs.

### ✅ Use of ORM/Frameworks
Modern frameworks (like Django, Hibernate, or Entity Framework) often have built-in protection against SQLi.

---

## Summary
SQL Injection is a critical vulnerability where malicious SQL queries are executed. To protect your application, **always use Prepared Statements** and strictly validate all user-supplied data.
