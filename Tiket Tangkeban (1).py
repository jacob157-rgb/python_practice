ulangin="y"
while ulangin=="y":
#input pogram
    print("""
--------------------------------------------------------------
               SELAMAT DATANG DI OBYEK WISATA ALAM
                            TANGKEBAN
                 NYALEMBANG-PULOSARI-PEMALANG
--------------------------------------------------------------
Silahkan Masukkan User dan Password
Pass admin
    """)
    user=input("Masukkan Username   : ")
    password=input("Masukkan Password   : ")
    if password=="admin":
        ngulang="y"
        while ngulang=="y":
            print("""
------------------------------------------------------------
               SELAMAT DATANG DI OBYEK WISATA ALAM
                            TANGKEBAN
                 NYALEMBANG-PULOSARI-PEMALANG
------------------------------------------------------------
Silahkan Pilih Pembelian Tiket

a. Tiket Masuk Tangkeban Park
b. Taman Langit
c. Camping Ground
d. Log Out
------------------------------------------------------------
            """)
            pilihtiket = input("Silahkan Pilih Pembelian Tiket Dengan Memasukkan Abjad Dari List Di Atas : ")

# START FUNGSI A
            if pilihtiket == "a" or pilihtiket == "A":
                ulangtiketbukit = "y"
                while ulangtiketbukit == "y":
                    print("""
-------------------------------------------------
           TIKET MASUK TANGKEBAN PARK
-------------------------------------------------
a. Tiket Orang Masuk                  Rp 25000
b. Tiket Kendaraan Motor              Rp 5000
c. Tiket Kendaraan Mobil              Rp 10000
d. Kembali ke menu awal
-------------------------------------------------
*Beli Tiket Orang Masuk
 Rp 24.000 dengan minimal pembelian 4 orang

*Beli Tiket Kendaraan Motor dan Mobil 
 Potongan harga Rp 1000 
 Dengan minimal pembelian 2 motor/mobil
-------------------------------------------------                    
                    """)
                    pilihan = input("Silahkan Pilih Tiket Dengan Memasukkan Abjad Dari List Diatas : ")

# START TIKET ORANG MASUK
                    if pilihan == "a" or pilihan == "A":
                        stop = "y"
                        while stop == "y":
                            from datetime import datetime
                            current = datetime.now()
                            tahun = current.year
                            bulan = current.month
                            hari = current.day
                            jumlahorang = int(input("\nJumlah Orang             : "))
                            if jumlahorang > 4:
                                print("\nJumlah Maksimal Untuk Satu Tiket 4 Orang\n")
                                break
                            hargatiketorang = 25000
                            totalharga = hargatiketorang * jumlahorang
                            diskon = int(totalharga * 0.04)
                            totalbeli = int(totalharga-diskon)
                            if jumlahorang == 4 :
                                print(                  "Sub Total                : Rp", totalharga)
                                print(                  "Diskon                   : Rp", diskon)
                                print(                  "Total Yang Harus Dibayar : Rp", totalbeli)
                            else :
                                print(                  "Total Yang Harus Dibayar : Rp", totalharga)
                            jumlahbayar = int(input("Uang Yang Diterima       : Rp "))
                            nama = []
                            umur = []
                            for i in range(jumlahorang):
                                print("\nData ke-", i + 1)
                                nama_pengunjung = input(    "Masukkan Nama : ")
                                nama.append(nama_pengunjung)
                                umur_pengunjung = int(input("Masukkan Umur : "))
                                umur.append(umur_pengunjung)
                                print("\n")
                            for i in range(jumlahorang):
                                print("----------------------------------------------")
                                print("              Tiket Orang Masuk               ")
                                print("                   TANGKEBAN                  ")
                                print("          NYALEMBANG-PULOSARI-PEMALANG        ")
                                print("----------------------------------------------")
                                print("                                   {}/{}/{}".format(hari, bulan, tahun))
                                print("Nama Kasir   : ", user)
                                print("\n")
                                for i in range(jumlahorang):
                                    print("Nama : {}".format(nama[i]))
                                    print("Umur : {}".format(umur[i]))
                                    print()
                                if jumlahorang == 4:
                                    print("----------------------------------------------")
                                    print("               Harga Tiket      : Rp", hargatiketorang)
                                    print("               Sub Total        : Rp", totalharga)
                                    print("               Diskon           : Rp", diskon)
                                    print("               Total Pembayaran : Rp", totalbeli)
                                    print("----------------------------------------------")
                                    print("               Jumlah Uang      : Rp", jumlahbayar)
                                    print("               Kembali          : Rp", int(jumlahbayar - (totalharga-diskon)))
                                    print("----------------------------------------------")
                                else :
                                    print("----------------------------------------------")
                                    print("               Harga Tiket      : Rp", hargatiketorang)
                                    print("               Total Pembayaran : Rp", totalharga)
                                    print("----------------------------------------------")
                                    print("               Jumlah Uang      : Rp", jumlahbayar)
                                    print("               Kembali          : Rp", jumlahbayar - totalharga)
                                    print("----------------------------------------------")
                                print("                 Terimakasih                  ")
                                print("----------------------------------------------")
                            ulangtiketbukit = input("Masukkan y untuk kembali : ")
                            break
