print("========Program Penghitung Telur========")       ##Program Dimulai
jumlahuang = int(input("Masukan Jumlah uang\t  : Rp."))    #membaca input jumlah uang yang ingin dibelanjakan
tarif = int(input("Masukan Tarif angkutan PP : Rp."))   #membaca input tarif angkutan pulang pergi
telur = int(input("Masukan Harga Telur/Kg\t  : Rp."))      #membaca input harga telur/Kg
#mengcheck apakah uang yang ingin dibelanjakan mencukupi
#jika mencukupi program berlanjut
if jumlahuang > tarif and jumlahuang > telur:
    sisa = jumlahuang-tarif
    totaltelur = sisa//telur
    sisauang = sisa%telur
    print("Jumlah Telur yang dapat dibeli :",totaltelur,"kg", sep='')
    print("Kembali : Rp.",sisauang, sep='')
    print("========================================")
#jika tidak mencukupi program berhenti
else:
    print("Maaf Uang Anda tidak mencukupi")
##Program Selesai