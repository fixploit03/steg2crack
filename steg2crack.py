#!/usr/bin/python3

## Program   : steg2crack
## Deskripsi : Program python3 sederhana yang dirancang untuk meng-crack file Stego.
## Pembuat   : fixploit03 
## Rilis     : 5-10-2024
## Github    : https://github.com/fixploit03/steg2crack/

import os
import subprocess           
import time
import shutil
from datetime import datetime

## Variabel warna
m = "\033[31m" # Merah
h = "\033[32m" # Hijau 
k = "\033[33m" # Kuning 
b = "\033[34m" # Biru
c = "\033[36m" # Cyan
p = "\033[37m" # Putih 
r = "\033[0m"  # Reset 

print(f"""
{c}      _             ____                     _    
{c}  ___| |_ ___  __ _|___ \ ___ _ __ __ _  ___| | __
{c} / __| __/ _ \/ _` | __) / __| '__/ _` |/ __| |/ /
{c} \__ \ ||  __/ (_| |/ __/ (__| | | (_| | (__|   < 
{c} |___/\__\___|\__, |_____\___|_|  \__,_|\___|_|\_|
{c}              |___/                               
{p}[{b}*{p}] Program   : {b}steg2crack
{p}[{b}*{p}] Deskripsi : {b}Program python3 untuk meng-crack file Stego
{p}[{b}*{p}] Pembuat   : {b}fixploit03 
{p}[{b}*{p}] Github    : {b}https://github.com/fixploit03/steg2crack/
{p}[{b}*{p}] Team      : {b}ArSec (Arjuna Security)
{r}""")

while True:
    try:
        file_stego = input(f"{p}[{b}#{p}] Masukkan nama file Stego: ")
        if not file_stego:
            print(f"{p}[{m}-{p}] File Stego tidak boleh kosong.{r}")
            continue 
        if not os.path.isfile(file_stego):
            print(f"{p}[{m}-{p}] File Stego '{file_stego}' tidak ditemukan.{r}")
            continue
        break
    except KeyboardInterrupt:
        print(f"\n{p}[{m}-{p}] Program dihentikan oleh pengguna.{r}")
        exit(1)

while True:
    try:
        file_wordlist = input(f"{p}[{b}#{p}] Masukkan nama file Wordlist: ")
        if not file_wordlist:
            print(f"{p}[{m}-{p}] File Wordlist tidak boleh kosong.{r}")
            continue 
        if not os.path.isfile(file_wordlist):
            print(f"{p}[{m}-{p}] File Wordlist '{file_wordlist}' tidak ditemukan.{r}")
            continue
        break
    except KeyboardInterrupt:
        print(f"\n{p}[{m}-{p}] Program dihentikan oleh pengguna.{r}")
        exit(1)

while True:
    try:
        folder = input(f"{p}[{b}#{p}] Masukkan nama folder untuk menyimpan hasil file yang berhasil di-crack: ")
        if not folder:
            print(f"{p}[{m}-{p}] Folder tidak boleh kosong.{r}")
            continue
        if not os.path.isdir(folder):
            print(f"{p}[{m}-{p}] Folder '{folder}' tidak ditemukan.{r}")
            continue
        break
    except KeyboardInterrupt:
        print(f"\n{p}[{m}-{p}] Program dihentikan oleh pengguna.{r}")
        exit(1)
            
print("")

kata_sandi_ditemukan = False


with open(file_wordlist, "r", encoding="latin-1", errors="ignore") as fw:
    daftar_kata_sandi = fw.read().splitlines()
    jumlah_kata_sandi = len(daftar_kata_sandi)
    waktu_mulai = datetime.now()
    print(f"{p}[{h}+{p}] Jumlah kata sandi yang terdapat dalam file Wordlist: {h}{jumlah_kata_sandi}{r}")
    input(f"\n{p}Tekan [{h}Enter{p}] untuk memulai proses cracking...{r}")
    print(f"\n{p}[{b}*{p}] Dimulai pada : {b}{waktu_mulai.strftime('%d-%m-%Y %H:%M:%S')}{r}\n")
    time.sleep(3)
    for kata_sandi in daftar_kata_sandi:
        file_txt = f"{file_stego}.out"
        perintah = f"steghide extract -sf {file_stego} -p {kata_sandi} -xf {file_txt}"
        try:
            hasil = subprocess.run(perintah, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if hasil.returncode == 0:
                waktu_akhir = datetime.now()
                print(f"{p}[{h}+{p}] Kata sandi ditemukan: {h}{kata_sandi}{r}") 
                print(f"\n{p}[{b}*{p}] Berakhir pada : {b}{waktu_akhir.strftime('%d-%m-%Y %H:%M:%S')}{r}")
                shutil.move(file_stego, folder)
                kata_sandi_ditemukan = True 
                break
            else:
                print(f"{p}[{m}-{p}] Kata sandi salah: {m}{kata_sandi}{r}")
        except KeyboardInterrupt:
            print(f"\n{p}[{m}-{p}] Program dihentikan oleh pengguna.{r}")
            exit(1)
            
    if not kata_sandi_ditemukan:
        waktu_akhir = datetime.now()
        print(f"{p}[{m}-{p}] Kata sandi tidak ditemukan, coba file Wordlist yang lain.{r}")
        print(f"\n{p}[{b}*{p}] Berakhir pada : {b}{waktu_akhir.strftime('%d-%m-%Y %H:%M:%S')}{r}")
