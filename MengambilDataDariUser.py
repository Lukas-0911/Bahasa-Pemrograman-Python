# Mengambil Imput Dari User

data = input("masukan data : ")

print("data =", data,",type =",type(data)) # data yang dimasukan pasti string

# jika kita ingin mengambil int, maka
data_int = int(input("masukan angka :")) #bisa diganti int dengan float
print("data =", data_int,",type =",type(data_int))

# untuk boolean
biner = bool(int(input("masukan nilai boolean :")))
print("data =", biner,",type =",type(biner))