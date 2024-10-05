#!/usr/bin/python3

## Title: Steghide Password Cracking Script
## Author: fixploit03 
## Date: 2024-10-05

import subprocess           

file_path = input("Enter the Steghide file path: ")
wordlist_path = input("Enter the wordlist file path: ")

password_found = False

with open(wordlist_path, "r", encoding="latin-1", errors="ignore") as f:
    for line in f:
        password = line.strip()  
        command = f"steghide extract -sf {file_path} -p {password} -f"
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            print(f"Password found: {password}") 
            password_found = True 
            break
        else:
            print(f"Incorrcet password: {password}")
if not password_found:
    print("Password not found, try a different wordlist.")
