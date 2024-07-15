import requests
from colorama import Fore, Style, init
import os
import time
from tqdm import tqdm

# Inisialisasi colorama
init(autoreset=True)

# Fungsi untuk mendapatkan subdomain dari VirusTotal
def get_subdomains_virustotal(domain, api_key):
    url = f"https://www.virustotal.com/vtapi/v2/domain/report?apikey={api_key}&domain={domain}"
    response = requests.get(url)
    subdomains = []
    if response.status_code == 200:
        data = response.json()
        subdomains = data.get("subdomains", [])
    return subdomains

def save_subdomains_to_file(subdomains, output_filename):
    with open(output_filename, 'w') as file:
        for subdomain in subdomains:
            file.write(subdomain + "\n")

if __name__ == "__main__":
    domain = input(f"{Fore.RED}{Style.BRIGHT}Masukkan domain yang ingin dicari subdomainnya: ")
    vt_api_key = "61fd44424026c88e65685f70ebfa6395ce0498ee5b6f6a8c3fb26d812d75b404"
    output_folder = "/storage/emulated/0/subdomains"
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    output_filename = os.path.join(output_folder, f"{domain}_subdomains.txt")
    
    print(f"{Fore.RED}{Style.BRIGHT}Mencari subdomain untuk {domain}...")

    all_subdomains = set()
    
    # Menampilkan progress bar
    print(f"{Fore.RED}{Style.BRIGHT}Menggunakan SubFinder ZannMods...")
    for _ in tqdm(range(10), desc="ZannTools"):
        time.sleep(0.1)  # Simulasi waktu loading
    all_subdomains.update(get_subdomains_virustotal(domain, vt_api_key))
    
    save_subdomains_to_file(all_subdomains, output_filename)
    print(f"{Fore.RED}{Style.BRIGHT}Subdomain tersimpan di {output_filename}")