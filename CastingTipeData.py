# Casting Tipe Data 
# atau merubah data dari satu tipe ke tipe lain
# tipe data : int, float, str, boolean

## INTEGER
print("===INTEGER===")
data_int = 9;
print("data = ",data_int, ",type",type(data_int))

#cara mengubah data
data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) # akan false jika nilai int = 0
print("data = ", data_float,",type = ",type(data_float))
print("data = ", data_str,",type = ",type(data_str))
print("data = ", data_bool,",type = ",type(data_bool))

## FLOAT
print("===FLOAT===")
data_float = 9.5;
print("data = ",data_float, ",type",type(data_float))

#cara mengubah data
data_float = int(data_float) # akan dibulatkan kebawah
data_str = str(data_float)
data_bool = bool(data_float) # akan false jika nilai int = 0
print("data = ", data_int,",type = ",type(data_int))
print("data = ", data_str,",type = ",type(data_str))
print("data = ", data_bool,",type = ",type(data_bool))

## BOOLEAN
print("===BOOLEAN===")
data_bool = True;
print("data = ",data_bool, ",type",type(data_bool))

#cara mengubah data
data_float = int(data_bool)
data_str = str(data_bool)
data_bool = float(data_bool)
print("data = ", data_int,",type = ",type(data_int))
print("data = ", data_str,",type = ",type(data_str))
print("data = ", data_float,",type = ",type(data_float))

## STRING
print("===STRING===")
data_bool = "Aman";
print("data = ",data_str, ",type",type(data_str))

#cara mengubah data 

# data_float = int(data_str) 'harus angka'
data_str = bool(data_str) # akan bernilai 'false' jika stringnya kosong/tidak diisi
# data_bool = float(data_str) 'harus angka'

#print("data = ", data_int,",type = ",type(data_int))
print("data = ", data_bool,",type = ",type(data_bool))
#print("data = ", data_float,",type = ",type(data_float))