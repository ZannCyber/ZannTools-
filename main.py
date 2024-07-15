from colorama import Fore, Style, init
import os

# Inisialisasi colorama
init(autoreset=True)

# Fungsi untuk menampilkan logo
def display_logo():
    logo = """
    ██████╗  █████╗ ████████╗ █████╗ ███████╗███████╗
    ██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔════╝██╔════╝
    ██████╔╝███████║   ██║   ███████║███████╗█████╗  
    ██╔══██╗██╔══██║   ██║   ██╔══██║╚════██║██╔══╝  
    ██║  ██║██║  ██║   ██║   ██║  ██║███████║███████╗
    ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝
    """
    print(f"{Fore.GREEN}{Style.BRIGHT}{logo}")

# Fungsi untuk meminta username dan password
def get_credentials():
    username = input(f"{Fore.RED}{Style.BRIGHT}Masukkan username: ")
    password = input(f"{Fore.RED}{Style.BRIGHT}Masukkan password: ")
    return username, password
# Fungsi untuk menampilkan pesan dengan efek delay
def print_with_typing_delay(message):
    for char in message:
        print(char, end='', flush=True)
        time.sleep(0.05)  # Ubah nilai delay sesuai keinginan
    print()  # Untuk newline setelah selesai mengetik

# Fungsi untuk menampilkan pesan setelah verifikasi
def display_verification_message():
    message = (f"{Fore.GREEN}{Style.BRIGHT}ANDA TERVERIFIKASI OLEH ZannTools!\n")
    print_with_typing_delay(message)


# Fungsi untuk menampilkan menu
def display_menu():
    print("\n=========== ZannTools ==========")
    print(f"{Fore.RED}{Style.BRIGHT}1. ENC CODE BASE64")
    print(f"{Fore.RED}{Style.BRIGHT}2. DECODE BASE64")
    print(f"{Fore.RED}{Style.BRIGHT}3. GET SOURCE")
    print(f"{Fore.RED}{Style.BRIGHT}4. BRUTE FORCE")
    print(f"{Fore.RED}{Style.BRIGHT}5. SubFinder")
    print(f"{Fore.RED}{Style.BRIGHT}6. Dork Google")
    print(f"{Fore.RED}{Style.BRIGHT}7. Sql Brute")
    print(f"{Fore.RED}{Style.BRIGHT}8. Keluar")
    print(f"=================================")

# Fungsi untuk memeriksa username dan password
def check_credentials(username, password):
    return username == "zannmods" and password == "zannmods"

# Fungsi untuk menjalankan script berdasarkan pilihan
def run_script(choice):
    script_files = {
        '1': 'enc.py',
        '2': 'decode1.py',
        '3': 'getweb1.py',
        '4': 'brute.py',
        '5': 'subfinder.py',
        '6': 'dorkgg.py',
        '7': 'sqlbrute.py',
    }

    if choice in script_files:
        script_file = script_files[choice]
        if os.path.exists(script_file):
            print(f"Menjalankan {script_file}...")
            os.system(f"python {script_file}")
        else:
            print(f"File {script_file} tidak ditemukan.")
    elif choice == '8':
        print(f"{Fore.RED}{Style.BRIGHT}Keluar Tools ZannMods.........")
        exit()
    else:
        print("Pilihan tidak valid. Silakan pilih lagi.")

def main():
    display_logo()
    username, password = get_credentials()

    if check_credentials(username, password):
        print(f"{Fore.GREEN}{Style.BRIGHT}ANDA TERVERIFIKASI OLEH ZannTools!\n")
        while True:
            display_menu()
            choice = input("Masukkan pilihan Anda: ")
            run_script(choice)
    else:
        print(f"{Fore.RED}Login gagal. Username atau password salah tolol.")

if __name__ == "__main__":
    main()