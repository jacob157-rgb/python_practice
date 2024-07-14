#list_nim = []
#list_uts = []
#list_uas = []
#list_total = []
#
#ulang = 2
#for i in range(ulang):
#    print("Data Ke-",str(i+1))
#    list_nim.append(str(input("Masukan NIM Anda : ")))
#    list_uts.append(int(input("Masukan Nilai UTS Anda : ")))
#    list_uas.append(int(input("Masukan Nilai UAS Anda : ")))
#for i in range(ulang):
#    list_total.append((list_uas[i] + list_uts[i]) / 2)
#print("="*50)
#print(" NIM\t    Nilai UTS\t Nilai UAS\tTotal")
#print("="*50)
#for i in range(ulang):
#    print("%s \t%i\t    %i\t\t%i"%(list_nim[i],list_uts[i],list_uas[i],list_total[i]))
#print("="*50)


angka = [1,2,3,4,5,6,7,8,9,10]
ganjil = []
genap = []
for i in angka:
    j = i%2
    if j == 0:
        print("Angka ",i,"Adalah Genap")
        genap.append(i)
    else:
        print("Angka ",i,"Adalah Ganjil")
        ganjil.append(i)
print(ganjil)
print(genap)
        
angka = {1:30,2:60,3:90,4:120}
if (2) in angka:
    print("Tersedia")
else:
    print("Tidak Tersedia")