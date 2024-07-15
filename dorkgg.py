import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style, init
import os
import time
from tqdm import tqdm
import re

# Inisialisasi colorama
init(autoreset=True)

# Fungsi untuk membersihkan nama file
def clean_filename(filename):
    return re.sub(r'[\/:*?"<>|]', '_', filename)

# Fungsi untuk melakukan pencarian Google Dork
def google_dork_search(query):
    url = f"https://www.google.com/search?q={query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    return response.text

# Fungsi untuk memparsing hasil pencarian Google
def parse_search_results(html):
    soup = BeautifulSoup(html, 'html.parser')
    results = []
    for g in soup.find_all(class_='g'):
        anchors = g.find_all('a')
        if anchors:
            link = anchors[0]['href']
            title = g.find('h3').text if g.find('h3') else 'No title'
            results.append((title, link))
    return results

def save_results_to_file(results, output_filename):
    with open(output_filename, 'w') as file:
        for title, link in results:
            file.write(f"{title}\n{link}\n\n")

if __name__ == "__main__":
    dork = input(f"{Fore.RED}{Style.BRIGHT}Masukkan Google Dork yang ingin digunakan: ")
    output_folder = "/storage/emulated/0/google_dorks"
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Bersihkan nama file sebelum digunakan
    output_filename = os.path.join(output_folder, f"{clean_filename(dork)}_results.txt")
    
    print(f"{Fore.RED}{Style.BRIGHT}Melakukan pencarian dengan dork: {dork}...")

    # Menampilkan progress bar
    print(f"{Fore.RED}{Style.BRIGHT}Mengirim permintaan ke Google...")
    for _ in tqdm(range(10), desc="Mengirim permintaan"):
        time.sleep(0.1)  # Simulasi waktu loading
    
    html = google_dork_search(dork)
    results = parse_search_results(html)
    
    save_results_to_file(results, output_filename)
    print(f"{Fore.RED}{Style.BRIGHT}Hasil pencarian tersimpan di {output_filename}")