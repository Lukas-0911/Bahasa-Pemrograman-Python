#OPERASI KOMPARASI

#setiap hasil dari operasi komparasi adalah boolean

# >, <, >=, <=, ==, !=, is, dan is not


a = 4
b = 2

# lebih besar dari >
print("===LEBIH DARI===")
hasil = a > 3
print(hasil)
hasil = b > 3
print(hasil)

# lebih kecil dari <
print("===KURANG DARI===")
hasil = a < 3
print(hasil)
hasil = b < 3
print(hasil)

# lebih besar sama dengan >=
print("===LEBIH BESAR SAMA DENGAN===")
hasil = a >= 3
print(hasil)
hasil = a >= 4
print(hasil)
hasil = b >= 3
print(hasil)

# lebih kecil sama dengan >=
print("===LEBIH KECIL SAMA DENGAN===")
hasil = a <= 3
print(hasil)
hasil = a <= 4
print(hasil)
hasil = b <= 3
print(hasil)

# sama dengan ==
print("===SAMA DENGAN===")
hasil = a == 3
print(hasil)
hasil = a == 4
print(hasil)
hasil = b == 3
print(hasil)

# tidak sama dengan !=
print("=== TIDAK SAMA DENGAN===")
hasil = a != 3
print(hasil)
hasil = a != 4
print(hasil)
hasil = b != 3
print(hasil)

# 'is' (membandingkan memory/obyek) sebagai komparasi objek identity
print("===Objek Identity (is)===")
x = 5 # ini adalah assigment membuat objek
y = 5
print('nilai x =',x,',id =',hex(id(x)))
print('nilai y =',y,',id =',hex(id(y)))
hasil = x is y
print('x is y =', hasil)

# 'is not' (membandingkan memory/obyek) sebagai komparasi objek identity
print("===Objek Identity (is not)===")
x = 5 # ini adalah assigment membuat objek
y = 5
print('nilai x =',x,',id =',hex(id(x)))
print('nilai y =',y,',id =',hex(id(y)))
hasil = x is not y
print('x is not y =', hasil)