import os #Mengimport library OS untuk clearscreen
import time #Mengimport Library time untuk delay
import random #Mengimport Library random untuk Merandom Kode
import pandas as pd #Mengimport Library panda sebagai "pd" untuk database
import datetime as dt #Mengimport Library datetime sebagai "dt" untuk tanggal dan waktu
import pyinputplus as pyip #Mengimport Library pyinputplus sebagai "pyip" untuk memudahkan input pilihan


def cetak(nama,nik,tanggalbrkt,asal,tujuan,jambrkt,jamtiba,kereta,kelas,gerbong,kursi,harga): #fungsi cetak sebagai pencetak transaksi
    '''Default Template Tiket'''
    print("="*55)
    print("Nama\t\t      : ",nama)
    print("NIK\t\t      : ",nik)
    print("Tanggal Keberangkatan : ",tanggalbrkt)
    print("Stasiun Asal\t      : ",asal)
    print("Stasiun Tujuan\t      : ", tujuan)
    print("Jam Keberangkatan     : ", jambrkt)
    print("Jam Tiba\t      : ", jamtiba)
    print("Jenis Kereta\t      : ",kereta)
    print("Kelas\t\t      : ",kelas)
    print("No.Tempat duduk       :  ",gerbong,"/",kursi,sep='')
    print("Total\t\t      :  Rp.", harga, sep='')
    print("="*55)
def printkode(tanggalbeli, jambeli, kodeunik): #fungsi cetak kode setelah pembelian dinyatakan berhasil
    '''Default Print kode setelah pembayaran'''
    print("Transaksi Berhasil pada ",tanggalbeli,"Pukul ",jambeli)
    print("Berikut kode unik yang dapat digunakan untuk refund tiket")
    print(kodeunik)    

datapenjualan = pd.DataFrame(  #membuat dataframe data penjualan dengan kolom yang sudah ditentukan
            columns=['Nama','NIK','Kode','Tanggal Pembelian','Jam Pembelian','Tanggal Keberangkatan','Stasiun Asal','Stasiun Tujuan','Jam Keberangkatan','Jam Tiba','Kereta','Kelas','Gerbong','Kursi','Total Pembayaran']
        )
datarefund = pd.DataFrame(   #membuat dataframe data refund dengan kolom yang sudah ditentukan 
            columns=['Nama','NIK','Kode','Tanggal Pembelian','Jam Pembelian','Tanggal Keberangkatan','Stasiun Asal','Stasiun Tujuan','Jam Keberangkatan','Jam Tiba','Kereta','Kelas','Gerbong','Kursi','Total Pembayaran','Alasan Refund','Total Refund']
        )
