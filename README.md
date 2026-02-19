# Get Data Wilayah Indonesia

Project ini berisi 2 script Python untuk mengambil data wilayah Indonesia dari API `wilayah.id`.

## Isi Project

- `wilayah.py`: script interaktif untuk menelusuri data wilayah dari **Provinsi -> Kabupaten/Kota -> Kecamatan -> Kelurahan/Desa**.
- `wilyahaidnew.py`: script sederhana untuk menampilkan daftar semua provinsi beserta kodenya.

## Prasyarat

- Python 3.8+
- Koneksi internet
- Library Python `requests`

## Instalasi

Jalankan perintah berikut di folder project:

```bash
pip install requests
```

## Cara Menjalankan

### 1) Menjalankan `wilyahaidnew.py`

Script ini akan mengambil dan menampilkan semua provinsi.

```bash
python wilyahaidnew.py
```

Contoh output:

```text
Provinsi: ACEH (ID: 11)
Provinsi: SUMATERA UTARA (ID: 12)
...
```

### 2) Menjalankan `wilayah.py`

Script ini bersifat interaktif. Kamu akan diminta memasukkan kode wilayah secara bertahap.

```bash
python wilayah.py
```

Alur yang dijalankan:

1. Menampilkan daftar provinsi
2. Input kode provinsi
3. Menampilkan daftar kabupaten/kota dari provinsi terpilih
4. Input kode kabupaten/kota
5. Menampilkan daftar kecamatan
6. Input kode kecamatan
7. Menampilkan daftar kelurahan/desa

Jika kode yang dimasukkan tidak valid, script akan menampilkan pesan error seperti:

- `Kode Provinsi tidak ditemukan!`
- `Kode Kabupaten tidak ditemukan!`
- `Kode Kecamatan tidak ditemukan!`

## Sumber API

Data diambil dari:

- `https://wilayah.id/api/provinces.json`
- `https://wilayah.id/api/regencies/{kode_provinsi}.json`
- `https://wilayah.id/api/districts/{kode_kabupaten}.json`
- `https://wilayah.id/api/villages/{kode_kecamatan}.json`

## Catatan

- Pastikan koneksi internet aktif saat menjalankan script.
- Jika API tidak dapat diakses, script bisa menampilkan error koneksi.
