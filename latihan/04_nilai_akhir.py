# Program Menghitung Nilai Akhir

nama = input("Masukkan nama: ")
nilai_tugas = float(input("Masukkan nilai tugas: "))
nilai_uts = float(input("Masukkan nilai UTS: "))
nilai_uas = float(input("Masukkan nilai UAS: "))

nilai_akhir = (20 / 100 * nilai_tugas) + (30 / 100 * nilai_uts) + (50 / 100 * nilai_uas)

print(f"Nama: {nama}")
print(f"Nilai akhir: {nilai_akhir:.2f}")