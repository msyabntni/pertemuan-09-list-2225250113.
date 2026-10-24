
# Latihan 5: Filter Kelulusan

# Input: Menyimpan daftar nilai dan batas kelulusan.
nilai = [75, 55, 80, 60, 45, 90]
batas_kelulusan = 60

# Proses: Memilih nilai yang lebih besar atau sama dengan 60.
lulus = []

for x in nilai:
    if x >= batas_kelulusan:
        lulus.append(x)

# Output: Menampilkan nilai yang lulus dan jumlahnya.
print(f"Nilai lulus = {lulus}")
print(f"Jumlah lulus = {len(lulus)}")
    