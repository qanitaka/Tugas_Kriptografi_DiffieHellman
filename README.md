# Implementasi Kriptografi: Diffie-Hellman & XOR Cipher

Tugas ini mendemonstrasikan algoritma pertukaran kunci Diffie-Hellman dan enkripsi simetris XOR yang dibangun dari awal (from scratch) tanpa menggunakan library eksternal.

## Detail Tugas
- Nama: Qanitah Khaula A.
- NIM: 24051204062
- Algoritma: Diffie-Hellman Key Exchange + XOR Stream Cipher

## Cara Menjalankan
1. Pastikan Python 3 terinstal.
2. Jalankan perintah: `python main.py`
3. Ikuti instruksi di layar dengan menekan **Enter** untuk melihat proses tahap demi tahap.

## Logika Program
Program bekerja dengan memecah proses menjadi 5 tahap utama:
1. Kesepakatan parameter publik (Prime & Generator).
2. Pembangkitan kunci publik dan privat.
3. Penghitungan *Shared Secret*.
4. Enkripsi teks "KRIPTO" menggunakan operasi Bitwise XOR.
5. Dekripsi untuk mengembalikan pesan ke bentuk semula.

## Kriteria Penilaian
- **Pemahaman Konsep**: Penjelasan matematis modular exponentiation.
- **Kejelasan Langkah**: Demo program step-by-step.
- **Clean Code**: Dokumentasi lengkap dalam komentar kode.
