import time
start_time = time.time() #untuk mengecek kecepatan running

print ("Hello") #print merupakan kode untuk menampilkan ke layout
print ("Apa kabarnya hari ini")

a = 10 # ini adalah coment

"""ini adalah comment 
multiline"""

print (a)
for i in range(1,1000):
    a = 10

print(time.time() - start_time, "detik") #mencetak kecepatan running

#kita bisa mengcompile python ke yang namanya bytcode
#cara mengcompile, buka terminal dan tuliskan 'python -m py_compile Main.py'
#kegunaan mengcompile adalah untuk mempercepat program python