# END TIKET ORANG MASUK

# START TIKET MOTOR
                    elif pilihan == "b" or pilihan == "B":
                        pas = "y"
                        while pas == "y":
                            from datetime import datetime
                            current = datetime.now()
                            tahun = current.year
                            bulan = current.month
                            hari = current.day
                            import datetime
                            x = datetime.datetime.now()
                            waktu = (x.strftime("%H:%M:%p"))
                            jumlahmotor = int(input(       "\nMasukkan Jumlah Kendaraan Motor : "))
                            if jumlahmotor >= 3:
                                print("\nJumlah Maksimal Untuk Satu Tiket 2 Kendaraan Motor\n")
                                break
                            hargatiketmotor = 5000
                            totalparkirmotor = hargatiketmotor * jumlahmotor
                            diskon = int(totalparkirmotor * 0.2)
                            totalbeli = int(totalparkirmotor - diskon)
                            if jumlahmotor == 2:
                                print(                       "Sub Total                       : Rp", totalparkirmotor)
                                print(                       "Diskon                          : Rp", diskon)
                                print(                       "Total Yang Harus Dibayar        : Rp", totalbeli)
                            else :
                                print(                       "Total Yang Harus Dibayar        : Rp", totalparkirmotor)
                            bayarparkirmotor = int(input(    "Uang Yang Diterima              : Rp "))
                            listplatmotor = []
                            merkmotor = []
                            for i in range(jumlahmotor):
                                print("\nData ke-", i + 1) 
                                platmotor = input("Masukkan Plat Nomor Motor : ")
                                listplatmotor.append(platmotor)
                                merk = input(     "Masukkan Merk Motor       : ")
                                merkmotor.append(merk)
                            for i in range(jumlahmotor):
                                print("----------------------------------------------")
                                print("               Tiket Masuk Motor              ")
                                print("                   TANGKEBAN                  ")
                                print("          NYALEMBANG-PULOSARI-PEMALANG        ")
                                print("----------------------------------------------")
                                print("{}/{}/{}                          ".format(hari, bulan, tahun),waktu)
                                print()
                                print("Nama Kasir   : ",user)
                                print("\n")
                                for i in range(jumlahmotor):
                                    print("Nomor Kendaraan {}".format(listplatmotor[i]))
                                    print("Merk Motor {}".format(merkmotor[i]))
                                    print()
                                if jumlahmotor == 2:
                                    print("----------------------------------------------")
                                    print("               Harga Tiket      : Rp", hargatiketmotor)
                                    print("               Sub Total        : Rp", totalparkirmotor)
                                    print("               Diskon           : Rp", diskon)
                                    print("               Total Pembayaran : Rp", totalbeli)
                                    print("----------------------------------------------")
                                    print("               Jumlah Uang      : Rp", bayarparkirmotor)
                                    print("               Kembali          : Rp", int(bayarparkirmotor - totalbeli))
                                    print("----------------------------------------------")
                                else :
                                    print("----------------------------------------------")
                                    print("               Harga Tiket      : Rp", hargatiketmotor)
                                    print("               Total Pembayaran : Rp", totalparkirmotor)
                                    print("----------------------------------------------")
                                    print("               Jumlah Uang      : Rp", bayarparkirmotor)
                                    print("               Kembali          : Rp", int(bayarparkirmotor - totalparkirmotor))
                                    print("----------------------------------------------")
                                print("                 Terimakasih                  ")
                                print("----------------------------------------------")
                            ulangtiketbukit = input("Masukkan y untuk kembali : ")
                            break
