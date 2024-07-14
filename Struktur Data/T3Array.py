# Array Dimensi Banyak
array_dimensi_banyak = [[0 for j in range(4)] for i in range(3)]
print("Array Dimensi Banyak :")
print(array_dimensi_banyak)

# Sparse Array
sparse_array = [[0 for j in range(4)] for i in range(3)]
sparse_array[0][1] = 1
sparse_array[1][2] = 1
sparse_array[2][3] = 1
print("Sparse Array :")
print(sparse_array)

print("Triangular Array")
# Triangular Array Atas
triangular_array_atas = [[0 for j in range(5)] for i in range(5)]
for i in range(5):
    for j in range(5):
        if i <= j:
            triangular_array_atas[i][j] = 1
print("UPPER : ")
print(triangular_array_atas)

# Triangular Array Bawah
triangular_array_bawah = [[0 for j in range(5)] for i in range(5)]
for i in range(5):
    for j in range(5):
        if i >= j:
            triangular_array_bawah[i][j] = 1
print("LOWER : ")
print(triangular_array_bawah)