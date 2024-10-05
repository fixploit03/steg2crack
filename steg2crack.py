#!/usr/bin/python3

## Title: Steghide Password Cracking Script
## Author: fixploit03 
## Date: 2024-10-05

import os
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
    print(f"{p}[{b}*{p}] Jumlah kata sandi yang terdapat dalam file Wordlist: {b}{jumlah_kata_sandi}{r}")
    input(f"\n{p}Tekan [{h}Enter{p}] untuk memulai proses cracking...{r}")
    for kata_sandi in daftar_kata_sandi:
        perintah = f"steghide extract -sf {file_stego} -p {kata_sandi} -f"
        hasil = subprocess.run(perintah, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if hasil.returncode == 0:
            print(f"{p}[{h}+{p}] Kata sandi ditemukan: {h}{kata_sandi}{r}") 
            kata_sandi_ditemukan = True 
            break
        else:
            print(f"{p}[{m}-{p}] Kata sandi salah: {m}{kata_sandi}{r}")
if not kata_sandi_ditemukan:
    print(f"{p}[{m}-{p}] Kata sandi tidak ditemukan, coba file Wordlist yang lain.{r}")
