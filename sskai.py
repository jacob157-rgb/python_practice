import os
import datetime as dt
import pyinputplus as pyip
import pandas as pd
import random as rd
def header_program(): #Header Program
    '''Header Program'''
    print("="*55)
    print(f"{'Program Self Service KAI':^55}")
    print("="*55)
def Daftar_menu1(): #Daftar menu Utama
    '''Daftar menu1'''
    os.system('clear')
    print("="*55)
    print(f"{'Selamat Datang di Self Service KAI':^55}")
    print("="*55)
    print("{:<55}".format("Silahkan Pilih Menu di bawah\n1. Pembelian Tiket\n2. Refund Tiket\n3. Costumer Service"))
def menu_beli(): #Daftar menu Pembelian
    '''Menu Pembelian Tiket'''
    os.system('clear')
    print("="*55)
    print(f"{'Selamat Datang di Menu Pembelian Tiket':^55}")
    print("="*55)
def stasiun_tujuan():
    '''Daftar Stasiun Tujuan'''
    os.system('clear')
    print("Daftar Stasiun Tujuan :")
    print("1. Brebes\n2. Pemalang\n3. Pekalongan\n4. Semarang")
def kelas():
    '''Kelas Kereta'''
    os.system('clear')
    print("Kelas Kereta :")
    print("1. Ekonomi\n2. Bisnis\n3. Eksekutif")
def jam():
    '''Daftar'''
    os.system('clear')
    print("Daftar Jam Keberangkatan :")
    print("1. 08:00\n2. 13:30\n3. 16:00")
def print_out(nama, nik, tanggal, stasiuntj, jamk, jamtiba, kelask, gerbong, kursi, total):
    '''Default Template Tiket'''
    print("="*55)
    print("Nama\t\t      : ",nama)
    print("NIK\t\t      : ",nik)
    print("Kodeunik\t      : ",kode)
    print("Tanggal Keberangkatan : ",tanggal)
    print("Stasiun Asal\t      :  Tegal(TG)")
    print("Stasiun Tujuan\t      : ", stasiuntj)
    print("Jam Keberangkatan     : ", jamk)
    print("Jam Tiba\t      : ", jamtiba)
    print("Kelas\t\t      : ",kelask)
    print("No.Tempat duduk       :  ",gerbong,"/",kursi,sep='')
    print("Total\t\t      :  Rp.", total, sep='')
    print("="*55)
def printkode(tanggalbeli, jambeli, kode):
    '''Default Print kode setelah pembayaran'''
    print("Transaksi Berhasil pada ",tanggalbeli,"Pukul ",jambeli)
    print("berikut kode unik yang dapat digunakan untuk refund tiket")
    print(kode)
def menu_refund(): #Daftar menu Refund
    '''Menu Refund Tiket'''
    os.system('clear')
    print("="*55)
    print(f"{'Selamat Datang di Menu Refund Tiket':^55}")
    print("="*55)
    print("Panduan refund tiket kereta:")
    print("1. Masukan kode unik tiket yang ingin di refund")
    print("2. Cek apakah data yang sudah benar")
    print("3. Dana yang di refund adalah 75% Total Pembelian")
    print("")
    print("Terimakasih!")
def cs(): #Info Customer Service
    '''Costumer Service'''
    os.system('clear')
    print("Mohon Hubungi kontak kami apabila ada kendala.")
    print("="*55)
    print("Office phone\t  : 022-4230031")
    print("Contact center\t  : (021) 121")
    print("Layanan Pelanggan : cs@kai.id")
    print("="*55)
def thx(): #Ucapan Terimakasih
    print("Terimakasih telah menggunakan Self Service\nDengan menggunakan Self Service anda telah\nmembantu menghambat penyebaran Virus Covid-19")
#Program Utama
df = pd.DataFrame(
        columns=['Nama', 'NIK', 'Tanggal Pembelian', 'Jam Pembelian', 'Tanggal Keberangkatan', 'Stasiun Tujuan', 'Jam Keberangkatan', 'Jam Tiba', 'Kelas Kereta', 'Gerbong', 'Kursi', 'Total Pembelian', 'Kode']
    )
df1 = pd.DataFrame(
        columns=['Nama', 'NIK', 'Tanggal Pembelian', 'Jam Pembelian', 'Tanggal Keberangkatan', 'Stasiun Tujuan', 'Jam Keberangkatan', 'Jam Tiba', 'Kelas Kereta', 'Gerbong', 'Kursi', 'Total Pembelian', 'Kode', 'Alasan', 'Total Refund']
    )
