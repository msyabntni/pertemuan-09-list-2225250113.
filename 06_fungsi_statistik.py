
# Latihan 6: Fungsi Statistik

# Input: Menerima list nilai sebagai parameter fungsi.
def rata_rata(data):
    # Proses: Memeriksa data dan menghitung rata-rata.
    if len(data) == 0:
        return 0

    return sum(data) / len(data)


# Input: Menyimpan lima nilai.
nilai = [75, 80, 65, 90, 88]

# Output: Menampilkan hasil rata-rata dari fungsi.
print(f"Rata-rata = {rata_rata(nilai):.2f}")
    