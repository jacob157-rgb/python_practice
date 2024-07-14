#Program Hitung Gaji Karyawan
pokok = 300000
print("="*70)
print(f"{'Program Hitung Gaji Karyawan':^70}")
print("="*70)
nama = input("Masukan Nama Karyawan\t\t  : ")
golongan = int(input("Masukan Golongan Jabatan (1|2|3)  : "))
if golongan == 1:
    tunjanganjb = (5*pokok)/100
elif golongan == 2:
    tunjanganjb = (10*pokok)/100
elif golongan == 3:
    tunjanganjb = (15*pokok)/100
pendidikan = input("Masukan Pendidikan (SMK|D1|D3|S1) : ")
if pendidikan == "SMK" or pendidikan == "smk":
    tunjanganp = (2.5*pokok)/100
elif pendidikan == "D1" or pendidikan == "d1":
    tunjanganp = (5*pokok)/100
elif pendidikan == "D3" or pendidikan == "d3":
    tunjanganp = (20*pokok)/100
elif pendidikan == "S1" or pendidikan == "s1":
    tunjanganp = (30*pokok)/100
jumlahjk = int(input("Masukan Jumlah Jam Kerja\t  : "))
if jumlahjk > 8:
    lembur = (jumlahjk-8)*3500
else:
    lembur = 0
totalgaji = pokok+tunjanganjb+tunjanganp+lembur
print("="*70)
print("Karyawan yang bernama : ",nama)
print("Honor yang diterima   :")
print(f"{'Gaji Pokok':<50}", f"{'Rp.':>1}",pokok)
print(f"{'Tunjangan Jabatan':<50}", f"{'Rp.':>1}",tunjanganjb)
print(f"{'Tunjangan Pendidikan':<50}", f"{'Rp.':>1}",tunjanganp)
print(f"{'Honor Lembur':<50}", f"{'Rp.':>1}",lembur)
print(f"{'+':>70}")
print("-"*70)
print(f"{'Total Gaji (Pokok+Tunjangan+Lembur)':<50}", f"{'Rp.':>1}",totalgaji)