# OPERASI LOGIKA ATAU BOOLEAN 

# not, or, and, xor

## NOT (akan true jika kedua data sama)
print("===NOT===")
a = True
c = not a
print('data a =', a)
print('------not------')
print('data c =', c)

## OR (Akan false jika keduanya false)
print("===OR===")
a = True
b = False
c = a or b
print(a,'OR',b,'=', c)
a = False
b = False
c = a or b
print(a,'OR',b,'=', c)
a = False
b = True
c = a or b
print(a,'OR',b,'=', c)
a = True
b = True
c = a or b
print(a,'OR',b,'=', c)

## END (Akan tru jika kduanya true)
print("===END===")
a = True
b = False
c = a and b
print(a,'and',b,'=', c)
a = False
b = False
c = a and b
print(a,'and',b,'=', c)
a = False
b = True
c = a and b
print(a,'and',b,'=', c)
a = True
b = True
c = a and b
print(a,'and',b,'=', c)

## XOR (Akan true jika salah satunya true, sisanya false)
print("===XOR===")
a = True
b = False
c = a ^ b
print(a,'XOR',b,'=', c)
a = False
b = False
c = a ^ b
print(a,'XOR',b,'=', c)
a = False
b = True
c = a ^ b
print(a,'XOR',b,'=', c)
a = True
b = True
c = a ^ b
print(a,'XOR',b,'=', c)