# END TIKET MOTOR

# START TIKET MOBIL
                    elif pilihan == "c" or pilihan == "C":
                        cus = "y"
                        while cus == "y":
                            from datetime import datetime
                            current = datetime.now()
                            tahun = current.year
                            bulan = current.month
                            hari = current.day
                            import datetime
                            x = datetime.datetime.now()
                            waktu = (x.strftime("%H:%M:%p"))
                            jumlahmobil = int(input(   "\nMasukkan Jumlah Kendaraan Mobil : "))
                            if jumlahmobil >= 3:
                                print("\nJumlah Maksimal Untuk Satu Tiket 2 Kendaraan Mobil\n")
                                break
                            hargatiketmobil = 10000
                            totalparkirmobil = hargatiketmobil * jumlahmobil
                            diskon = int(totalparkirmobil * 0.1)
                            totalbeli = int(totalparkirmobil-diskon)
                            if jumlahmobil == 2:
                                print(                       "Sub Total                       : Rp", totalparkirmobil)
                                print(                       "Diskon                          : Rp", diskon)
                                print(                       "Total Yang Harus Di Bayar       : Rp", totalbeli)
                            else :
                                print(                       "Total Yang Harus Di Bayar       : Rp", totalparkirmobil)
                            bayarparkirmobil = int(input("Uang Yang Diterima              : "))
                            listplatmobil = []
                            listmerkmobil = []
                            for i in range(jumlahmobil):
                                print("\nData ke-", i + 1)
                                platmobil = input("Masukkan Plat Nomor Mobil : ")
                                listplatmobil.append(platmobil)
                                merkmobil = input("Masukkan Merk Mobil       : ")
                                listmerkmobil.append(merkmobil)
                            for i in range(jumlahmobil):
                                print("----------------------------------------------")
                                print("               Tiket Masuk Mobil              ")
                                print("                   TANGKEBAN                  ")
                                print("          NYALEMBANG-PULOSARI-PEMALANG        ")
                                print("----------------------------------------------")
                                print("{}/{}/{}                             ".format(hari, bulan, tahun),waktu)
                                print()
                                print("Nama Kasir   : ", user)
                                print("\n")
                                for i in range(jumlahmobil):
                                    print("Nomor Kendaraan {}".format(listplatmobil[i]))
                                    print("Merk Mobil {}".format(listmerkmobil[i]))
                                    print()
                                if jumlahmobil == 2:
                                    print("----------------------------------------------")
                                    print("               Harga Tiket      : Rp", hargatiketmobil)
                                    print("               Sub Total        : Rp", totalparkirmobil)
                                    print("               Diskon           : Rp", diskon)
                                    print("               Total Pembayaran : Rp", totalbeli)
                                    print("----------------------------------------------")
                                    print("               Jumlah Uang      : Rp", bayarparkirmobil)
                                    print("               Kembali          : Rp", int(bayarparkirmobil - totalbeli))
                                    print("----------------------------------------------")
                                else :
                                    print("----------------------------------------------")
                                    print("               Harga Tiket      : Rp", hargatiketmobil)
                                    print("               Total Pembayaran : Rp", totalparkirmobil)
                                    print("----------------------------------------------")
                                    print("               Jumlah Uang      : Rp", bayarparkirmobil)
                                    print("               Kembali          : Rp", int(bayarparkirmobil - totalparkirmobil))
                                    print("----------------------------------------------")
                                print("                 Terimakasih                  ")
                                print("----------------------------------------------")
                            ulangtiketbukit = input("Masukkan y untuk kembali : ")
                            break
# END TIKET MOBIL

#KEMBALI
                    elif pilihan=="d" or pilihan=="D":
                        ngulang="y"
                        break
#END KEMBALI
                    else:
                        ulangtiketbukit = input("Pilihan tidak ada apakah anda ingin mengulangi y/n : ")
# END FUNGSI A

# START FUNGSI B TAMAN LANGIT
            elif pilihtiket == "b" or pilihtiket == "B":
                ulangtikettaman = "y"
                while ulangtikettaman == "y":
                    import time
                    hari = ("Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu","Minggu")
                    sekarang = time.time()
                    infowaktu = time.localtime(sekarang)
                    info_hari = hari[infowaktu[6]]
