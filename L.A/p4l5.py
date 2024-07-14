gp = int(input("Masukan Jumlah Gaji Pokok : "))
tjg = (20*gp)/100
jk = int(input("Masukan Jumlah Jam Kerja : "))
if jk > 200:
    lm = (jk-200)*20000
else:
    lm = 0
totalgaji = gp+tjg+lm
pajak = (10*totalgaji)/100
gajiakhir = totalgaji-pajak
print("Hasil Lembur anda adalah : Rp.",lm)
print("Gaji anda adalah : Rp.",totalgaji)
print("Gaji anda setelah Pajak 10 Persen adalah : Rp.",gajiakhir)