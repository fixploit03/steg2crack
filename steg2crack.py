#!/usr/bin/python3

## Program   : steg2crack
## Deskripsi : Program python3 sederhana yang dirancang untuk meng-crack file Stego.
## Pembuat   : fixploit03 
## Rilis     : 5-10-2024
## Github    : https://github.com/fixploit03/steg2crack/

import os
import subprocess           
import time
from datetime import datetime

## Variabel warna
m = "\033[31m" # Merah
h = "\033[32m" # Hijau 
k = "\033[33m" # Kuning 
b = "\033[34m" # Biru
c = "\033[36m" # Cyan
p = "\033[37m" # Putih 
r = "\033[0m"  # Reset 

print("""
     _                                 _
 ___| |_ ___  __ _  ___ _ __ __ _  ___| | _____ _ __
/ __| __/ _ \/ _` |/ __| '__/ _` |/ __| |/ / _ \ '__|
\__ \ ||  __/ (_| | (__| | | (_| | (__|   <  __/ |
|___/\__\___|\__, |\___|_|  \__,_|\___|_|\_\___|_|
             |___/ 
             
      https://github.com/fixploit03/steg2crack/""")

file_stego = input(f"{p}[{b}#{p}] Masukkan nama file Stego: ")

if not os.path.isfile(file_stego):
    print(f"{p}[{m}-{p}] File Stego '{file_stego}' tidak ditemukan.{r}")
    exit(1)
    
file_wordlist = input(f"{p}[{b}#{p}] Masukkan nama file Wordlist: ")

if not os.path.isfile(file_wordlist):
    print(f"{p}[{m}-{p}] File Wordlist '{file_wordlist}' tidak ditemukan.{r}")
    exit(1)

print("")

kata_sandi_ditemukan = False

with open(file_wordlist, "r", encoding="latin-1", errors="ignore") as fw:
    daftar_kata_sandi = fw.read().splitlines()
    jumlah_kata_sandi = len(daftar_kata_sandi)
    waktu_mulai = datetime.now()
    print(f"{p}[{b}*{p}] Jumlah kata sandi yang terdapat dalam file Wordlist: {b}{jumlah_kata_sandi}{r}")
    input(f"\n{p}Tekan [{h}Enter{p}] untuk memulai proses cracking...{r}")
    print(f"\n{p}[{b}*{p}] Dimulai pada : {b}{waktu_mulai.strftime('%d-%m-%Y %H:%M:%S')}{r}\n")
    time.sleep(3)
    for kata_sandi in daftar_kata_sandi:
        perintah = f"steghide extract -sf {file_stego} -p {kata_sandi} -f"
        hasil = subprocess.run(perintah, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if hasil.returncode == 0:
            waktu_akhir = datetime.now()
            print(f"{p}[{h}+{p}] Kata sandi ditemukan: {h}{kata_sandi}{r}") 
            print(f"\n{p}[{b}*{p}] Berakhir pada : {b}{waktu_akhir.strftime('%d-%m-%Y %H:%M:%S')}{r}")
            kata_sandi_ditemukan = True 
            break
        else:
            print(f"{p}[{m}-{p}] Kata sandi salah: {m}{kata_sandi}{r}")
if not kata_sandi_ditemukan:
    waktu_akhir = datetime.now()
    print(f"{p}[{m}-{p}] Kata sandi tidak ditemukan, coba file Wordlist yang lain.{r}")
    print(f"\n{p}[{b}*{p}] Berakhir pada : {b}{waktu_akhir.strftime('%d-%m-%Y %H:%M:%S')}{r}")
