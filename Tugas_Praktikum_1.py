import array

arr = array.array('i' , [1, 2, 3, 4, 5])

print(arr)       # array('i' , [1, 2, 3, 4, 5])
print(list(arr)) # [1, 2, 3, 4, 5]

# 1. Mengakses Elemen Array
print(arr[0]) # 1

# 2. Mengubah Elemen Array
arr[1] = 20
print(arr) # array('i' , [1, 20, 3, 4, 5])

# 3. Menambah Elemen
arr.append(6)
print(arr) # array('i' , [1, 20, 3, 4, 5, 6])

# 4. Menggabungkan Array dengan extend()
arr.extend([7, 8, 9])
print(arr) # array('i' , [1, 20, 3, 4, 5, 6, 7, 8, 9])

# 5. Menghapus Elemen dengan remove()
arr.remove(20)
print(arr) # array('i' , [1, 3, 4, 5, 6, 7, 8, 9])

# 6. Menggunakan Slicing
# Mengambil 3 elemen pertama (indeks 0, 1, 2)
bagian_awal = arr[0:3]
# Mengambil 3 elemen terakhir menggunakan indeks negatif
bagian_akhir = arr[-3:]

print(bagian_awal)  # array('i' , [1, 3, 4])
print(bagian_akhir) # array('i' , [7, 8, 9])
print(arr)          # array('i' , [1, 3, 4, 5, 6, 7, 8, 9])

# 7. Menghitung Kemunculan dengan Count()
print(arr.count(5)) # 1

# 8. Membalik Urutan dengan reverse()
arr.reverse()
print(arr) # array('i' , [9, 8, 7, 6, 5, 4, 3, 1])
