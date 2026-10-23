panjang = float(input("Masukkan panjang persegi panjang: "))
lebar = float(input("Masukkan lebar persegi panjang: "))

luas = panjang * lebar
print(f"Output Luas: {luas} m2,")

keliling = 2 * (panjang + lebar)
print(f"Output Keliling8: {keliling} m")

#Uji Coba dengan Input:
#  panjang = 8
#  lebar   = 5

#+-------+----------------------------------+---------+-------+------+----------+-------------------------------------+
#| Baris | Instruksi / Statement            | panjang | lebar | luas | keliling | Output / Layar                      |
#+-------+----------------------------------+---------+-------+------+----------+-------------------------------------+
#| 5     | panjang = float(input(...))      | 8.0     | -     | -    | -        | Masukkan panjang (m): 8             |
#| 6     | lebar = float(input(...))        | 8.0     | 5.0   | -    | -        | Masukkan lebar (m): 5               |
#| 9     | luas = panjang * lebar           | 8.0     | 5.0   | 40.0 | -        | -                                   |
#| 10    | keliling = 2 * (panjang + lebar) | 8.0     | 5.0   | 40.0 | 26.0     | -                                   |
#| 13    | print(f"Luas : {luas:.1f} ...")  | 8.0     | 5.0   | 40.0 | 26.0     | Luas : 40.0 m2, Keliling : 26.0 m   |
#+-------+----------------------------------+---------+-------+------+----------+-------------------------------------+