print("-"*50)
print(f"{'Pendaftaran Mahasiswa Baru':^50}")
print("-"*50)
nis = input("Masukan NIS  : ")
nama = input("Masukan Nama : ")
jurusan = input("Masukan Jurusan [SI|SIA] : ")

if jurusan == "SI" or jurusan == "si":
    nama_jurusan = "Sistem Informasi"
    harga = 2400000
elif jurusan == "SIA" or jurusan == "sia":
    nama_jurusan = "Sistem Informasi Akutansi"
    harga = 2000000

print("-"*50)
print("NIS\t: ",nis)
print("Nama\t: ",nama)
print("Jurusan : ",nama_jurusan)
print("Harga\t: ",harga)
print("-"*50)