![Python Version](https://img.shields.io/badge/python-3.x-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Repo Size](https://img.shields.io/github/repo-size/fixploit03/steg2crack)
![Issues](https://img.shields.io/github/issues/fixploit03/steg2crack)
![Forks](https://img.shields.io/github/forks/fixploit03/steg2crack)
![Stars](https://img.shields.io/github/stars/fixploit03/steg2crack)

# steg2crack :closed_lock_with_key:

`steg2crack` adalah program Python sederhana yang dirancang untuk meng-crack file [Stegano](https://www.kajianpustaka.com/2017/09/sejarah-prinsip-kerja-teknik-steganografi.html?m=1) dengan teknik [Dictionary Attack](https://www.asdf.id/definisi-dictionary-attack-adalah/).

## Demonstrasi :movie_camera:

[Lihat video demonstrasi di YouTube](https://www.youtube.com/watch?v=Qd4P68u0UFQ)

## Instalasi :gear:

### Termux :iphone:

```
# Memperbaharui repositori Termux 
$ pkg update

# Menginstal python3 
$ pkg install python3

# Menginstal steghide 
$ pkg install steghide

# Menginstal git
$ pkg install git

# Mengkloning repositori steg2crack dari GitHub
$ git clone https://github.com/fixploit03/steg2crack/
```

### Linux (Debian/Ubuntu) :computer:

```
# Memperbaharui repositori Linux 
$ sudo apt-get update

# Menginstal python3 
$ sudo apt-get install python3

# Menginstal steghide 
$ sudo apt-get install steghide

# Menginstal git
$ sudo apt-get install git

# Mengkloning repositori steg2crack dari GitHub
$ git clone https://github.com/fixploit03/steg2crack/
```

## Menjalankan Program 👨🏾‍💻

```
python3 steg2crack.py
```

## Lisensi :scroll:

Program ini dilisensikan di bawah [MIT License](https://github.com/fixploit03/steg2crack/blob/main/LICENSE).

## Penulis :pen:

[fixploit03](https://github.com/fixploit03)

> :clipboard: **Catatan**: Program ini hanya mendukung file Stegano yang dihasilkan oleh alat Steghide, sehingga mungkin tidak berfungsi dengan file Stegano yang dihasilkan oleh alat lain.
