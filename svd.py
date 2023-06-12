import numpy as np

# Matriks input
A = np.array([[1, -1], [0, 1], [1, 0]])

# Mencari SVD
U, s, VT = np.linalg.svd(A)

# Menampilkan hasil
print("Matriks A:")
print(A)

print("Matriks U:")
print(U)

print("Matriks singular values (s):")
print(s)

print("Matriks VT:")
print(VT)
