import requests
import argparse
from urllib.parse import urljoin

def find_directories(base_url, wordlist_path):
    try:
        with open(wordlist_path, 'r') as file:
            for line in file:
                word = line.strip()
                if not word: continue
                url = urljoin(base_url, word)
                try:
                    response = requests.get(url, timeout=3, allow_redirects=False)
                    status = response.status_code
                    if status == 200 or status == 403 or status == 301:
                        print(f"[+] Found: {url} (Status: {status})")
                except requests.exceptions.RequestException:
                    pass
    except FileNotFoundError:
        print(f"[-] Wordlist not found at '{wordlist_path}'")

def main():
    parser = argparse.ArgumentParser(description="A simple directory brute-forcer.")
    parser.add_argument("-u", "--url", required=True, help="Target URL")
    parser.add_argument("-w", "--wordlist", required=True, help="Path to wordlist")
    
    args = parser.parse_args()
    target_url = args.url
    if not target_url.startswith(('http://', 'https://')):
        target_url = 'http://' + target_url
        
    print(f"[*] Scanning {target_url}...")
    find_directories(target_url, args.wordlist)
    print("[*] Scan complete.")

if __name__ == "__main__":
    main()
