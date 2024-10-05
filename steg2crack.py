#!/usr/bin/python3

## Title: Steghide Password Cracking Script
## Author: fixploit03 
## Date: 2024-10-05

import subprocess           

## Variabel warna
m = "\033[31m" # Merah
h = "\033[32m" # Hijau 
k = "\033[33m" # Kuning 
b = "\033[34m" # Biru
c = "\033[36m" # Cyan
p = "\033[37m" # Putih 
r = "\033[0m"  # Biru

print("""
-----------------------------------------------
Steghide Password Cracking Script by fixploit03
(https://github.com/fixploit03/steg2crack/)
-----------------------------------------------
""")

file_path = input(f"{p}[{b}#{p}] Enter the Steghide file path: ")
wordlist_path = input(f"{p}[{b}#{p}] Enter the wordlist file path: ")

print("")

password_found = False

with open(wordlist_path, "r", encoding="latin-1", errors="ignore") as f:
    for line in f:
        password = line.strip()  
        command = f"steghide extract -sf {file_path} -p {password} -f"
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            print(f"{p}[{h}+{p}] Password found: {h}{password}{r}") 
            password_found = True 
            break
        else:
            print(f"{p}[{m}-{p}] Incorrcet password: {m}{password}{r}")
if not password_found:
    print(f"{p}[{m}-{p}] Password not found, try a different wordlist.{r}")