#KONDISI PERTAMA TAMAN LANGIT WEEKDAY
                    if info_hari == hari[0] or info_hari == hari[1] or info_hari == hari[2] or info_hari == hari[
                        3] or info_hari == hari[4]:
                        print("""
------------------------------------
      TIKET MASUK TAMAN LANGIT
------------------------------------
*Weekday                 Rp 40.000
 untuk pembelian Tiket Standar 
------------------------------------
*Triple Fun Weekday      Rp 108.000
 Diskon 10%
 Jumlah maksimal pembelian 3 tiket
------------------------------------""")
                        lanjut=input("Masukkan L untuk lanjut K untuk kembali ke menu awal : ")
                        if lanjut=="l" or lanjut=="L":
                            stoptaman = "y"
                            while stoptaman == "y":
                                from datetime import datetime
                                current = datetime.now()
                                tahun = current.year
                                bulan = current.month
                                hari = current.day
                                jumlahorang = int(input("\nJumlah orang             : "))
                                if jumlahorang > 3:
                                    print("\nJumlah maksimal pesan 3 orang\n")
                                    break
                                hargatikettaman = 40000
                                totalharga = hargatikettaman * jumlahorang
                                diskon = int(totalharga * 0.1)
                                totalbeli = totalharga - diskon
                                if jumlahorang ==3:
                                    print(                    "Sub Total                : Rp", totalharga)
                                    print(                    "Diskon 10%               : Rp", diskon)
                                    print(                    "Total Yang Harus Dibayar : Rp", totalbeli)
                                else : 
                                    print(                    "Total Yang Harus Dibayar : Rp", totalharga)
                                jumlahbayar = int(input(  "Uang Yang Diterima       : "))
                                nama = []
                                umur = []
                                for i in range(jumlahorang):
                                    print("\nData ke-", i + 1)
                                    nama_pengunjung = input(    "Masukkan Nama : ")
                                    nama.append(nama_pengunjung)
                                    umur_pengunjung = int(input("Masukkan Umur : "))
                                    umur.append(umur_pengunjung)
                                for i in range(jumlahorang):
                                    print("----------------------------------------------")
                                    print("          Tiket Masuk Taman Langit           ")
                                    print("                  Weekday                    ")
                                    print("----------------------------------------------")
                                    print(info_hari,"{}/{}/{}".format(hari, bulan, tahun))
                                    print()
                                    print("Nama Kasir   : ", user)
                                    print("\n")
                                    for i in range(jumlahorang):
                                        print("Nama : {}".format(nama[i]))
                                        print("Umur : {}".format(umur[i]))
                                        print()
                                    if jumlahorang == 3 :
                                        print("----------------------------------------------")
                                        print("                      Harga Tiket : Rp", hargatikettaman)
                                        print("                      Sub Total   : Rp", totalharga)
                                        print("                      Diskon 10%  : Rp", diskon)
                                        print("                      Total Harga : Rp", totalbeli)
                                        print("----------------------------------------------")
                                        print("                      Jumlah Uang : Rp", jumlahbayar)
                                        print("                      Kembali     : Rp", jumlahbayar - totalbeli)
                                        print("----------------------------------------------")
                                    else :
                                        print("----------------------------------------------")
                                        print("                      Harga Tiket : Rp", hargatikettaman)
                                        print("                      Total Harga : Rp", totalharga)
                                        print("----------------------------------------------")
                                        print("                      Jumlah Uang : Rp", jumlahbayar)
                                        print("                      Kembali     : Rp", jumlahbayar - totalharga)
                                        print("----------------------------------------------")
                                    print("                 Terimakasih                  ")
                                    print("----------------------------------------------")
                                ulangtikettaman = input("Masukkan y untuk kembali : ")
                                break
                        elif lanjut=="k" or lanjut=="K":
                           ngulang="y"
                           break
                        else:
                            print("Inputan Salah")
                            ulangtikettaman="y"
#END KONDISI PERTAMA TAMAN LANGIT WEEKDAY

