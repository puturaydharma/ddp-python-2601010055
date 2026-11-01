# Latihan 4: Menghitung Total Belanja

# Input: data barang dari pengguna
nama_barang = input("Masukkan nama barang: ")
harga_satuan = float(input("Masukkan harga satuan: "))
jumlah_barang = int(input("Masukkan jumlah barang: "))

# Proses: hitung subtotal, PPN 11%, dan total bayar
subtotal = harga_satuan * jumlah_barang
ppn = subtotal * 0.11
total_bayar = subtotal + ppn

# Output: tampilkan rincian dengan format 2 angka desimal
print(f"Barang        : {nama_barang}")
print(f"Subtotal      : {subtotal:,.2f}")
print(f"PPN 11%       : {ppn:,.2f}")
print(f"Total Bayar   : {total_bayar:,.2f}")