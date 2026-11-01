# Latihan 2: Menghitung Luas & Keliling Persegi Panjang

panjang = float(input("Masukkan panjang (m): "))
lebar = float(input("Masukkan lebar (m): "))

luas = panjang * lebar
keliling = 2 * (panjang + lebar)

print(f"Luas     : {luas} m2")
print(f"Keliling : {keliling} m")

# ==========================================
# TRACE TABLE
# Masukan contoh: panjang = 8, lebar = 5
# ------------------------------------------
# Baris | panjang | lebar | luas  | keliling | Output
# ------------------------------------------
#   3   |   8.0   |   -   |   -   |    -     | Masukkan panjang (m): 
#   4   |   8.0   |  5.0  |   -   |    -     | Masukkan lebar (m): 
#   6   |   8.0   |  5.0  |  40.0 |    -     | -
#   7   |   8.0   |  5.0  |  40.0 |   26.0   | -
#   9   |   8.0   |  5.0  |  40.0 |   26.0   | Luas     : 40.0 m2
#   10  |   8.0   |  5.0  |  40.0 |   26.0   | Keliling : 26.0 m
# ==========================================