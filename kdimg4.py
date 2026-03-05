"""
TUGAS KRIPTOGRAFI: ANALISIS & IMPLEMENTASI MEKANISME KRIPTOGRAFI
Algoritma: Diffie-Hellman Key Exchange & XOR Cipher
Implementasi: Python (From Scratch)
"""

import time

def generate_public_key(base, private_key, modulus):
    """Menghitung kunci publik menggunakan modular exponentiation: (base^private) % modulus"""
    return pow(base, private_key, modulus)

def generate_shared_secret(received_public_key, private_key, modulus):
    """Menghitung shared secret (kunci rahasia bersama)."""
    return pow(received_public_key, private_key, modulus)

def encrypt_message(plaintext, key):
    """Mengubah Plaintext menjadi Ciphertext menggunakan logika bitwise XOR."""
    ciphertext = []
    for char in plaintext:
        # Karakter diubah ke ASCII, lalu di-XOR dengan kunci
        encrypted_char = ord(char) ^ key
        ciphertext.append(encrypted_char)
    return ciphertext

def decrypt_message(ciphertext, key):
    """Mengembalikan Ciphertext menjadi Plaintext asli menggunakan XOR."""
    decrypted_text = ""
    for code in ciphertext:
        # (A XOR B) XOR B = A
        decrypted_char = chr(code ^ key)
        decrypted_text += decrypted_char
    return decrypted_text

def main():
    print("====================================================")
    print("   DEMO IMPLEMENTASI DIFFIE-HELLMAN & XOR CIPHER   ")
    print("====================================================\n")

    # --- STEP 1: PARAMETER PUBLIK ---
    print("[TAHAP 1] Penentuan Parameter Publik")
    p = 23  # Bilangan Prima (Modulus)
    g = 5   # Basis (Generator)
    print(f"Pihak-pihak menyepakati angka publik: p = {p}, g = {g}")
    input(">> Tekan Enter untuk lanjut ke Pembangkitan Kunci...")

    # --- STEP 2: KEY GENERATION ---
    print("\n[TAHAP 2] Pembangkitan Kunci (Key Generation)")
    # Alice
    a_private = 6
    a_public = generate_public_key(g, a_private, p)
    print(f"Alice: Private Key = {a_private}, Public Key = {a_public}")

    # Bob
    b_private = 15
    b_public = generate_public_key(g, b_private, p)
    print(f"Bob  : Private Key = {b_private}, Public Key = {b_public}")
    input(">> Tekan Enter untuk proses Pertukaran Kunci...")

    # --- STEP 3: SHARED SECRET CALCULATION ---
    print("\n[TAHAP 3] Penghitungan Shared Secret (Kunci Bersama)")
    kunci_rahasia_alice = generate_shared_secret(b_public, a_private, p)
    kunci_rahasia_bob = generate_shared_secret(a_public, b_private, p)
    
    print(f"Kunci Rahasia di sisi Alice: {kunci_rahasia_alice}")
    print(f"Kunci Rahasia di sisi Bob  : {kunci_rahasia_bob}")
    
    shared_key = kunci_rahasia_alice
    print(f"Hasil: Kunci rahasia identik! (K = {shared_key})")
    input(">> Tekan Enter untuk memulai Proses Enkripsi...")

    # --- STEP 4: ENKRIPSI ---
    print("\n[TAHAP 4] Proses Enkripsi (Plaintext -> Ciphertext)")
    plaintext = "KRIPTO"
    ciphertext = encrypt_message(plaintext, shared_key)
    print(f"Pesan Asli (Plaintext) : {plaintext}")
    print(f"Hasil Enkripsi (XOR)   : {ciphertext}")
    input(">> Tekan Enter untuk memulai Proses Dekripsi...")

    # --- STEP 5: DEKRIPSI ---
    print("\n[TAHAP 5] Proses Dekripsi (Ciphertext -> Plaintext)")
    decrypted_msg = decrypt_message(ciphertext, shared_key)
    print(f"Input Ciphertext       : {ciphertext}")
    print(f"Hasil Balik (Plaintext): {decrypted_msg}")
    
    print("\n====================================================")
    print("           DEMO BERHASIL DISELESAIKAN               ")
    print("====================================================")

if __name__ == "__main__":
    main()

