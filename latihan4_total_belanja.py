nama_barang = input("Masukkan nama barang: ")
harga_barang = float(input("Masukkan harga barang: "))
jumlah_barang = int(input("Masukkan jumlah barang: "))

subtotal = harga_barang * jumlah_barang
ppn = subtotal * 0.11
total_bayar = subtotal + ppn

print(f"Subtotal: Rp{subtotal}")
print(f"PPN: Rp{ppn}")
print(f"Total Bayar: Rp{total_bayar}")


#Uji Coba dengan Input:
#  nama_barang   = Buku
#  harga_satuan  = 25000
#  jumlah_barang = 3

#+-------+--------------------------------------+-------------+--------------+---------------+----------+--------+-------------+----------------------------------------------+
#| Baris | Instruksi / Statement                | nama_barang | harga_satuan | jumlah_barang | subtotal | ppn    | total_bayar | Output / Layar                               |
#+-------+--------------------------------------+-------------+--------------+---------------+----------+--------+-------------+----------------------------------------------+
#| 5     | nama_barang = input(...)             | 'Buku'      | -            | -             | -        | -      | -           | Masukkan nama barang: Buku                   |
#| 6     | harga_satuan = int(input(...))       | 'Buku'      | 25000        | -             | -        | -      | -           | Masukkan harga satuan: 25000                 |
#| 7     | jumlah_barang = int(input(...))      | 'Buku'      | 25000        | 3             | -        | -      | -           | Masukkan jumlah barang: 3                    |
#| 10    | subtotal = harga_satuan * jumlah...  | 'Buku'      | 25000        | 3             | 75000    | -      | -           | -                                            |
#| 11    | ppn = subtotal * 0.11                | 'Buku'      | 25000        | 3             | 75000    | 8250.0 | -           | -                                            |
#| 12    | total_bayar = subtotal + ppn         | 'Buku'      | 25000        | 3             | 75000    | 8250.0 | 83250.0     | -                                            |
#| 15    | print(f"Subtotal {subtotal} ...")    | 'Buku'      | 25000        | 3             | 75000    | 8250.0 | 83250.0     | Subtotal 75000, PPN 8250.0, Total 83250.0    |
#+-------+--------------------------------------+-------------+--------------+---------------+----------+--------+-------------+----------------------------------------------+