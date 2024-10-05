#!/usr/bin/python3

## Title: Steghide Password Cracking Script
## Author: fixploit03 
## Date: 2024-10-05

import sys
import subprocess
import argparse
import textwrap
from pwn import *

# Expected Arguments
parser = argparse.ArgumentParser(description="Steghide Password Cracking Script by fixploit03", 
                                 formatter_class=argparse.RawTextHelpFormatter,
                                 epilog=textwrap.dedent(''' 
Script Usage : 
python3 steg2crack.py -f secret.jpg -w wordlist.txt
'''))

parser.add_argument("-f", "--file", help="Steghide file") 
parser.add_argument("-w", "--wordlist", help="Password Dictionary") 
args = parser.parse_args()

if len(sys.argv) < 2:
    log.failure(f"Script Usage: python3 steg2crack.py -h [help] -f [file] -w [wordlist]")
    sys.exit(1)

file_path = args.file
wordlist_path = args.wordlist

password_found = False  # Variable to track if the password is found

banner = log.info("Steghide Password Cracking Script by fixploit03")
print()
stats = log.progress("Hunting for Password")
print() 

try:
    with open(wordlist_path, 'r') as f:
        for line in f:
            password = line.strip()
            # Execute the Steghide command to try the password
            command = f"steghide extract -sf {file_path} -p {password} -f"
            stats.status(f"Trying with Password: {password}")
            result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            # Check if the password is correct by examining the returncode
            if result.returncode == 0:  # 0 means success
                log.success("SUCCESS !!")
                log.success(f"Password found: {password}")
                password_found = True
                break

    if not password_found:
        log.failure("Oops! Password not found, try a different wordlist.")
except FileNotFoundError:
    log.failure(f"File not found: {wordlist_path}")
    sys.exit(1)
except Exception as e:
    log.failure(f"An error occurred: {e}")
    sys.exit(1)
