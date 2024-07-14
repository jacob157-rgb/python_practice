ulang = 2
for i in range(ulang):
    print("Data ke-", str(i+1))
    nama = input("Masukan Nama Mahasiswa : ")
    uts = int(input("Masukan nilai UTS Mahasiswa : "))
    uas = int(input("Masukan nilai UAS Mahasiswa : "))
    
    print("Nama Mahasiswa adalah %s Nilai UTS = %i dan Nilai UAS = %i" %
          (nama, uts, uas))