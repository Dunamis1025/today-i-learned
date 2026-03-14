# SQL Injection (SQLi) Deep Dive

## 1. Executive Summary
**SQL Injection (SQLi)** is a critical web security vulnerability that allows an attacker to interfere with the queries that an application makes to its database. By injecting malicious SQL code into input fields, attackers can bypass authentication, access sensitive data, and in some scenarios, gain administrative control over the database server.



---

## 2. Technical Attack Mechanism
The vulnerability occurs when user-supplied data (from forms, cookies, or HTTP headers) is concatenated directly into a database query string without proper sanitization or parameterization.

### The "Logic Hijacking" Example
Consider a standard login query:
```sql
SELECT * FROM accounts WHERE user = '$username' AND pass = '$password';
If an attacker inputs admin as the username and ' OR '1'='1 as the password, the resulting query becomes:SQLSELECT * FROM accounts WHERE user = 'admin' AND pass = '' OR '1'='1';
Since '1'='1' is a tautology (always true), the WHERE clause evaluates to true regardless of the password, granting unauthorized access.3. Comprehensive Taxonomy of SQLiA. In-band SQLi (Classic)The attacker uses the same communication channel to both launch the attack and gather results.Union-Based: Leverages the UNION SQL operator to combine the results of the original query with a new query injected by the attacker. This allows for the extraction of data from any table in the database.Error-Based: The attacker intentionally triggers database errors to gain information about the database structure (e.g., table names, column types) from the error messages returned to the client.B. Inferential SQLi (Blind SQLi)No data is transferred via the web application directly. Instead, the attacker reconstructs the database structure by sending payloads and observing the server's response patterns.Boolean-Based: The attacker sends a query that asks the database a true/false question. Based on whether the page content changes or remains the same, the attacker can deduce data bit by bit.Time-Based: The attacker injects a command that tells the database to wait (e.g., SLEEP(10)) before responding if a condition is true. If the response is delayed, the attacker confirms the condition.C. Out-of-band SQLiUsed when the server is hardened against standard responses, but the database can make external network requests (like DNS or HTTP). The attacker triggers the database to send data to a server they control.4. Mitigation and Defense-in-Depth✅ Primary Defense: Prepared Statements (Parameterized Queries)This is the most effective defense. The application defines the SQL code first, then passes user inputs as parameters. The database treats these strictly as data, never as executable code.Example (Java/JDBC):JavaString customerName = request.getParameter("customerName");
// The '?' acts as a placeholder that cannot be escaped
PreparedStatement pstmt = connection.prepareStatement("SELECT * FROM users WHERE name = ?");
pstmt.setString(1, customerName); 
ResultSet results = pstmt.executeQuery();
✅ Secondary Defense: Input Validation (Allow-listing)Implement strict validation for all user input. Use "Allow-lists" to define exactly what is permitted (e.g., a zip code should only accept 5 digits) rather than "Block-lists" which try to guess what is malicious.✅ Database Security: Principle of Least Privilege (PoLP)The web application’s database account should only have the minimum permissions required. For example, an application that only reads data should not have DROP TABLE or GRANT permissions.✅ Use of WAF (Web Application Firewall)A WAF can help detect and block known SQLi patterns in incoming traffic as an additional perimeter layer.5. Summary ComparisonFeatureIn-band SQLiBlind SQLiOut-of-band SQLiSpeedFastSlow (Iterative)ModerateVisibilityHigh (Direct results)Low (Inferred)None (External)ComplexityLowHighHighThis document is part of a personal cybersecurity study series. Last updated: March 2026.
