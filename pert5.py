# operasi aritmatika
# x / + -

# operasi penjumlahan +
a = 12
b = 9
hasil = a + b
print(a, "+", b, "=", hasil)

# pengurangan -
a = 9
b = 12
hasil = a - b
print(a, "-", b, "=", hasil)

# perkalian *
a = 9
b = 12
hasil = a * b
print(a, "x", b, "=", hasil)

# pembagian /
a = 15
b = 4
hasil = a / b
print(a, ":", b, "=", hasil)


# perpangkatan menggunakan ** (eksponensial)
a = 9
b = 12
hasil = a ** b
print(a, "pangkat", b, "=", hasil)

# sisa pembagian (modulus) %
a = 12
b = 9
hasil = a % b
print(a, "mod", b, "=", hasil)

# floor division //
a = 15
b = 4
hasil = a // b
print(a, "floor division", b, "=", hasil)


# operasi prioritas
# 1. ()
# 2. perpangkatan / akar
# 3. perkalian pembagian
# 4. penjumlahan pengurangan
# Buatlah operasi penjumlahan yang menggabungkan semua operasi di atas

# contoh operasi gabungan
a = 9
b = 12
c = 4

hasil = (a + b) + a**1 - (b % c) + (b // c) * 1
print("Hasil operasi gabungan =", hasil)
