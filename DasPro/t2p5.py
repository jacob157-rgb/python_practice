import os
import pyinputplus as pyip
no = [] # List Nomor
jp = [] # List Jenis Potong
hs = [] # List Harga Satuan
bp = [] # List Banyak Potong/Banyak Beli
jh = [] # List Jumlah harga
def menu(): # Fungsi Menu
    '''menu pembelian'''
    os.system('clear')
    print("-"*45)
    print(f"{'GEROBAK FRIED CHICKEN':^45}")
    print("-"*45)
    print("Kode\t       Jenis Potong\t      Harga")
    print("-"*45)
    print(" D\t\tDada\t\t     Rp.2500")
    print(" P\t\tPaha\t\t     Rp.2000")
    print(" S\t\tSayap\t\t     Rp.1500")
    print("-"*45)   
def printout():
    '''menu printout'''
    os.system('clear')
    print("-"*45)
    print(f"{'GEROBAK FRIED CHICKEN':^45}")
    print("-"*45)
    print("No.     Jenis    Harga\t  Banyak   Jumlah\n        Potong   Satuan\t  Beli\t   Harga")
    print("-"*45)
# Main Program
lanjut = "Y"
while lanjut == "Y":
    menu() #Memanggil fungsi menu
    bj = pyip.inputInt("Banyak Jenis (max 3) : ", min=1, max=3) #Maksimal jenis = 3 berdasarkan menu
    if bj <= 3: #Jika True maka akan mengeksekusi for
        for i in range(bj):
            print("Jenis Ke -",str(i+1))
            no.append(str(i+1)) #Input No ke List Nomor
            kp = pyip.inputChoice(['D','P','S'], prompt='Kode Potong (D|P|S) : ')
            if kp == "D": # Jika Memilih D (dada)
                jptg = "Dada" #Jenis Potong
                jp.append(jptg) #Jenis Potong diinput ke list jp(Jenis Potong)
                hstn = 2500 #Harga Satuan
                hs.append(hstn) #Harga Satuan diinput ke list hs(Harga Satuan)
                bptg = int(input("Banyak Potong : ")) #Input Banyak Potong
                bp.append(bptg) #Banyak Potong diinput ke list bp(Banyak Potong/Banyak Beli)
                jhrg = hstn*bptg #Jumlah Harga = Harga Satuan * Banyak Potong
                jh.append(jhrg) #Jumlah Harga diinput ke list jh(Jumlah Harga)
            elif kp == "P": # Jika Memilih P (paha)
                jptg = "Paha" #Jenis Potong
                jp.append(jptg) #Jenis Potong diinput ke list jp(Jenis Potong)
                hstn = 2000 #Harga Satuan
                hs.append(hstn) #Harga Satuan diinput ke list hs(Harga Satuan)
                bptg = int(input("Banyak Potong : ")) #Input Banyak Potong
                bp.append(bptg) #Banyak Potong diinput ke list bp(Banyak Potong/Banyak Beli)
                jhrg = hstn*bptg #Jumlah Harga = Harga Satuan * Banyak Potong
                jh.append(jhrg) #Jumlah Harga diinput ke list jh(Jumlah Harga)
            elif kp == "S": # Jika Memilih S (sayap)
                jptg = "Sayap" #Jenis Potong
                jp.append(jptg) #Jenis Potong diinput ke list jp(Jenis Potong)
                hstn = 1500 #Harga Satuan
                hs.append(hstn) #Harga Satuan diinput ke list hs(Harga Satuan)
                bptg = int(input("Banyak Potong : ")) #Input Banyak Potong
                bp.append(bptg) #Banyak Potong diinput ke list bp(Banyak Potong/Banyak Beli)
                jhrg = hstn*bptg #Jumlah Harga = Harga Satuan * Banyak Potong
                jh.append(jhrg) #Jumlah Harga diinput ke list jh(Jumlah Harga)
            i += 1 
        printout()
        for n in range(bj):
            print(" ",no[n],".\t", jp[n],"\t Rp.",hs[n],"   ",bp[n],"\t   Rp.",jh[n],sep='')
        print("-"*45)
        jb = sum(jh)
        pj = (10*jb)/100
        tb = jb + pj
        print("\t\t  Jumlah Bayar : Rp.",jb,sep='')
        print("\t\t  Pajak 10%    : Rp.",pj,sep='')
        print("\t\t  Total Bayar  : Rp.",tb,sep='')
        ud = pyip.inputInt("\t\t  Masukan Uang : Rp.", min=tb)
        uk = ud-tb
        print("\t\t      Kembali  : Rp.",uk,sep='')
    else: #Else
        print("Banyak Jenis yang dimasukan melebihi Banyak Jenis yang tertera pada Menu") 
    lanjut = pyip.inputChoice(['Y','N'], prompt='Transaksi Lagi? (Y/N) : ')
    if lanjut == "N":
        break