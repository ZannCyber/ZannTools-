import requests
from colorama import Fore, Style, init
import os
import time
from tqdm import tqdm  # Menambahkan tqdm untuk progress bar

# Inisialisasi colorama
init(autoreset=True)

def save_html_source(url, output_filename):
    response = requests.get(url)
    response.raise_for_status()  # Memastikan tidak ada error dalam permintaan
    
    with open(output_filename, 'w', encoding='utf-8') as file:
        file.write(response.text)

def get_storage_folder():
    storage_folder = "/storage/emulated/0/html_sources"
    if not os.path.exists(storage_folder):
        os.makedirs(storage_folder)
    return storage_folder

if __name__ == "__main__":
    url = input(f"{Fore.RED}{Style.BRIGHT}Masukkan URL yang ingin diambil source HTML-nya: ")
    storage_folder = get_storage_folder()
    output_filename = os.path.join(storage_folder, 'source.html')  # Nama file untuk menyimpan source HTML
    
    # Menampilkan progress bar
    print(f"{Fore.RED}{Style.BRIGHT}Mengambil source HTML...")
    for _ in tqdm(range(100), desc="Proses By ZannMods"):
        time.sleep(0.02)  # Simulasi waktu loading
    
    save_html_source(url, output_filename)
    print(f"{Fore.RED}{Style.BRIGHT}Source HTML tersimpan di {output_filename}")