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

print(f"""
{p}***********************************************************
{p}* {c}Program     {p}: {c}steg2crack                                {p}*
{p}* {c}description {p}: {c}Steghide Password Cracking Script         {p}*
{p}* {c}Author      {p}: {c}fixploit03                                {p}*
{p}* {c}Github      {p}: {c}https://github.com/fixploit03/steg2crack/ {p}*
{p}***********************************************************
{r}""")

stego_file_path = input(f"{p}[{b}#{p}] Enter the Stego file path: ")
wordlist_file_path = input(f"{p}[{b}#{p}] Enter the Wordlist file path: ")

print("")

password_found = False

with open(wordlist_file_path, "r", encoding="latin-1", errors="ignore") as wf:
    password_list = wf.read().splitlines()
    for password in password_list:
        command = f"steghide extract -sf {stego_file_path} -p {password} -f"
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            print(f"{p}[{h}+{p}] Password found: {h}{password}{r}") 
            password_found = True 
            break
        else:
            print(f"{p}[{m}-{p}] Incorrcet password: {m}{password}{r}")
if not password_found:
    print(f"{p}[{m}-{p}] Password not found, try a different wordlist.{r}")