#KONDISI KEDUA TAMAN LANGIT WEEKEND
                    elif info_hari==hari[5] or info_hari==hari[6]:
                        print("""
------------------------------------
     TIKET MASUK TAMAN LANGIT
------------------------------------
*Weekend Taman Langit   Rp 50.000
 untuk pembelian tiket standard 
------------------------------------
*Triple Fun Weekend     Rp 135.000
 Diskon 10%
 Jumlah maksimal pembelian 3 tiket
------------------------------------""")
                        lanjut = input("masukkan l untuk lanjut k untuk kembali ke menu awal : ")
                        if lanjut == "l" or lanjut == "L":
                            stoptaman = "y"
                            while stoptaman == "y":
                                from datetime import datetime
                                current = datetime.now()
                                tahun = current.year
                                bulan = current.month
                                hari = current.day
                                jumlahorang = int(input("\nJumlah orang : "))
                                if jumlahorang > 3:
                                    print("\nJumlah maksimal pesan 3 orang\n")
                                    break
                                hargatikettaman = 50000
                                totalharga = hargatikettaman * jumlahorang
                                diskon = int(totalharga * 0.1)
                                totalbeli = int(totalharga - diskon)
                                if jumlahorang == 3 :
                                    print(                    "Sub Total                : Rp", totalharga)
                                    print(                    "Diskon 10%               : Rp", diskon)
                                    print(                    "Total Yang Harus Dibayar : Rp", totalbeli)
                                else :
                                    print(                    "Total Yang Harus Dibayar : Rp", totalharga)
                                jumlahbayar = int(input(  "Uang Yang Diterima       : Rp "))
                                nama = []
                                umur = []
                                for i in range(jumlahorang):
                                    print("\nData ke-", i + 1)
                                    nama_pengunjung = input(    "Masukkan Nama : ")
                                    nama.append(nama_pengunjung)
                                    umur_pengunjung = int(input("Masukkan Umur : "))
                                    umur.append(umur_pengunjung)
                                for i in range(jumlahorang):
                                    print("----------------------------------------------")
                                    print("           Tiket Masuk Taman Langit           ")
                                    print("                    Weekend                   ")
                                    print("----------------------------------------------")
                                    print(info_hari,"{}/{}/{}".format(hari, bulan, tahun))
                                    print()
                                    print("Nama Kasir   : ", user)
                                    print("\n")
                                    for i in range(jumlahorang):
                                        print("Nama : {}".format(nama[i]))
                                        print("Umur : {}".format(umur[i]))
                                        print()
                                    if jumlahorang == 3 :
                                        print("----------------------------------------------")
                                        print("                      Harga Tiket : Rp", hargatikettaman)
                                        print("                      Sub Total   : Rp", totalharga)
                                        print("                      Diskon 10%  : Rp", diskon)
                                        print("                      Total Harga : Rp", totalbeli)
                                        print("----------------------------------------------")
                                        print("                      Jumlah Uang : Rp", jumlahbayar)
                                        print("                      Kembali     : Rp", jumlahbayar - totalbeli)
                                        print("----------------------------------------------")
                                    else :
                                        print("----------------------------------------------")
                                        print("                      Harga Tiket : Rp", hargatikettaman)
                                        print("                      Total Harga : Rp", totalharga)
                                        print("----------------------------------------------")
                                        print("                      Jumlah Uang : Rp", jumlahbayar)
                                        print("                      Kembali     : Rp", jumlahbayar - totalharga)
                                        print("----------------------------------------------")
                                    print("                 Terimakasih                  ")
                                    print("----------------------------------------------")
                                ulangtikettaman = input("Masukkan Y Untuk Kembali : ")
                                break
                        elif lanjut=="k" or lanjut=="K":
                           ngulang="y"
                           break
                        else:
                            print("Inputan Salah")
                            ulangtikettaman="y"
# END KONDISI KEDUA WEEKEND
# END KONDISI B TAMAN LANGIT

#START CAMPING GROUND
            elif pilihtiket=="c" or pilihtiket=="C":
                stopcamping="y"
                while stopcamping=="y":
                    print("""
--------------------------------------------------------------------------
                        TIKET MASUK CAMPING GROUND
--------------------------------------------------------------------------
                                            Harga Weekday   Harga Weekend
a. Tiket Camping                              Rp 20.000       Rp 50.000  
b. Sewa Tenda                                 Rp 75.000       Rp 150.000
c. Kembali ke menu awal
--------------------------------------------------------------------------
*Weekday (Hari Senin-Jumat)
*Weekend (Hari Sabtu-Minggu)
--------------------------------------------------------------------------
                    """)
                    pilihtiketcamping=input("Silahkan Pilih Tiket Camping Dengan Memasukkan Abjad Dari List Diatas : ")