isContinue = "Y" #iscontinue = ya
while isContinue == "Y": #while loop ketika iscontinue == "Y" maka loop akan dijalankan
    os.system('cls') #Clear tampilan terminal saat program dijalankan
    print("Self Sevice KAI")
    menu = pyip.inputMenu(['Pembelian Tiket', 'Refund Tiket', 'CS'], prompt="Silahkan Pilih Menu dibawah :\n", lettered=False, numbered=True) #menampilkan menu menu utama, jika input diluar menu yang ditampilkan maka akan di hiraukan
    if menu == "Pembelian Tiket": #jika user memilih menu 1 (Pembelian Tiket)
        os.system('cls') #Clear terminal
        print("Selamat datang di menu Pembelian Tiket\nSilahkan lengkapi Data diri anda :\n") #Sambutan menu pembelian
        nama = pyip.inputStr("Nama : ") #input nama user
        nik = pyip.inputInt("NIK  : ") #input nik user
        os.system('cls') #clear terminal
        asal = "Tegal (TG)" #menginisalisasi asal = tegal
        tujuan = pyip.inputMenu(['Brebes (BB)','Pemalang (PML)','Pekalongan (PK)','Semarang (SMC)'], prompt="Silahkan Pilih Stasiun tujuan :\n", lettered=False, numbered=True) #menampilkan menu tujuan, jika input diluar menu yang ditampilkan maka akan dihiraukan
        if tujuan == "Brebes (BB)": #jika tujuan brebes maka
            kereta = ['Kamandaka'] #kereta hanya ada jenis kamandaka
            harga = 50000 #harga awal = 50000
            listjam = ['08:00 - 08:12 - (12m)', '13:30 - 13:42 - (12m)', '16:00 - 16:12 - (12m)'] #list jam menuju brebes yang nantinya akan dippanggil
        elif tujuan == "Pemalang (PML)": #tapi jika tujuan pemalang maka
            kereta = ['Kaligung'] #kereta menuju pemalahng hanya ada jenis kaligung
            harga = 75000 #harga awal = 75000
            listjam = ['08:00 - 08:23 - (23m)', '13:30 - 13:52 - (23m)', '16:00 - 16:23 - (23m)'] #list jam menuju pemalang yang nantinya akan dippanggil
        elif tujuan == "Pekalongan (PK)": #tapi jika tujuan pekalongan maka
            kereta = ['Kaligung','Jayabaya'] #kereta ada dua pilihan kaligung dan jayabaya yang nantinya akan di list
            harga = 100000 #harga awal = 100000
            listjam = ['08:00 - 08:52 - (52m)', '13:30 - 14:22 - (52m)', '16:00 - 16:52 - (52m)'] #list jam menuju pekalongan yang nantinya akan dippanggil
        elif tujuan == "Semarang (SMC)": #tapi jika tujuan semarang maka
            kereta = ['Kaligung','Jayabaya'] #kereta ada dua pilihan kaligung dan jayabaya yang nantinya akan di list
            harga = 125000 #harga awal = 125000
            listjam = ['08:00 - 10:12 - (2j12m)', '13:30 - 15:42 - (2j12m)', '16:00 - 18:12 - (2j12m)'] #list jam menuju semarang yang nantinya akan dippanggil
        os.system('cls') #clear terminal
        print("Tujuan dipilih",tujuan) #mencetak tujuan yang sudah dipilih
        tanggalbrkt = pyip.inputDate("Silahkan masukan tanggal Keberangkatan\n(hh/bb/tttt) : ",formats=['%d/%m/%Y']) #memasukan tanggal keberangkatan
        os.system('cls') #clear terminal
        kelas = pyip.inputMenu(['Ekonomi','Bisnis','Eksekutif'], prompt="Silahkan Pilih kelas :\n", lettered=False, numbered=True) #menampilkan menu kelas, jika input diluar menu yang ditampilkan maka akan dihiraukan
        if kelas == "Ekonomi": #jika kelas ekonomi dipilih
            harga += 0 #maka hargaawal + 0
            gerbong = "EKO" #kode gerbong = "EKO"
        elif kelas == "Bisnis": #tapi jika kelas bisnis dipilih
            harga += 15000 #maka hargaawal + 15000
            gerbong = "BIS" #kode gerbong = "BIS"
        elif kelas == "Eksekutif": #tapi jika kelas eksekutif dipilih
            harga += 30000 #maka hargaawal + 30000
            gerbong = "EKS" #kode gerbong = "EKS"
        kereta = random.choice(kereta) #merandom list kereta sesuai tujuan yang dipilih
        gerbong = gerbong+"-"+str(random.randint(1,12)) #menambahkan kode gerbong dan merandom angka dari 1-12
        kursi = str(random.randint(1,20))+random.choice(['A','B','C','D']) #merandom kursi dari angka 1-20 dan abjad ABCD
        os.system('cls') #clear terminal
        jam = pyip.inputMenu(listjam, prompt="Silahkan Pilih Jadwal Keberangkatan :\n", lettered=False, numbered=True) #menu jam keberangkatan menampilkan list jam sesuai dengan list jam tujuan
        jam = jam.split(" - ") #membagi list jam yang dipilih, dengan tanda "-" sebagai pemisah. contoh 08:00 - 10:12 - (2j12m) dipilih akan menjadi list ['08:00','10:12','(2j12m)'] #indexing dimulai dari 0
        jambrkt = jam[0] #jam berangkat adalah index ke [0] dari list jam yang sudah dipisah
        jamtiba = jam[1] #jam tiba adalah index ke [1] dari list jam yang sudah dipisah
        os.system('cls') #clear terminal
        cetak(nama,nik,tanggalbrkt,asal,tujuan,jambrkt,jamtiba,kereta,kelas,gerbong,kursi,harga) #memasukan semua variabel yang diisi ke dalam fungsi cetak guna menampilkan data data
        bayar = pyip.inputInt("Silahkan Masukan Jumlah Uang Anda : Rp.", min=harga) #meminta user menginput jumlah uang batas minimal dari harga jika yang dimasukan kurang dari jumlah harga maka akan dihiraukan
        kembali = bayar-harga  #kembali = jumlah bayar - total harga
        if kembali != 0: #jika kembali tidak bernilai 0 maka
            print("Kembali : Rp.", kembali, sep='') #cetak kembalian
        kode = "".join(nama.split())+str(nik) #kode adalah gabungan nama dan nik tanpa spasi
        kodeunik = str("".join(random.sample(kode, 10))) #kode unik adalah hasil random dari kode dengan panjang 10 karakter
        kodeunik = kodeunik.lower() #kode unik diformat menjadi lowercase (Huruf Kecil)
        tanggalbeli = dt.datetime.now().strftime("%x") #tanggal beli = datetime now dengan format yang ditampilkan hh/bb/tt
        jambeli = dt.datetime.now().strftime("%X") #jam beli = datetime now dengan format yang ditampilkan jj/mm/dd
        printkode(tanggalbeli,jambeli,kodeunik) #memasukan variabel tanggalbeli jambeli dan kodeunik untuk dicetak
        datapenjualan.loc[len(datapenjualan.index)] = [nama,nik,kodeunik,tanggalbeli,jambeli,tanggalbrkt,asal,tujuan,jambrkt,jamtiba,kereta,kelas,gerbong,kursi,harga] #memasukan semua hasil data penjualan ke dalam dataframe penjualan sesuai kolom yang sudah diinisialisasi di awal(line30)
        time.sleep(10) #menjeda program dari loop selama 10 detik
    elif menu == "Refund Tiket": #tapi jika yang dipilih menu refund
        os.system('cls') #clear terminal
        lkode = datapenjualan['Kode'].tolist() #membuat list kode unik diambil dari dataframe penjualan
        cari = pyip.inputChoice(lkode, prompt="Silahkan Masukan Kode Unik : ",blank=True) #mencari kode yang tersedia di dalam list kode, jika tidak tersedia maka akan dihiraukan
        hasil = datapenjualan.loc[datapenjualan['Kode']==cari] #mencari "kodeunik" di dalam dataframe 
        print(hasil) #mencetak baris data berdasarkan pencarian
        benar = pyip.inputYesNo("Apakah Data sudah benar(y/n)? ",yesVal='Y',noVal='N') #meminta user memastikan apakah data yang dicari sudah benar
        if benar == "Y": #jika benar maka
            alasan = str(input("Silahkan masukan alasan anda merefund tiket : ")) #user diminta memasukan alasan refund
            totalrefund = int((harga*75)/100) #dana yang direfund adalah 75% dari pembelian
            print("Dana yang di refund sebesar Rp.",totalrefund, sep='') #mencetak data yang di refund
            datarefund = pd.concat([hasil, datarefund]) #memasukan data penjualan yang direfund ke dataframe refund
            datapenjualan = datapenjualan.drop(hasil.index, inplace=False) #menghapus data penjualan yang sudah di refund jadi user tidak dapat merefund 2 kali
            datarefund['Alasan Refund'] = datarefund['Alasan Refund'].fillna(alasan) #memasukan alasan ke kolom "Alasan Refund" di dataframe refund
            datarefund['Total Refund'] = datarefund['Total Refund'].fillna(totalrefund) #memasukan jumlahrefund ke kolom "jumlah Refund" di dataframe refund
    elif menu == "CS": #tapi jika yang dipilih menu cs
        os.system('cls') #clear terminal
        luser = ['admin'] #list username admin dan masih bisa ditambahkan jika ada admin baru
        lpwd = ['admin'] #list password admin dan masih bisa ditambahkan jika ada admin baru
        print("Selamat datang di Costumer Service\nMohon Hubungi kontak kami apabila terjadi kendala.\n") #sambutan costumer service
        print("Office phone\t  : 022-4230031")
        print("Contact center\t  : (021) 121")
        print("Layanan Pelanggan : cs@kai.id\n")
        time.sleep(10) #delay selama 10 detik untuk menampilkan menu admin tersembunyi
        islogin = pyip.inputYesNo("Login Sebagai Admin(y/n)? ",yesVal='Y',noVal='N') #menampilkan pilihan login sebagai admin
        if islogin == "Y": #jika iya maka
            os.system('cls') #clear terminal
            user = pyip.inputChoice(luser, prompt="Silahkan Masukan Username : ",blank=True) #meminta admin memasukan username sesuai yang terdaftar pada list dan mengabaikan jika tidak tertera
            pwd = pyip.inputChoice(lpwd, prompt="Silahkan Masukan Password : ",blank=True) #meminta admin memasukan pasword sesuai yang terdaftar pada list dan mengabaikan jika tidak tertera
            if user in luser and pwd in lpwd: #jika username ada di list username dan password ada di list password maka login berhasil
                os.system('cls') #clear terminal
                print("Login Berhasil, Selamat datang",user) #login berhasil
                menuadmin = pyip.inputMenu(['Cetak Data Penjualan','Cetak Data Refund','Logout'], prompt="Silahkan Pilih menu :\n", lettered=False, numbered=True) #menampilkan menu admin
                if menuadmin == "Cetak Data Penjualan": #jika cetak data penjualan dipilih maka
                    print("Menyimpan data penjualan ke (datapenjualantiket.xlsx)") #menampilkan di terminal
                    datapenjualan.to_excel("datapenjualantiket.xlsx") #dan menyimpan data penjualan sebagai "datapenjualan.xlsx" di direktori yang sama seperti di program
                elif menuadmin == "Cetak Data Refund": #jika cetak data refund dipilih maka
                    print("Menyimpan data refund ke (datarefundtiket.xlsx)") #menampilkan di terminal
                    datarefund.to_excel("datarefundtiket.xlsx") #dan menyimpan data refund sebagai "datarefund.xlsx" di direktori yang sama seperti di program
                elif menuadmin == "Logout": #jika logout dipilih maka
                    break #menghentikan loop
        isContinue = pyip.inputYesNo("Transaksi Lagi(y/n)? ",yesVal='Y',noVal='N') #mengkonfirmasi apakah ingin transaksi lagi
        if isContinue == "N": #jika tidak maka
            os.system('cls') #clear terminal
            break #menghentikan loop while