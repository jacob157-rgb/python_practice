# Fungsi Segitiga
def triangle(n, char): #Mengambil nilai input "n" dan "char"
	
	# Jumlah Spasi
	k = n - 1 # k adalah n(nilai tinggi)-1 

	# Loop Baris yang mengatur banyaknya baris
	for i in range(0, n): #untuk i di jangkauan (0-n)
	
		# Loop Spasi yang mengatur spasi
		# Nilai berubah berdasarkan input
		for j in range(0, k): #untuk j di jangkauan (0-k)
			print(end=" ") #cetak spasi (Segitiga siku terbalik)
	
		k = k - 1 #mengurangi segitiga siku terbalik setiap loopnya
	
		# Loop yang mengatur kolom
		# Nilai berubah berdasarkan Loop Baris
		for j in range(0, i+1):
		
			# Mencetak Karakter yang diinputkan
			print(char,"", end="")
	
		# Penutup setiap baris
		print("\r")

# Driver Code
n = int(input("Masukan Tinggi : "))
char = str(input("Masukan Char : "))
triangle(n, char)