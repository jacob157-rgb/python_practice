import os
import datetime as dt
import pyinputplus as pyip
tgl = dt.datetime.now()
no = []
mnl = []
hrgmnl = []
pbl = []
ttlpbl = []
tpl = []
hrtpgl = []
jtpgl = []
ttltpgl = []

def menu():
    '''Daftar Menu'''
    os.system('clear')
    print("-"*50)
    print(f"{'Seblak':^50}")
    print("-"*50)
    print(" Menu\t\t\t\t\t Harga")
    print("-"*50)
    print(" -Seblak Original\t\t\tRp.8000")
    print(" (Sayur, Makaroni, Kerupuk)")
    print(" -Seblak Seafood\t\t\tRp.10000")
    print(" (Sayur, Makaroni, Kerupuk, \n Stick Crab, Tofu, Dumpling, Chikua)")
    print("-"*50)   
def topping():
    '''Daftar Toping'''
    os.system('clear')
    print("-"*25)
    print(" Topping\t  Harga")
    print("-"*25)
    print(" 1.Ceker\t Rp.2000")
    print(" 2.Kikil\t Rp.2000")
    print(" 3.Sosis\t Rp.2000")
    print(" 4.Bakso\t Rp.2000")
    print(" 5.Sayap\t Rp.3000")
    print(" 6.Telur\t Rp.3000")
    print(" 7.Telur Puyuh\t Rp.3000")
    print(" 8.Tulangan\t Rp.4000")
    print("-"*25)
def printout(user):
    '''Printout'''
    print("-"*50)
    print(f"{'Seblak':^50}")
    print("-"*50)
    print("Kasir : ",user,  "Tgl Transaksi : ",tgl.strftime("%x"),tgl.strftime("%X"))
    print("-"*50)

loginlagi = 'yes'
while loginlagi == 'yes':
    user = 'admin'#pyip.inputStr("Username : ")
    password = 'admin'#pyip.inputPassword("Password : ")
    if user == "admin" and password == "admin":
        menu()
        jb = pyip.inputInt("Masukan Jumlah Beli : ", min=1)
        for i in range(jb):
            print("Pembelian Ke-",str(i+1))
            no.append(str(i+1))
            mn = pyip.inputChoice(['Original','Seafood'], prompt="Masukan Jenis Seblak (Original/Seafood) : ")
            if mn == 'Original':
                mnl.append(mn)
                hrgmn = 8000
                hrgmnl.append(hrgmn)
            elif mn == 'Seafood':
                mnl.append(mn)
                hrgmn = 10000
                hrgmnl.append(hrgmn)
            pb = pyip.inputInt("Masukan Jumlah Porsi : " ,min=1)
            pbl.append(pb)
            ttlpb = hrgmn*pb
            ttlpbl.append(ttlpb)
            ttpg = pyip.inputYesNo("Apakah anda ingin menambahkan topping(Y/N) : ")
            if ttpg == "yes":
                topping()
                tpg = pyip.inputInt("Masukan Jumlah Topping : ")
                tp = pyip.inputChoice(['1','2','3','4','5','6','7','8'], prompt="Masukan Topping : ")
                if tp == "1":
                    tpl.append('Ceker')
                    hrtpg = 2000
                    hrtpgl.append(hrtpg)
                    jtpg = int(input("Masukan Banyaknya Topping : "))
                    jtpgl.append(jtpg)
                    ttltpg = hrtpg*jtpg
                    ttltpgl.append(ttltpg)
                elif tp == "2":
                    tpl.append('Kikil')
                    hrtpg = 2000
                    hrtpgl.append(hrtpg)
                    jtpg = int(input("Masukan Banyaknya Topping : "))
                    jtpgl.append(jtpg)
                    ttltpg = hrtpg*jtpg
                    ttltpgl.append(ttltpg)
                elif tp == "3":
                    tpl.append('Sosis')
                    hrtpg = 2000
                    hrtpgl.append(hrtpg)
                    jtpg = int(input("Masukan Banyaknya Topping : "))
                    jtpgl.append(jtpg)
                    ttltpg = hrtpg*jtpg
                    ttltpgl.append(ttltpg)
                    lagi = pyip.inputYesNo("Tambah Topping Lagi(Y/N) : ")    
                elif tp == "4":
                    tpl.append('Bakso')
                    hrtpg = 2000
                    hrtpgl.append(hrtpg)
                    jtpg = int(input("Masukan Banyaknya Topping : "))
                    jtpgl.append(jtpg)
                    ttltpg = hrtpg*jtpg
                    ttltpgl.append(ttltpg)
                elif tp == "5":
                    tpl.append('Sayap')
                    hrtpg = 3000
                    hrtpgl.append(hrtpg)
                    jtpg = int(input("Masukan Banyaknya Topping : "))
                    jtpgl.append(jtpg)
                    ttltpg = hrtpg*jtpg
                    ttltpgl.append(ttltpg)
                elif tp == "6":
                    tpl.append('Telur')
                    hrtpg = 3000
                    hrtpgl.append(hrtpg)
                    jtpg = int(input("Masukan Banyaknya Topping : "))
                    jtpgl.append(jtpg)
                    ttltpg = hrtpg*jtpg
                    ttltpgl.append(ttltpg)
                elif tp == "7":
                    tpl.append('Telur Puyuh')
                    hrtpg = 3000
                    hrtpgl.append(hrtpg)
                    jtpg = int(input("Masukan Banyaknya Topping : "))
                    jtpgl.append(jtpg)
                    ttltpg = hrtpg*jtpg
                    ttltpgl.append(ttltpg)
                elif tp == "8":
                    tpl.append('Tulangan')
                    hrtpg = 4000
                    hrtpgl.append(hrtpg)
                    jtpg = int(input("Masukan Banyaknya Topping : "))
                    jtpgl.append(jtpg)
                    ttltpg = hrtpg*jtpg
                    ttltpgl.append(ttltpg)
        printout(user)
        for n in range(jb):
            print(" ",no[n],".",mnl[n],pbl[n],"*",hrgmnl[n],ttlpbl[n])
            for t in range(tpg):
                print("-",tpl[t],"*",jtpgl[t],"=",ttltpgl[t])
        uang = int(input)

    else:
        print("Username/Password yang anda masukan salah!")
        loginlagi = pyip.inputYesNo("Cobalagi? (Y/N) : ")            