#START KONDISI A
                    if pilihtiketcamping=="a" or pilihtiketcamping=="A":
                        ulangweekdaycamping = "y"
                        while ulangweekdaycamping == "y":
                            import time
                            hari = ("Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu")
                            sekarang = time.time()
                            infowaktu = time.localtime(sekarang)
                            camping_hari = hari[infowaktu[6]]

#START KONDISI PERTAMA WEEKDAY CAMPING WEEKDAY
                            if camping_hari==hari[0] or camping_hari==hari[1] or camping_hari==hari[2] or camping_hari==hari[3] or camping_hari==hari[4]:
                                print("""
-------------------------------------
     TIKET MASUK CAMPING GROUND
              Weekday
-------------------------------------
*Weekday Camping Ground   Rp 20.000
 untuk pembelian tiket standard

*Jumlah maksimal pesan 3 orang 
-------------------------------------""")
                                lanjut = input("masukkan l untuk lanjut k untuk kembali ke menu awal : ")
                                if lanjut == "l" or lanjut == "L":
                                    stopcamping = "y"
                                    while stopcamping == "y":
                                        from datetime import datetime
                                        current = datetime.now()
                                        tahun = current.year
                                        bulan = current.month
                                        hari = current.day
                                        jumlahorang = int(input("\nJumlah orang             : "))
                                        if jumlahorang > 3:
                                            print("\nJumlah maksimal pesan 3 orang\n")
                                            break
                                        hargatiketcamping = 20000
                                        totalharga = hargatiketcamping * jumlahorang
                                        print(                    "Total yang harus dibayar : Rp", totalharga)
                                        jumlahbayar = int(input(  "Uang Yang Diterima       : "))
                                        nama = []
                                        umur = []
                                        for i in range(jumlahorang):
                                            print("\nData ke-", i + 1)
                                            nama_pengunjung = input("Masukkan Nama : ")
                                            nama.append(nama_pengunjung)
                                            umur_pengunjung = int(input("Masukkan Umur : "))
                                            umur.append(umur_pengunjung)
                                        for i in range(jumlahorang):
                                            print("----------------------------------------------")
                                            print("         Tiket Masuk Camping Ground           ")
                                            print("                  Weekday                     ")
                                            print("----------------------------------------------")
                                            print(camping_hari, "{}/{}/{}".format(hari, bulan, tahun))
                                            print()
                                            print("Nama Kasir   : ", user)
                                            print("\n")
                                            for i in range(jumlahorang):
                                                print("Nama : {}".format(nama[i]))
                                                print("Umur : {}".format(umur[i]))
                                                print()
                                            print("----------------------------------------------")
                                            print("                      Harga Tiket : Rp", hargatiketcamping)
                                            print("                      Total Harga : Rp", totalharga)
                                            print("----------------------------------------------")
                                            print("                      Jumlah Uang : Rp", jumlahbayar)
                                            print("                      Kembali     : Rp", jumlahbayar - totalharga)
                                            print("----------------------------------------------")
                                            print("                 Terimakasih                  ")
                                            print("----------------------------------------------")
                                        ulangweekdaycamping= input("Masukkan y untuk kembali : ")
                                        break
                                elif lanjut == "k" or lanjut == "K":
                                    stopcamping = "y"
                                    break
                                else:
                                    print("inputan salah")
                                    ulangweekdaycamping = "y"
#END KONDISI KEDUA WEEKDAY CAMPING