isContinue = "Y"
while isContinue == "Y":
    os.system('clear')
    x = dt.datetime.now()
    header_program()
    mulai = pyip.inputChoice(['Y','N'], prompt="Apakah anda ingin melakukan Self Service KAI(y/n) : ")
    if mulai =="Y":
        Daftar_menu1()
        pilih_menu1 = pyip.inputChoice(['1','2','3'], prompt="Silahkan Pilih Menu Diatas : ")
        if pilih_menu1 == 1: #Memilih Menu 1 (Menu Beli)
            menu_beli()
            nama = input("Silahkan Masukan Nama Anda : ") #Input Nama
            nik = pyip.inputInt("Silahkan Masukan NIK Anda  : ") #Input NIK
            ku = nama+str(nik)
            leng = 10
            kode = str("".join(rd.sample(ku, leng)))
            tanggalbeli = x.strftime("%x")
            jambeli = x.strftime("%X")
            stasiun_tujuan() #Menampilkan daftar stasiun Tujuan
            pilih_stasiun_tujuan = pyip.inputChoice(['1','2','3','4'], prompt="Silahkan Pilih Menu Diatas : ")
            if pilih_stasiun_tujuan == 1: #Memilih Stasiun 1 (Brebes)  
                tanggal = pyip.inputDate("Tanggal keberangkatan (hh/bb/tttt) : ")
                stasiuntj = "Brebes(BMA)"
                kelas()
                kelask = pyip.inputChoice(['1','2','3'], prompt="Silahkan Pilih Menu Diatas : ")
                if kelask == 1:
                    kelask = "Ekonomi"
                    harga = 50000
                    gerbong = "EKO-1"
                    kursi = "2A"
                elif kelask == 2:
                    kelask = "Bisnis"
                    harga = 65000
                    gerbong = "BIS-1"
                    kursi = "1A"
                elif kelask == 3:
                    kelask = "Eksekutif"
                    harga = 80000
                    gerbong = "EKS-1"
                    kursi = "4D"
                jam()
                jamk = pyip.inputChoice(['1','2','3'], prompt="Silahkan Pilih Menu Diatas : ")
                if jamk == 1:
                    jamk = "08:00"
                    jamtiba = "09:30"
                elif jamk == 2:
                    jamk = "13:30"
                    jamtiba = "15:00"
                elif jamk == 3:
                    jamk = "16:00"
                    jamtiba = "17:30"
                os.system('clear')
                total = harga
                print_out(nama, nik, tanggal, stasiuntj, jamk, jamtiba, kelask, gerbong, kursi, total)
                uangbayar = pyip.inputInt("Silahkan Masukan Jumlah Uang Anda : Rp.", min=total)
                kembali = uangbayar-total
                print("Kembali : Rp.", kembali, sep='')
                printkode(tanggalbeli,jambeli,kode)
                df.loc[len(df.index)] = [nama, nik, tanggalbeli, jambeli, tanggal, stasiuntj, jamk, jamtiba, kelask, gerbong, kursi, total, kode]
                thx()
            elif pilih_stasiun_tujuan == 2: #Memilih Stasiun 2 (Pemalang)
                tanggal = input("Tanggal keberangkatan (hh/bb/tttt) : ")
                stasiuntj = "Pemalang(PML)"
                kelas()
                kelask = pyip.inputChoice(['1','2','3'], prompt="Silahkan Pilih Menu Diatas : ")
                if kelask == 1:
                    kelask = "Ekonomi"
                    harga = 75000
                    gerbong = "EKO-2"
                    kursi = "4A"
                elif kelask == 2:
                    kelask = "Bisnis"
                    harga = 90000
                    gerbong = "BIS-2"
                    kursi = "2B"
                elif kelask == 3:
                    kelask = "Eksekutif"
                    harga = 105000
                    gerbong = "EKS-2"
                    kursi = "3C"
                jam()
                jamk = pyip.inputChoice(['1','2','3'], prompt="Silahkan Pilih Menu Diatas : ")
                if jamk == 1:
                    jamk = "08:00"
                    jamtiba = "09:30"
                elif jamk == 2:
                    jamk = "13:30"
                    jamtiba = "15:00"
                elif jamk == 3:
                    jamk = "16:00"
                    jamtiba = "17:30"
                os.system('clear')
                total = harga
                print_out(nama, nik, tanggal, stasiuntj, jamk, jamtiba, kelask, gerbong, kursi, total)
                uangbayar = pyip.inputInt("Silahkan Masukan Jumlah Uang Anda : Rp.", min=total)
                kembali = uangbayar-total
                print("Kembali : Rp.", kembali, sep='')
                printkode(tanggalbeli,jambeli,kode)
                df.loc[len(df.index)] = [nama, nik, tanggalbeli, jambeli, tanggal, stasiuntj, jamk, jamtiba, kelask, gerbong, kursi, total, kode]
                thx()
            elif pilih_stasiun_tujuan == 3: #Memilih Stasiun 3 (Pekalongan)
                tanggal = input("Tanggal keberangkatan (hh/bb/tttt) : ")
                stasiuntj = "Pekalongan(PK)"
                kelas()
                kelask = pyip.inputChoice(['1','2','3'], prompt="Silahkan Pilih Menu Diatas : ")
                if kelask == 1:
                    kelask = "Ekonomi"
                    harga = 100000
                    gerbong = "EKO-3"
                    kursi = "2D"
                elif kelask == 2:
                    kelask = "Bisnis"
                    harga = 115000
                    gerbong = "BIS-3"
                    kursi = "3D"
                elif kelask == 3:
                    kelask = "Eksekutif"
                    harga = 130000
                    gerbong = "EKS-3"
                    kursi = "3A"
                jam()
                jamk = pyip.inputChoice(['1','2','3'], prompt="Silahkan Pilih Menu Diatas : ")
                if jamk == 1:
                    jamk = "08:00"
                    jamtiba = "09:30"
                elif jamk == 2:
                    jamk = "13:30"
                    jamtiba = "15:00"
                elif jamk == 3:
                    jamk = "16:00"
                    jamtiba = "17:30"
                os.system('clear')
                total = harga
                print_out(nama, nik, tanggal, stasiuntj, jamk, jamtiba, kelask, gerbong, kursi, total)
                uangbayar = pyip.inputInt("Silahkan Masukan Jumlah Uang Anda : Rp.", min=total)
                kembali = uangbayar-total
                print("Kembali : Rp.", kembali, sep='')
                printkode(tanggalbeli,jambeli,kode)
                df.loc[len(df.index)] = [nama, nik, tanggalbeli, jambeli, tanggal, stasiuntj, jamk, jamtiba, kelask, gerbong, kursi, total, kode]
                thx()
            elif pilih_stasiun_tujuan == 4: #Memilih Stasiun 4 (Semarang)
                tanggal = input("Tanggal keberangkatan (hh/bb/tttt) : ")
                stasiuntj = "Semarang(SMC)"
                kelas()
                kelask = pyip.inputChoice(['1','2','3'], prompt="Silahkan Pilih Menu Diatas : ")
                if kelask == 1:
                    kelask = "Ekonomi"
                    harga = 125000
                    gerbong = "EKO-4"
                    kursi = "2A"
                elif kelask == 2:
                    kelask = "Bisnis"
                    harga = 135000
                    gerbong = "BIS-4"
                    kursi = "3C"
                elif kelask == 3:
                    kelask = "Eksekutif"
                    harga = 155000
                    gerbong = "EKS-4"
                    kursi = "4B"
                jam()
                jamk = pyip.inputChoice(['1','2','3'], prompt="Silahkan Pilih Menu Diatas : ")
                if jamk == 1:
                    jamk = "08:00"
                    jamtiba = "09:30"
                elif jamk == 2:
                    jamk = "13:30"
                    jamtiba = "15:00"
                elif jamk == 3:
                    jamk = "16:00"
                    jamtiba = "17:30"
                os.system('clear')
                total = harga
                print_out(nama, nik, tanggal, stasiuntj, jamk, jamtiba, kelask, gerbong, kursi, total)
                uangbayar = pyip.inputInt("Silahkan Masukan Jumlah Uang Anda : Rp.", min=total)
                kembali = uangbayar-total
                print("Kembali : Rp.", kembali, sep='')
                printkode(tanggalbeli,jambeli,kode)
                df.loc[len(df.index)] = [nama, nik, tanggalbeli, jambeli, tanggal, stasiuntj, jamk, jamtiba, kelask, gerbong, kursi, total, kode]
                thx()
        elif pilih_menu1 == 2:
            menu_refund()
            lkode = df['Kode'].tolist()
            cari = pyip.inputChoice(lkode, prompt="Silahkan Masukan Kode Unik :")
            hasil = df.loc[df1['Kode']==cari]
            print(hasil)
            benar = pyip.inputChoice(['Y','N'], prompt="Apakah Data sudah benar(y/n)?")
            if benar == "Y":
                alasan = str(input("Silahkan masukan alasan anda merefund tiket : "))
                totalrefund = (total*75)/100
                print("Dana yang di refund sebesar Rp.",totalrefund, sep='')
                df1 = pd.concat([hasil, df1])
                df1 = df1.loc[len(df.index)] = [alasan, totalrefund]
        elif pilih_menu1 == 3:
            cs()
    elif mulai == "N":
        quit()
    isContinue = pyip.inputChoice(['Y','N'], prompt="Transaksi Lagi(y/n)?")
    if isContinue == "N":
        os.system('clear')
        thx()
        break
print(df)
print(df1)