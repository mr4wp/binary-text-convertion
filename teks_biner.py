import re
import os
import time

os.system('clear')
time.sleep(1)


def text_to_binary(text):
    """Mengonversi teks ke representasi biner 8-bit."""
    return ' '.join(format(ord(char), '08b') for char in text)

def binary_to_text(binary_string):
    """Mengonversi string biner (kelipatan 8 bit) menjadi teks ASCII."""
    binary_values = binary_string.split(' ')
    ascii_characters = [chr(int(bv, 2)) for bv in binary_values]
    return ''.join(ascii_characters)

def is_valid_binary_string(binary_string):
    """Memeriksa apakah string biner hanya berisi karakter 0 atau 1 dan panjangnya kelipatan 8."""
    if not re.match(r'^[01 ]+$', binary_string):
        return False
    binary_values = binary_string.split(' ')
    return all(len(bv) == 8 for bv in binary_values)

def main():
    print()
    print()
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(" Author    : MR_4WP ")
    print(" COMMUNITY : ANONYMOUS WEST PAPUA ")
    print(" TOOLS     : KONVERTION TEKS-BINER ")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print()
    print()
    print()
    print("Pilih mode :")
    print()
    print("[1]>  Teks  ke Biner")
    print("[2]>  Biner ke Teks")
    print()
    print()
    mode = input("Masukkan pilihan (1/2) : ")

    if mode == '1':
        # Mode Teks ke Biner
        print()
        print()
        text_input = input("Masukkan teks yang ingin dikonversi ke biner: ")
        if text_input:
            binary_output = text_to_binary(text_input)
            print()
            print()
            print(f"Teks Anda dalam biner: {binary_output}")
        else:
            print()
            print()
            print("Input teks tidak boleh kosong.")

    elif mode == '2':
        # Mode Biner ke Teks
        print()
        print()
        binary_input = input("Masukkan kode biner (kelipatan 8 bit, dipisahkan dengan spasi): ")
        if is_valid_binary_string(binary_input):
            text_output = binary_to_text(binary_input)
            print()
            print()
            print(f"diterjemahkan ke teks: {text_output}")
        else:
            print()
            print()
            print("Input biner tidak valid! Pastikan hanya menggunakan '0' dan '1', dengan panjang setiap byte adalah 8 bit, dipisahkan dengan spasi.")

    else:
        print()
        print()
        print("Pilihan tidak valid. Silakan pilih 1 atau 2.")

    # Memberi pilihan untuk melakukan konversi lagi

    print()
    print()
    lagi = input("Do You Want To Continue? (y/n): ").lower()
    if lagi == 'y':
        print("\n" + "-"*50 + "\n")
        main()
    else:
        print()
        print()
        print("Terima kasih telah menggunakan Konverter Biner-Teks Modern!")

if __name__ == "__main__":
    main()