#START KONDISI WEEKEND CAMPING
                            elif camping_hari==hari[5] or camping_hari==hari[6]:
                                print("""
---------------------------------------
      TIKET MASUK CAMPING GROUND
              Weekend
---------------------------------------
*Weekend Camping Ground   Rp 50.000
 untuk pembelian tiket standard

*Jumlah maksimal pesan 3 orang
---------------------------------------""")
                                lanjut = input("masukkan l untuk lanjut k untuk kembali ke menu awal : ")
                                if lanjut == "l" or lanjut == "L":
                                    stop_camping = "y"
                                    while stop_camping == "y":
                                        from datetime import datetime
                                        current = datetime.now()
                                        tahun = current.year
                                        bulan = current.month
                                        hari = current.day
                                        jumlahorang = int(input("\nJumlah orang             : "))
                                        if jumlahorang > 3:
                                            print("\nJumlah maksimal pesan 3 orang\n")
                                            break
                                        hargatiketcamping = 50000
                                        totalharga = hargatiketcamping * jumlahorang
                                        print(                    "Total yang harus dibayar : Rp", totalharga)
                                        jumlahbayar = int(input(  "Uang yang diterima       : "))
                                        nama = []
                                        umur = []
                                        for i in range(jumlahorang):
                                            print("\nData ke-", i + 1)
                                            nama_pengunjung = input("Masukkan nama : ")
                                            nama.append(nama_pengunjung)
                                            umur_pengunjung = int(input("Masukkan umur : "))
                                            umur.append(umur_pengunjung)
                                        for i in range(jumlahorang):
                                            print("----------------------------------------------")
                                            print("         Tiket Masuk Camping Ground           ")
                                            print("                  Weekend                     ")
                                            print("----------------------------------------------")
                                            print(camping_hari, "{}/{}/{}".format(hari, bulan, tahun))
                                            print()
                                            print("Nama Kasir   : ", user)
                                            print("\n")
                                            for i in range(jumlahorang):
                                                print("Nama : {}".format(nama[i]))
                                                print("Umur : {}".format(umur[i]))
                                                print()
                                            print("----------------------------------------------")
                                            print("                      Harga Tiket : Rp", hargatiketcamping)
                                            print("                      Total Harga : Rp", totalharga)
                                            print("----------------------------------------------")
                                            print("                      Jumlah Uang : Rp", jumlahbayar)
                                            print("                      Kembali     : Rp", jumlahbayar - totalharga)
                                            print("----------------------------------------------")
                                            print("                 Terimakasih                  ")
                                            print("----------------------------------------------")
                                        ulangtiketcamping = input("Masukkan y untuk kembali : ")
                                        break
                                elif lanjut == "k" or lanjut == "K":
                                    stopcamping = "y"
                                    break
                                else:
                                    print("inputan salah")
                                    ulangweekendcamping= "y"
#END KONDISI KEDUA WEEKEND CAMPING GROUND
#END KONDISI A

#START KONDISI B
                    elif pilihtiketcamping=="b" or pilihtiketcamping=="B":
                        ulangweekendcamping = "y"
                        while ulangweekendcamping == "y":
                            import time

                            hari = ("Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu")
                            sekarang = time.time()
                            infowaktu = time.localtime(sekarang)
                            sewa_hari = hari[infowaktu[6]]

# START KONDISI PERTAMA WEEKDAY Sewa Tenda
                            if sewa_hari == hari[0] or sewa_hari == hari[1] or sewa_hari == hari[2] or sewa_hari == hari[
                                3] or sewa_hari == hari[4]:
                                print("""
----------------------------------------------------
                TIKET SEWA TENDA
                    Weekday
----------------------------------------------------
Weekday Sewa Tenda                      Rp 75.000
*Jumlah maksimal pesan 3 orang
----------------------------------------------------""")
                                lanjut = input("masukkan l untuk lanjut k untuk kembali ke menu awal : ")
                                if lanjut == "l" or lanjut == "L":
                                    stopsewa = "y"
                                    while stopsewa == "y":
                                        from datetime import datetime
                                        current = datetime.now()
                                        tahun = current.year
                                        bulan = current.month
                                        hari = current.day
                                        jumlahorang = int(input("\nJumlah orang             : "))
                                        if jumlahorang > 3:
                                            print("\nJumlah maksimal pesan 3 orang\n")
                                            break
                                        hargatiketsewa = 75000
                                        totalharga = hargatiketsewa * jumlahorang
                                        print(                    "Total yang harus dibayar : Rp", totalharga)
                                        jumlahbayar = int(input(  "Uang yang diterima       : "))
                                        nama = []
                                        umur = []
                                        for i in range(jumlahorang):
                                            print("\nData ke-", i + 1)
                                            nama_pengunjung = input("Masukkan nama : ")
                                            nama.append(nama_pengunjung)
                                            umur_pengunjung = int(input("Masukkan umur : "))
                                            umur.append(umur_pengunjung)
                                        for i in range(jumlahorang):
                                            print("----------------------------------------------")
                                            print("              TIKET SEWA TENDA                ")
                                            print("                  Weekday                     ")
                                            print("----------------------------------------------")
                                            print(sewa_hari, "{}/{}/{}".format(hari, bulan, tahun))
                                            print()
                                            print("Nama Kasir   : ", user)
                                            print("\n")
                                            for i in range(jumlahorang):
                                                print("Nama : {}".format(nama[i]))
                                                print("Umur : {}".format(umur[i]))
                                                print()
                                            print("----------------------------------------------")
                                            print("                      Harga Tiket : Rp", hargatiketsewa)
                                            print("                      Total Harga : Rp", totalharga)
                                            print("----------------------------------------------")
                                            print("                      Jumlah Uang : Rp", jumlahbayar)
                                            print("                      Kembali     : Rp", jumlahbayar - totalharga)
                                            print("----------------------------------------------")
                                            print("                 Terimakasih                  ")
                                            print("----------------------------------------------")
                                        ulangweekdaysewa = input("Masukkan y untuk kembali : ")
                                        break
                                elif lanjut == "k" or lanjut == "K":
                                    stopsewa = "y"
                                    break
                                else:
                                    print("inputan salah")
                                    ulangweekdaysewa = "y"
