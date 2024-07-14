def kecepatan(jarak,waktu):
    '''Fungsi Mencari Kecepatan'''
    kecepatan = jarak/waktu
    print("-Fungsi Mencari Kecepatan")
    print("Jarak =",jarak,"Km")
    print("Waktu =",waktu,"Jam")
    print("Kecepatan = Jarak * Waktu")
    print("Kecepatan =",kecepatan,"Km/Jam")
def jarak(kecepatan,waktu):
    '''Fungsi Mencari Jarak'''
    jarak = kecepatan*waktu
    print("-Fungsi Mencari Jarak")
    print("Kecepatan =",kecepatan,"Km/Jam")
    print("Waktu =",waktu,"Jam")
    print("Jarak = Kecepatan * Waktu")
    print("Jarak =",jarak,"Km")
def waktu(jarak,kecepatan):
    '''Fungsi Mencari Waktu'''
    waktu = jarak/kecepatan
    print("-Fungsi Mencari Waktu")
    print("Jarak =",jarak,"Km")
    print("Kecepatan =",kecepatan,"Km/Jam")
    print("Waktu = Jarak / Kecepatan")
    print("Waktu =",waktu,"Jam")
    
kecepatan(10,1)
jarak(10,2)
waktu(10,10)