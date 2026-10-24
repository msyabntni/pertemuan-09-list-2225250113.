# Pertemuan 09 - List Python

**Nama:** Masya Bantani 
**NIM:** 2225250113 
**Kelas:** 3E  
**Mata Kuliah:** Algoritma dan Pemrograman

## Tujuan

Mempelajari list dalam Python, meliputi pembuatan list, indeks, slicing, manipulasi data, agregasi nilai, penyaringan data, serta penggunaan fungsi untuk mengolah sekumpulan nilai agar program lebih terstruktur dan mudah dipahami.

## Struktur Folder

```text
pertemuan-09-list-2225250119/
├── README.md
├── .gitignore
├── latihan/
│   ├── 01_buat_list.py
│   ├── 02_indeks_slicing.py
│   ├── 03_manipulasi_list.py
│   ├── 04_agregasi_nilai.py
│   ├── 05_filter_kelulusan.py
│   └── 06_fungsi_statistik.py
└── praktik/
    └── analisis_nilai_mahasiswa.py
```

## Materi yang Dipelajari

1. Membuat dan membaca list menggunakan tanda kurung siku `[]`.
2. Mengakses elemen list menggunakan indeks.
3. Menggunakan slicing untuk mengambil sebagian elemen list.
4. Memanipulasi list menggunakan `append()`, `insert()`, dan `remove()`.
5. Menghitung total, rata-rata, nilai minimum, dan maksimum menggunakan fungsi bawaan Python.
6. Menyaring nilai berdasarkan batas kelulusan menggunakan perulangan dan percabangan.
7. Membuat fungsi untuk menghitung rata-rata dan menentukan nilai yang lulus.
8. Menguji program melalui terminal VS Code dan mengelola tugas menggunakan Git dan GitHub.

## Deskripsi Latihan

| **File** | **Keterangan** |
|---|---|
| `01_buat_list.py` | Membuat list berisi lima nilai dan menghitung jumlah elemennya. |
| `02_indeks_slicing.py` | Menampilkan elemen pertama, terakhir, tiga elemen awal, dan elemen indeks 1 sampai 3. |
| `03_manipulasi_list.py` | Mengubah, menambahkan, menyisipkan, dan menghapus elemen list. |
| `04_agregasi_nilai.py` | Menghitung total, rata-rata, nilai minimum, dan maksimum. |
| `05_filter_kelulusan.py` | Menampilkan nilai yang memenuhi batas kelulusan 60 dan menghitung jumlahnya. |
| `06_fungsi_statistik.py` | Membuat fungsi `rata_rata(data)` untuk menghitung rata-rata nilai. |
| `analisis_nilai_mahasiswa.py` | Menganalisis nilai mahasiswa menggunakan fungsi rata-rata dan penyaringan nilai lulus. |

## Cara Menjalankan Program

Pastikan Python sudah terpasang di komputer dan terminal VS Code berada di folder utama proyek.

### 1. Menjalankan File Latihan

Untuk menjalankan latihan pertama, gunakan perintah berikut:

```bash
python latihan/01_buat_list.py
```

Untuk menjalankan latihan lainnya, gunakan perintah berikut:

```bash
python latihan/02_indeks_slicing.py
python latihan/03_manipulasi_list.py
python latihan/04_agregasi_nilai.py
python latihan/05_filter_kelulusan.py
python latihan/06_fungsi_statistik.py
```

### 2. Menjalankan Program Praktik

Jalankan perintah berikut pada terminal VS Code:

```bash
python praktik/analisis_nilai_mahasiswa.py
```

## Hasil Pengujian Latihan

| **No.** | **Program** | **Hasil Pengujian** |
|---|---|---|
| 1 | Membuat dan membaca list | Banyak data = 5 |
| 2 | Indeks dan slicing | Elemen pertama = 75, elemen terakhir = 70 |
| 3 | Manipulasi list | `[75, 70, 82, 90]` |
| 4 | Agregasi nilai | Total = 398, rata-rata = 79.60 |
| 5 | Filter kelulusan | Nilai lulus = `[75, 80, 60, 90]`, jumlah = 4 |
| 6 | Fungsi statistik | Rata-rata = 79.60 |

## Hasil Pengujian Praktik

Program praktik `analisis_nilai_mahasiswa.py` menggunakan daftar nilai berikut:

`[78, 55, 90, 67, 60, 82, 45, 71, 88, 59]`

| **Operasi** | **Input** | **Hasil Pengujian** |
|---|---|---|
| Menghitung rata-rata | 10 nilai mahasiswa | 69.50 |
| Menentukan nilai lulus | Batas kelulusan = 60 | `[78, 90, 67, 60, 82, 71, 88]` |
| Menghitung jumlah lulus | Batas kelulusan = 60 | 7 mahasiswa |
| Menghitung jumlah tidak lulus | Batas kelulusan = 60 | 3 mahasiswa |

Berdasarkan hasil pengujian, program berhasil menghitung rata-rata nilai mahasiswa sebesar 69.50. Sebanyak 7 nilai memenuhi batas kelulusan, sedangkan 3 nilai belum memenuhi batas kelulusan.

## Kuis Formatif - Kuis 3

Kuis formatif membahas materi list Python, meliputi penggunaan list untuk menyimpan banyak data, indeks dan slicing, manipulasi elemen, fungsi untuk menghitung jumlah elemen dan rata-rata, penanganan list kosong, serta perintah Git untuk mengirim commit lokal ke GitHub.

## Refleksi

Melalui pertemuan ini, saya mempelajari cara menyimpan dan mengolah sekumpulan data menggunakan list dalam Python. Saya juga memahami penggunaan indeks dan slicing, manipulasi elemen list, serta fungsi bawaan seperti `sum()`, `len()`, `min()`, dan `max()` untuk melakukan perhitungan statistik sederhana.

Selain itu, saya mempelajari cara menyaring nilai berdasarkan batas kelulusan dan membuat fungsi untuk menghitung rata-rata serta menentukan nilai yang lulus. Seluruh program telah dijalankan melalui terminal VS Code dan menghasilkan keluaran sesuai dengan yang diharapkan. Materi ini membantu saya memahami pengolahan data secara terstruktur serta meningkatkan kemampuan dalam menggunakan Python, Git, dan GitHub untuk menyelesaikan tugas pemrograman.
