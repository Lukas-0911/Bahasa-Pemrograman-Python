# OPERASI ARITMATIKA

a = 10
b = 3

# operasi tambah +
hasil = a + b
print(a,'+',b,'=', hasil)

# operasi pengurangan -
hasil = a - b
print(a,'-',b,'=', hasil)

# operasi perkalian *
hasil = a * b
print(a,'x',b,'=', hasil)

# operasi pembagian
hasil = a / b
print(a,'/',b,'=', hasil)

#operator eksponen (pangkat) **
hasil = a ** b
print(a,'**',b,'=', hasil)

#operator modulus (sisa pembagian) %
hasil = a % b
print(a,'%',b,'=', hasil)

#operator floor division (Hasil pembagian Dibulatkan) //
hasil = a // b
print(a,'//',b,'=', hasil)

# prioritas operasi, operational precedence

"""
    perhitungan akan diprioritaskan dari
        1. ()
        2. exponen **
        3. perkalian *
        4. pembagian /
        5. modulus %
        6. division //
        7. penjumlahan dan pengurangan + -
"""

x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x 
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x,'=',hasil)

hasil = x + y * z # perkalian akan didahulukan 
print(x,'+',y,'x',z,'=',hasil)

hasil = (x + y) * z #operasi yang ada di dalam tanda kurung akan di kerjakan duluan
print('(',x,'+',y,') x',z,'=',hasil)