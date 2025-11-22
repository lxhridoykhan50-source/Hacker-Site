# 🛡️ Ethical Hacking Tools for Termux

এই রিপোজিটরিতে কিছু মৌলিক এথিক্যাল হ্যাকিং টুলস রয়েছে যা Python-এ লেখা এবং Termux-এ চালানোর জন্য অপ্টিমাইজ করা।

### ⚠️ সতর্কতা
শুধুমাত্র শিক্ষাগত উদ্দেশ্যে এবং নিজের সিস্টেমে বা অনুমোদিত পরিবেশে ব্যবহার করুন। অননুমোদিত ব্যবহার আইনত দণ্ডনীয়।

### 📲 Termux-এ সেটআপ
১. `pkg update && pkg upgrade`
২. `pkg install python git`
৩. `git clone https://github.com/YOUR_USERNAME/ethical-hacking-tools.git`
৪. `cd ethical-hacking-tools`
৫. `pip install -r requirements.txt`

### 🚀 ব্যবহারবিধি
- **পোর্ট স্ক্যানার:** `python port_scanner.py -t <IP> -p <port_range>`
- **ডিরেক্টরি স্ক্যানার:** `python directory_scanner.py -u <URL> -w wordlists/directories.txt`
- **হ্যাশ ক্র্যাকার:** `python hash_cracker.py -H <hash> -a <md5/sha1> -w wordlists/passwords.txt`
