#!/usr/bin/python3

## Program   : steg2crack
## Deskripsi : Program python3 sederhana yang dirancang untuk meng-crack file Stego.
## Pembuat   : fixploit03 
## Rilis     : 5-10-2024
## Github    : https://github.com/fixploit03/steg2crack/

# MIT License
# 
# Copyright (c) 2024 fixploit03 
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import subprocess           
import time
import platform
from datetime import datetime 

## Variabel warna
m = "\033[31m" # Merah
h = "\033[32m" # Hijau 
k = "\033[33m" # Kuning 
b = "\033[34m" # Biru
c = "\033[36m" # Cyan
p = "\033[37m" # Putih 
r = "\033[0m"  # Reset 

# Cek sistem operasi 
sistem_operasi = platform.system()
# Android (Termux) & Linux
if sistem_operasi == "Linux":
    os.system("clear")
# Windows
elif sistem_operasi == "Windows":
    os.system("cls")
    
print(f"""
{p}                         ,
{p}  ,-.       _,---._ __  / l
{p} /  )    .-'       `./ /   l
{p}(  (   ,'            `/    /|
{p} \  `-"             .'\   / |
{p}  `.              ,  \ \ /  |
{p}   /`.          ,'-`----Y   |
{p}  (            ;        |   '
{p}  |  ,-.    ,-'         |  /
{p}  |  | (   |        {c}Cat {p}| /
{p}  )  |  \  `.___________|/
{p}  `--'   `--'
{r}
[{b}*{p}] Mengecek steghide...{r}""")
time.sleep(3)

# Cek steghide 
cek_steghide = f"steghide --version"
hasil_cek_steghide = subprocess.run(cek_steghide, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

if hasil_cek_steghide.returncode == 0:
    print(f"{p}[{h}+{p}] steghide sudah terinstal.{r}")
    input(f"\n{p}Tekan [{h}Enter{p}] untuk memulai proses melanjutkan...{r}")
    os.system("clear")
else:
    print(f"{p}[{m}-{p}] steghide belum terinstal.{r}")
    exit(1)

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
        file_stego = input(f"{p}[{b}#{p}] Masukkan nama file Stego : ")
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
        file_wordlist = input(f"{p}[{b}#{p}] Masukkan nama file Wordlist : ")
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

print("")

kata_sandi_ditemukan = False

with open(file_wordlist, "r", encoding="latin-1", errors="ignore") as fw:
    daftar_kata_sandi = fw.read().splitlines()
    jumlah_kata_sandi = len(daftar_kata_sandi)
    waktu_mulai = datetime.now()
    print(f"{p}[{h}+{p}] Jumlah kata sandi yang terdapat dalam file Wordlist : {h}{jumlah_kata_sandi}{r}")
    input(f"\n{p}Tekan [{h}Enter{p}] untuk memulai proses cracking...{r}")
    print(f"\n{p}[{b}*{p}] Dimulai pada : {b}{waktu_mulai.strftime('%d-%m-%Y %H:%M:%S')}{r}\n")
    time.sleep(3)
    for kata_sandi in daftar_kata_sandi:
        perintah_crack = f"steghide extract -sf {file_stego} -p {kata_sandi} -f"
        try:
            hasil_crack = subprocess.run(perintah_crack, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if hasil_crack.returncode == 0:
                perintah_cari_info_file = f"steghide info -p {kata_sandi} {file_stego}"
                hasil_cari_info_file = subprocess.run(perintah_cari_info_file, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                file_terbunyi = re.search(r'embedded file "([^"]+)"', hasil_cari_info_file.stdout)
                print(file_terbunyi)
                waktu_akhir = datetime.now()
                print(f"{p}[{h}+{p}] Kata sandi ditemukan : {h}{kata_sandi}{r}") 
                print(f"\n{p}[{b}*{p}] Berakhir pada : {b}{waktu_akhir.strftime('%d-%m-%Y %H:%M:%S')}{r}")
                kata_sandi_ditemukan = True 
                break
            else:
                print(f"{p}[{m}-{p}] Kata sandi salah : {m}{kata_sandi}{r}")
        except KeyboardInterrupt:
            print(f"\n{p}[{m}-{p}] Program dihentikan oleh pengguna.{r}")
            exit(1)
            
    if not kata_sandi_ditemukan:
        waktu_akhir = datetime.now()
        print(f"{p}[{m}-{p}] Kata sandi tidak ditemukan, coba file Wordlist yang lain.{r}")
        print(f"\n{p}[{b}*{p}] Berakhir pada : {b}{waktu_akhir.strftime('%d-%m-%Y %H:%M:%S')}{r}")
