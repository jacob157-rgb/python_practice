import numpy as np

# Array Dimensi Banyak
array_banyak = np.zeros((3, 4))
print("Array Dimensi Banyak:")
print(array_banyak)

# Sparse Array
sparse_array = np.zeros((3, 4))
sparse_array[0, 1] = 1
sparse_array[1, 2] = 1
sparse_array[2, 3] = 1
print("Sparse Array:")
print(sparse_array)

# Triangular Array Atas
triangular_array_bawah = np.zeros((5, 5))
triangular_array_bawah[np.tril_indices(5)] = 1
print("Triangular Array Bawah:")
print(triangular_array_bawah)

# Triangular Down Array
triangular_array_atas = np.zeros((5, 5))
triangular_array_atas[np.triu_indices(5)] = 1
print("Triangular Array Atas:")
print(triangular_array_atas)