import hashlib
import argparse

def crack_hash(hash_to_crack, wordlist_path, hash_algorithm):
    try:
        with open(wordlist_path, 'r', encoding='latin-1') as file:
            for line in file:
                password = line.strip()
                if hash_algorithm == 'md5':
                    hashed_password = hashlib.md5(password.encode()).hexdigest()
                elif hash_algorithm == 'sha1':
                    hashed_password = hashlib.sha1(password.encode()).hexdigest()
                else:
                    print("[-] Unsupported algorithm. Use 'md5' or 'sha1'.")
                    return
                if hashed_password == hash_to_crack:
                    print(f"[+] Password Found: {password}")
                    return
        print("[-] Password not found in wordlist.")
    except FileNotFoundError:
        print(f"[-] Wordlist not found at '{wordlist_path}'")

def main():
    parser = argparse.ArgumentParser(description="A simple hash cracker.")
    parser.add_argument("-H", "--hash", required=True, dest="hash_to_crack", help="Hash to crack")
    parser.add_argument("-a", "--algorithm", required=True, choices=['md5', 'sha1'], help="Hash algorithm")
    parser.add_argument("-w", "--wordlist", required=True, help="Path to wordlist")
    
    args = parser.parse_args()
    print(f"[*] Cracking hash...")
    crack_hash(args.hash_to_crack, args.wordlist, args.algorithm)

if __name__ == "__main__":
    main()
