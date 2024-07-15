import base64
from colorama import Fore, Style, init
import os
import time
from tqdm import tqdm  # Menambahkan tqdm untuk progress bar

# Inisialisasi colorama
init(autoreset=True)

def decode_base64_to_file(input_filename, output_filename):
    with open(input_filename, 'r') as file:
        base64_encoded = file.read()
        file_content = base64.b64decode(base64_encoded)
    
    with open(output_filename, 'wb') as output_file:
        output_file.write(file_content)

def get_storage_folder():
    storage_folder = "/storage/emulated/0/decoded_ZannMods"
    if not os.path.exists(storage_folder):
        os.makedirs(storage_folder)
    return storage_folder

if __name__ == "__main__":
    input_filename = input(f"{Fore.RED}{Style.BRIGHT}Masukkan nama file yang mau di-decode (contoh: enccode_tools-zann.txt): ")
    storage_folder = get_storage_folder()
    output_filename = os.path.join(storage_folder, 'decoded_file')  # Nama file untuk menyimpan hasil decoding
    
    # Menampilkan progress bar
    print(f"{Fore.RED}{Style.BRIGHT}Decoding file...")
    for _ in tqdm(range(100), desc="Proses decoding"):
        time.sleep(0.02)  # Simulasi waktu loading
    
    decode_base64_to_file(input_filename, output_filename)
    print(f"{Fore.RED}{Style.BRIGHT}Hasil decoding tersimpan di {output_filename}")