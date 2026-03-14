# SQL Injection (SQL 인젝션)

## 1. What is SQL Injection? / SQL 인젝션이란?

**SQL Injection** is a web security vulnerability that allows an attacker to interfere with the queries that an application makes to its database. It typically occurs when an attacker inputs malicious SQL code into an input field, which is then executed by the server.

**SQL 인젝션**은 공격자가 애플리케이션의 데이터베이스 쿼리에 개입할 수 있게 허용하는 웹 보안 취약점입니다. 주로 공격자가 입력창에 악의적인 SQL 코드를 삽입하고, 이것이 서버 측 데이터베이스에서 실행될 때 발생합니다.

---

## 2. How it Works / 작동 원리

When an application uses unvalidated user input directly in a SQL query, an attacker can change the query's logic.

애플리케이션이 사용자 입력값을 검증 없이 SQL 쿼리에 직접 사용할 때, 공격자는 쿼리의 논리 구조를 변경할 수 있습니다.

**Example (Vulnerable Code):**
`SELECT * FROM users WHERE username = 'admin' AND password = '`**`' OR '1'='1`**`';`

In this case, because `'1'='1'` is always true, the attacker can log in without a valid password.
위 예시에서 `'1'='1'`은 항상 참이므로, 공격자는 유효한 비밀번호 없이도 로그인을 할 수 있게 됩니다.

---

## 3. Types of SQL Injection / SQL 인젝션의 종류

### ① In-band SQLi (Classic)
The attacker uses the same communication channel to launch the attack and gather results.
공격자가 공격과 결과 확인을 동일한 통신 채널을 통해 수행하는 가장 일반적인 방식입니다.
* **Error-based:** Forcing the database to produce error messages that reveal info. (에러 기반: DB 에러 메시지를 통해 정보 유출)
* **Union-based:** Using the `UNION` operator to combine results from multiple tables. (유니온 기반: UNION 연산자를 사용해 다른 테이블의 데이터를 탈취)

### ② Inferential SQLi (Blind SQLi)
The server doesn't return data directly. The attacker observes the server's response (True/False or Time delay) to reconstruct the database structure.
서버가 직접적인 데이터를 반환하지 않을 때, 서버의 응답(참/거짓 또는 응답 시간 차이)을 관찰하여 정보를 유추합니다.
* **Boolean-based:** Checking if the page content changes based on a TRUE/FALSE query. (불린 기반: 쿼리 결과에 따른 페이지 변화 확인)
* **Time-based:** Making the database wait for a few seconds if a condition is true. (시간 기반: 조건이 참일 때 응답을 지연시켜 확인)

### ③ Out-of-band SQLi
Used when the attacker cannot use the same channel to launch the attack and gather results, often relying on the database's ability to make HTTP or DNS requests.
공격 채널과 결과 획득 채널이 다를 때 사용하며, DB가 직접 HTTP나 DNS 요청을 보내도록 유도합니다.

---

## 4. Impact of SQL Injection / SQL 인젝션의 영향

* **Data Theft:** Stealing sensitive data like passwords, credit card numbers, or personal info. (데이터 탈취: 비밀번호, 카드 정보 등 유출)
* **Data Manipulation:** Modifying or deleting database records. (데이터 조작: DB 기록 수정 및 삭제)
* **Authentication Bypass:** Logging in as administrative users. (인증 우회: 관리자 계정으로 로그인)
* **Remote Code Execution:** In some cases, gaining full control over the database server. (원격 코드 실행: DB 서버 전체 제어권 획득)

---

## 5. How to Prevent SQL Injection / 방어 방법

### ✅ Prepared Statements (with Parameterized Queries)
This is the most effective defense. Instead of building a query string with user input, parameters are sent separately so the DB treats them as data, not code.
가장 효과적인 방어법입니다. 쿼리 문법과 데이터를 분리하여, 사용자 입력을 코드가 아닌 단순 데이터로 처리하게 합니다.

### ✅ Input Validation & Sanitization
Never trust user input. Use allow-lists to permit only expected characters or formats.
사용자 입력을 신뢰하지 마세요. 허용된 문자열이나 형식만 통과시키는 화이트리스트 방식을 권장합니다.

### ✅ Principle of Least Privilege
The database account used by the web application should only have the permissions it absolutely needs.
웹 애플리케이션용 DB 계정에는 반드시 필요한 최소한의 권한만 부여해야 합니다.

### ✅ Use of ORM/Frameworks
Modern frameworks (like Django, Hibernate, or Entity Framework) often have built-in protection against SQLi.
최신 프레임워크들은 기본적으로 SQL 인젝션을 방어하는 기능을 내장하고 있는 경우가 많습니다.

---

## Summary / 요약

SQL Injection is a critical vulnerability where malicious SQL queries are executed. To protect your application, **always use Prepared Statements** and strictly validate all user-supplied data.

SQL 인젝션은 악의적인 SQL 쿼리가 실행되는 위험한 취약점입니다. 이를 방어하기 위해 **반드시 Prepared Statements(준비된 실행문)를 사용**하고, 사용자 입력값을 엄격하게 검증해야 합니다.
