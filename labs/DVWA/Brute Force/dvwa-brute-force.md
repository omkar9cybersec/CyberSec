# DVWA Brute Force Attack — Lab Writeup

## Objective
Brute-force the DVWA login form using Burp Suite Intruder to recover valid credentials.

## Environment
- **Target:** DVWA (Damn Vulnerable Web Application)
- **Tool:** Burp Suite (Community/Pro)
- **Attack type:** Cluster Bomb (Intruder)

## Steps

1. **Capture request**
   - Enter test credentials (e.g. `A1` / `123`) on the DVWA login form.
   - Intercept the request in Burp Suite Proxy — it's a **GET request** with `username` and `password` as parameters.
   - Right-click → **Send to Intruder**.

2. **Set positions**
   - Go to **Intruder → Positions**.
   - Clear default markers.
   - Add markers around the `username` and `password` values.
   - Attack type: **Cluster Bomb** (tests every combination of two independent payload sets).

3. **Configure payloads**
   - **Payload Set 1 (username):** `admin`, `user`, `admin1`, `user1`, `AAA`
   - **Payload Set 2 (password):** `password`, `Squirt`, `1234`
   - Payloads added manually (alternative: load from a `.txt` wordlist).

4. **Run attack**
   - Payload count: 4 | Request count: 20 (5 usernames × 4 passwords).
   - Start attack and let Burp send all combinations.

5. **Analyze results**
   - Sort results by **Length** column.
   - One request (`admin` / `password`) returns a distinct length (**4736**) vs. all others being identical.
   - Anomalous length = successful login indicator.

6. **Verify**
   - Manually log in with `admin` / `password` → login succeeds.

## Key Takeaway
Response **length/status code differences** in Intruder results are the primary signal for identifying valid credentials during a brute-force attack.

## Notes
- DVWA has no rate-limiting/lockout, making this attack trivial — real targets often have CAPTCHAs, lockouts, or WAFs requiring throttling.
- Only perform brute-force attacks on systems you own or are explicitly authorized to test.

## Reference
- Video: [Brute Force Attack on DVWA | Bug Bounty Hunting & Ethical Hacking Tutorial](https://www.youtube.com/watch?v=zamSIcJonMg)
