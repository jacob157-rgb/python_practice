jam = int(input("Masukan Jam Sewa : "))
if jam > 3:
    tarif = 5000
    total = 3*6000+(jam-3)*tarif
else:
    tarif = 6000
    total = jam*tarif
print("Biaya Sewa selama", jam,"Jam yang harus Dibayar adalah : Rp.",total)