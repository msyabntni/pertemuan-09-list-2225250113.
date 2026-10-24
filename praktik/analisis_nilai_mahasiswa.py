# Latihan 7: Fungsi Statistik dan Nilai Lulus

# Input: Menerima list nilai dari parameter data.
def rata_rata(data):
    # Proses: Menghitung rata-rata nilai.
    if len(data) == 0:
        return 0
    return sum(data) / len(data)


def nilai_lulus(data, batas=60):
    # Proses: Memilih nilai yang memenuhi batas kelulusan.
    lulus = []
    for nilai in data:
        if nilai >= batas:
            lulus.append(nilai)
    return lulus


# Input: Menyimpan daftar nilai mahasiswa.
nilai = [78, 55, 90, 67, 60, 82, 45, 71, 88, 59]

# Proses: Menghitung rata-rata dan menentukan nilai lulus.
rata = rata_rata(nilai)
daftar_lulus = nilai_lulus(nilai)

# Output: Menampilkan ringkasan nilai.
print("=== Ringkasan Nilai ===")
print(f"Daftar nilai = {nilai}")
print(f"Rata-rata = {rata:.2f}")
print(f"Nilai lulus = {daftar_lulus}")
print(f"Jumlah nilai lulus = {len(daftar_lulus)}")
print(f"Jumlah tidak lulus = {len(nilai) - len(daftar_lulus)}")