# END KONDISI KEDUA WEEKDAY SEWA TENDA

# START KONDISI WEEKEND SEWA
                            elif sewa_hari == hari[5] or sewa_hari == hari[6]:
                                print("""
----------------------------------------------------
                TIKET SEWA TENDA 
                    Weekend
----------------------------------------------------
Weekend Sewa Tenda                      Rp 150.000
*Jumlah maksimal pesan 3 orang
----------------------------------------------------""")
                                lanjut = input("masukkan l untuk lanjut k untuk kembali ke menu awal : ")
                                if lanjut == "l" or lanjut == "L":
                                    stopsewa = "y"
                                    while stopsewa == "y":
                                        from datetime import datetime
                                        current = datetime.now()
                                        tahun = current.year
                                        bulan = current.month
                                        hari = current.day
                                        jumlahorang = int(input("\nJumlah orang             : "))
                                        if jumlahorang > 3:
                                            print("\nJumlah maksimal pesan 3 orang\n")
                                            break
                                        hargatiketsewa = 150000
                                        totalharga = hargatiketsewa * jumlahorang
                                        print(                    "Total yang harus dibayar : Rp", totalharga)
                                        jumlahbayar = int(input(  "Uang yang diterima       : "))
                                        nama = []
                                        umur = []
                                        for i in range(jumlahorang):
                                            print("\nData ke-", i + 1)
                                            nama_pengunjung = input("Masukkan nama :")
                                            nama.append(nama_pengunjung)
                                            umur_pengunjung = int(input("Masukkan umur :"))
                                            umur.append(umur_pengunjung)
                                        for i in range(jumlahorang):
                                            print("----------------------------------------------")
                                            print("             TIKET SEWA TENDA                 ")
                                            print("                 Weekday                      ")
                                            print("----------------------------------------------")
                                            print(sewa_hari, "{}/{}/{}".format(hari, bulan, tahun))
                                            print()
                                            print("Nama Kasir   : ", user)
                                            print("\n")
                                            for i in range(jumlahorang):
                                                print("Nama : {}".format(nama[i]))
                                                print("Umur : {}".format(umur[i]))
                                                print()
                                            print("----------------------------------------------")
                                            print("                      Harga Tiket : Rp", hargatiketsewa)
                                            print("                      Total Harga : Rp", totalharga)
                                            print("----------------------------------------------")
                                            print("                      Jumlah Uang : Rp", jumlahbayar)
                                            print("                      Kembali     : Rp", jumlahbayar - totalharga)
                                            print("----------------------------------------------")
                                            print("                 Terimakasih                  ")
                                            print("----------------------------------------------")
                                        ulangtiketsewa = input("Masukkan y untuk kembali : ")
                                        break
                                elif lanjut == "k" or lanjut == "K":
                                    stopsewa = "y"
                                    break
                                else:
                                    print("inputan salah")
                                    ulangweekdaysewa = "y"
# END KONDISI KEDUA WEEKEND Sewa Tenda
#END KONDISI B
#KEMBALI KE MENU AWAL
                    elif pilihtiketcamping=="c" or pilihtiketcamping=="C":
                        ngulang="y"
                        break
#END KEMBALI KE MENU AWAL
                    else:
                        stopsewa=input("Pilihan tidak ada apakah anda ingin mengulangi y/n : ")
#LOGOUT
            elif pilihtiket =="d" or pilihtiket=="D":
                ulangin="y"
                break
            else:
                ngulang=input("Pilihan tidak ada apakah anda ingin mengulangi y/n : ")
    else:
        print("\nPassword salah\n")
        ulangin=input("Apakah anda ingin login kembali y/n : ")