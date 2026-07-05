#!/usr/bin/env python3
import hashlib
import sys

def crack_hash(hash_value, wordlist_file):
    """Crack hash using wordlist"""
    try:
        with open(wordlist_file, 'r', errors='ignore') as f:
            for password in f:
                password = password.strip()
                # Try MD5
                md5_hash = hashlib.md5(password.encode()).hexdigest()
                if md5_hash == hash_value:
                    return password, "MD5"
                
                # Try SHA1
                sha1_hash = hashlib.sha1(password.encode()).hexdigest()
                if sha1_hash == hash_value:
                    return password, "SHA1"
        
        return None, None
    except FileNotFoundError:
        print(f"[-] Wordlist file not found: {wordlist_file}")
        return None, None

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 hash-cracker.py <hash> <wordlist>")
        print("Example: python3 hash-cracker.py 5d41402abc4b2a76b9719d911017c592 /usr/share/wordlists/rockyou.txt")
        sys.exit(1)
    
    hash_value = sys.argv[1].lower()
    wordlist = sys.argv[2]
    
    print(f"[*] Cracking hash: {hash_value}")
    print(f"[*] Using wordlist: {wordlist}\n")
    
    password, hash_type = crack_hash(hash_value, wordlist)
    
    if password:
        print(f"[+] PASSWORD FOUND: {password}")
        print(f"[+] Hash Type: {hash_type}")
    else:
        print(f"[-] Password not found in wordlist")

if __name__ == "__main__":
    main()
