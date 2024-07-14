import os
import pyinputplus as pyip
def header():
    '''Header Dari Program Hitung Gaji'''
    print("="*50)
    print(f"{'|':<0}{'Program Hitung Gaji':^48}{'|':>0}")
    print("="*50)
def printout(nama,gp,lembur,jk,lm,totalgaji,gajiakhir):
    '''Prinout Gaji'''
    print("Nama\t\t         :",nama)
    print("Gaji Pokok\t         : Rp.",gp,sep='')
    print("Gaji Lembur (Jam)        : Rp.",lembur,sep='')
    print("Jam Kerja\t         :",jk,"Jam")
    print("Jam Lembur\t         :",jk-8,"Jam")
    print("Hasil Lembur\t         : Rp.",lm,sep='')
    print("Total Gaji\t         : Rp.",int(totalgaji),sep='')
    print('Gaji setelah Pajak',' 10%','   : Rp.',int(gajiakhir),sep='')
    print("="*50)
lanjut = 'Y'
while lanjut == 'Y':
    os.system('clear')
    header()
    nama = str(input("Masukan Nama Karyawan\t         : "))
    gp = int(input("Masukan Jumlah Gaji Pokok        : Rp.")) ##input gaji pokok user
    lembur = int(input("Masukan Jumlah Gaji Lembur (Jam) : Rp."))
    jtjg = int(input("Masukan Tunjangan anda (%)       : "))
    tjg = (jtjg*gp)/100 #tunjangan adalah 20% dari gaji pokok
    jk = int(input("Masukan Jumlah Jam Kerja (Jam)   : ")) #input jam kerja untuk menghitung hasil lembur
    os.system('clear')
    if jk > 8: #jika jam kerja lebih dari 8 jam
        lm = (jk-8)*lembur #hasil lembur adalah jumlah lebih jam kerja * 20000
    else: #jika tidak memenuhi maka
        lm = 0 #tidak ada hasil lembur
    totalgaji = gp+tjg+lm #total gaji = gaji pokok+tunjangan+hasil lembur
    pajak = (10*totalgaji)/100 #pajak 10% dari total gaji
    gajiakhir = totalgaji-pajak #gaji akhir adalah total gaji - pajak10%
    header()
    printout(nama,gp,lembur,jk,lm,totalgaji,gajiakhir)
    lanjut = pyip.inputYesNo(prompt="Hitung Gaji Lagi (Y/N) : ", yesVal='Y',noVal='N')