pokok = 5000000
banyakproduk = int(input("Masukan Banyak Produk yang terjual : "))
hargasatuan = int(input("Masukan Harga Satuan Produk : "))
#Proses
omset = hargasatuan*banyakproduk
if banyakproduk > 100:
    bonus = (20*omset)/100
else:
    bonus = (10*omset)/100
total = pokok+bonus
print("Gaji Yang didapat : Rp.",total)