# Tugas M9 - Unit Testing dan Test-Driven Development

**Nama:** Firman H Gultom  
**NIM:** 123140171  
**Mata Kuliah:** Pengujian Perangkat Lunak

## Deskripsi Proyek

Proyek ini merupakan implementasi tugas Minggu 9 mengenai *Unit Testing* dan *Test-Driven Development (TDD)* menggunakan Python dan pytest.

Program yang dikembangkan merupakan sistem peminjaman buku perpustakaan sederhana dengan dua fungsi utama, yaitu menghitung denda keterlambatan dan memeriksa kelayakan peminjaman berdasarkan jenis keanggotaan.

## Teknologi yang Digunakan

- Python 3.13
- Pytest 9.2.0
- Visual Studio Code
- Git dan GitHub

## Fitur Program

### 1. Perhitungan Denda (`hitung_denda`)

Menghitung denda berdasarkan jumlah hari keterlambatan dengan ketentuan:

- Keterlambatan negatif menghasilkan `ValueError`.
- Masa tenggang selama 1 hari.
- Denda sebesar Rp500 per hari setelah masa tenggang.
- Denda maksimal sebesar Rp25.000.

### 2. Pemeriksaan Kelayakan Peminjaman (`cek_kelayakan_pinjam`)

Memeriksa kelayakan jumlah buku berdasarkan jenis keanggotaan:

- Anggota Reguler dapat meminjam kurang dari 5 buku.
- Anggota Premium dapat meminjam kurang dari 7 buku.
- Jumlah peminjaman negatif menghasilkan `ValueError`.
- Jenis keanggotaan tidak bersifat case-sensitive.
- Jenis keanggotaan yang tidak valid menghasilkan `ValueError`.

## Struktur Proyek

```text
TUGAS_M9_Firman H Gultom/
│
├── peminjaman.py
├── test_peminjaman.py
├── README.md
├── .gitignore
└── varian_saya.json
```

File `varian_saya.json` digunakan sebagai konfigurasi pribadi dan tidak disertakan dalam repository publik.

## Instalasi dan Menjalankan Program

### 1. Clone Repository

```bash
git clone https://github.com/Firmanhg/Tugas_M09_Firman-H-Gultom.git
```

### 2. Masuk ke Direktori Proyek

```bash
cd Tugas_M09_Firman-H-Gultom
```

### 3. Instalasi Pytest

```bash
pip install pytest
```

### 4. Menjalankan Unit Testing

```bash
pytest -v
```

## Metode Pengujian

Pengujian dilakukan menggunakan pendekatan Test-Driven Development (TDD) dengan tiga tahapan:

1. **Red:** Membuat pengujian terlebih dahulu dan memastikan pengujian gagal ketika implementasi belum tersedia.
2. **Green:** Membuat implementasi fungsi hingga seluruh pengujian berhasil.
3. **Refactor:** Memeriksa dan merapikan kode tanpa mengubah perilaku program.

Teknik pengujian yang digunakan:

- `pytest.mark.parametrize` untuk menguji beberapa variasi input.
- `pytest.fixture` untuk menyediakan data pengujian.
- `pytest.raises` untuk menguji penanganan exception `ValueError`.
- Mutation testing untuk memastikan pengujian mampu mendeteksi kesalahan pada implementasi.

## Hasil Pengujian
<img width="913" height="268" alt="image" src="https://github.com/user-attachments/assets/3dddc8ab-9065-461b-b88d-6dc4b2615098" />

Berdasarkan pengujian terakhir, diperoleh hasil:

```text
17 passed
0 failed
```

Pengujian mutation testing juga berhasil mendeteksi kesalahan ketika batas maksimal denda dihilangkan dari implementasi.
