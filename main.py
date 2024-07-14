##VARIABEL
#variabel adalah tempat menyimpan data
print("+-+-Variabel-+-+")
#assignment nilai
a = 10
print("Nilai a =",a)

#penamaan
nilai_x = 15 #penamaan tidak boleh menggunakan spasi
#angka tidak boleh ditaruh di bagian depan
ribu10 = 10000

#pemanggilan assignment berlaku untuk diatasnya dan bisa diperbarui
a = 7
print("Nilai a =",a)

#assignment indirect
b = a
print("Nilai b =",b)



##TIPE DATA
print("+-+-Tipe Data-+-+")

#tipe data : angka satuan, bulat (integer)
data_integer = 1
print("Data    :",data_integer,)
print("Bertipe :",type(data_integer),"(Integer)")

#tipe data : angka dengan koma desimal (float)
data_float = 1.75
print("Data    :",data_float,)
print("Bertipe :",type(data_float),"(Float)")

#tipe data : kalimat / Kumpulan Karakter (String)
data_string = "Contoh"
print("Data    :",data_string,)
print("Bertipe :",type(data_string),"(String)")

#tipe data : biner true/false (Boolean)
data_bool = True
print("Data    :",data_bool,)
print("Bertipe :",type(data_bool),"(Boolean)")

##TIPE DATA KHUSUS
print("+-+-Tipe Data Khusus-+-+")
#bilangan kompleks
data_complex = complex(5,6)
print("Data    :",data_complex,)
print("Bertipe :",type(data_complex),"(Complex)")

#list (dapat diubah)(menggunakan kurung siku)
kata = ["Belajar", "Python"] 
angka = [10, 50, 100, 1000]
campur = ["Belajar", 100, 7.99, True]
#cetak
print(kata)
print(angka)
print(campur)

#tuple (tidak dapat diubah)(menggunakan kurung biasa)
kata = ("Belajar", "Python")
angka = (10, 50, 100, 1000)
campur = ("Belajar", 100, 7.99, True)
#cetak
print(kata)
print(angka)
print(campur)

#Tipe data dictionary
data = {1:"Belajar",2: ["C++", "Python"], "Di Kampus": "UBSI", "menyerah" : False, "Tahun": 2021}
print(data)


##CASTING
#casting adalah merubah tipe data satu ke tipe data lain
#Tipe-tipe data : int, float, str, bool
print("+-+-Casting-+-+")

data_integer = 9
print("Data    :",data_integer,)
print("Bertipe :",type(data_integer),"(Integer)")

data_float  = float(data_integer)
data_string = str(data_integer)
data_bool   = bool(data_integer)
print("Data    :",data_float, "type :",type(data_float))
print("Data    :",data_string, "type :",type(data_string))
print("Data    :",data_bool, "type :",type(data_bool))


