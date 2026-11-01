# Latihan 3: Konversi Suhu Celsius ke Fahrenheit & Kelvin

# Input: suhu dalam Celsius dari pengguna
celsius = float(input("Masukkan suhu dalam Celsius (°C): "))

# Proses: konversi ke Fahrenheit dan Kelvin
fahrenheit = celsius * 9/5 + 32
kelvin = celsius + 273.15

# Output: tampilkan hasil dengan 2 angka desimal
print(f"Fahrenheit : {fahrenheit:.2f} °F")
print(f"Kelvin     : {kelvin:.2f} K")