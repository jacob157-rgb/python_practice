import random

nama = "Jacob"
nik = 12221362

kode = nama+str(nik)
leng = 10
kodeunik = str("".join(random.sample(kode, leng)))
print(kodeunik)
kodekinu = random.sample(kodeunik, leng)
print(kodekinu)