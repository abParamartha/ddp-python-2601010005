celsius = float(input("Masukkan suhu dalam Celsius: "))


fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

print(f"Output: {fahrenheit} °F dan {kelvin} K")

#Uji Coba dengan Input:
#  celsius = 30

#+-------+---------------------------------------+---------+------------+--------+-------------------------------------+
#| Baris | Instruksi / Statement                 | celsius | fahrenheit | kelvin | Output / Layar                      |
#+-------+---------------------------------------+---------+------------+--------+-------------------------------------+
#| 5     | celsius = float(input(...))           | 30.0    | -          | -      | Masukkan suhu dalam Celsius (°C): 30|
#| 10    | fahrenheit = (celsius * 9 / 5) + 32   | 30.0    | 86.0       | -      | -                                   |
#| 11    | kelvin = celsius + 273.15             | 30.0    | 86.0       | 303.15 | -                                   |
#| 14    | print(f"{fahrenheit:.2f} °F ...")     | 30.0    | 86.0       | 303.15 | Output 86.00 °F dan 303.15 K        |
#+-------+---------------------------------------+---------+------------+--------+-------------------------------------+