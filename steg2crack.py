#!/usr/bin/python3

## Title: Steghide Password Cracking Script
## Author: fixploit03 
## Date: 2024-10-05

# Import necessary modules
import sys                      # Provides access to command-line arguments
import subprocess               # Allows executing shell commands
import argparse                 # For parsing command-line arguments
import textwrap                 # For formatting text
from pwn import *               # Importing the pwn module for logging and progress tracking

# Set up argument parser for the script
parser = argparse.ArgumentParser(description="Steghide Password Cracking Script by fixploit03", 
                                 formatter_class=argparse.RawTextHelpFormatter,
                                 epilog=textwrap.dedent(''' 
Script Usage : 
python3 steg2crack.py -f secret.jpg -w wordlist.txt
'''))

# Define expected command-line arguments
parser.add_argument("-f", "--file", help="Steghide file")  # Path to the steghide file
parser.add_argument("-w", "--wordlist", help="Password Dictionary")  # Path to the wordlist file
args = parser.parse_args()  # Parse the command-line arguments

# Check if at least one argument is provided
if len(sys.argv) < 2:
    log.failure(f"Script Usage: python3 steg2crack.py -h [help] -f [file] -w [wordlist]")
    sys.exit(1)  # Exit if no arguments are given

# Assigning file paths from the parsed arguments
file_path = args.file
wordlist_path = args.wordlist

# Check if the Steghide file exists
if not os.path.isfile(file_path):
    log.failure(f"Steghide file not found: {file_path}")
    sys.exit(1)

# Check if the wordlist file exists
if not os.path.isfile(wordlist_path):
    log.failure(f"Wordlist file not found: {wordlist_path}")
    sys.exit(1)

# Initialize a variable to track if the password is found
password_found = False  

# Log the banner message for the script
banner = log.info("Steghide Password Cracking Script by fixploit03")
print()

# Initialize a progress tracker for password attempts
stats = log.progress("Hunting for Password")
print() 

# Try to open the wordlist file and iterate through each password
try:
    with open(wordlist_path, "r", encoding="latin-1", errors="ignore") as f:
        for line in f:
            password = line.strip()  # Remove any leading/trailing whitespace from the password
            # Construct the shell command to attempt password extraction with Steghide
            command = f"steghide extract -sf {file_path} -p {password} -f"
            stats.status(f"Trying with Password: {password}")  # Update progress status
            # Execute the command in the shell
            result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            # Check if the password was correct by examining the return code
            if result.returncode == 0:  # Return code 0 indicates success
                log.success("SUCCESS !!")
                log.success(f"Password found: {password}")  # Log the found password
                password_found = True  # Update the flag to indicate a successful password match
                break  # Exit the loop since the password was found

    # If no password was found after trying all options
    if not password_found:
        log.failure("Oops! Password not found, try a different wordlist.")
except Exception as e:
    # Handle any other exceptions that may occur
    log.failure(f"An error occurred: {e}")
    sys.exit(1)  # Exit the script with an error code
