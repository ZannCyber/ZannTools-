import base64
from colorama import Fore, Style, init
import os
import time
from tqdm import tqdm  # Menambahkan tqdm untuk progress bar

# Inisialisasi colorama
init(autoreset=True)

def encode_file_to_base64(input_filename, output_filename):
    with open(input_filename, 'rb') as file:
        file_content = file.read()
        base64_encoded = base64.b64encode(file_content).decode('utf-8')
    
    with open(output_filename, 'w') as output_file:
        output_file.write(base64_encoded)

def get_storage_folder():
    storage_folder = "/storage/emulated/0/encoded_files"
    if not os.path.exists(storage_folder):
        os.makedirs(storage_folder)
    return storage_folder

if __name__ == "__main__":
    input_filename = input(f"{Fore.RED}{Style.BRIGHT}Masukkan nama file yang mau di-encode (contoh: private.html): ")
    storage_folder = get_storage_folder()
    output_filename = os.path.join(storage_folder, 'enccode_tools-zann.txt')  # Nama file untuk menyimpan hasil Base64
    
    # Menampilkan progress bar
    print(f"{Fore.RED}{Style.BRIGHT}Encoding file...")
    for _ in tqdm(range(100), desc="Proses encoding"):
        time.sleep(0.02)  # Simulasi waktu loading
    
    encode_file_to_base64(input_filename, output_filename)
    print(f"{Fore.RED}{Style.BRIGHT}Hasil encoding tersimpan di {output_filename}")