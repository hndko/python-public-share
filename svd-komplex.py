import numpy as np

# Matriks koefisien
A = np.array(
    [
        [1j, 0, -1, 0, 1],
        [1, 1, -1j, 0, 0],
        [2, 0, -5j, 0, 0],
        [0, 2j, 2, 0, 0],
        [0, 0, 0, 1, 1],
        [1j, 1j, 0, 0, 0],
    ]
)

# Vektor hasil
b = np.array([3, 4j, -3j, -5, 5, -3j])

# Memecahkan persamaan menggunakan SVD
U, s, V = np.linalg.svd(A, full_matrices=False)
x = np.dot(V.T, np.dot(np.diag(1 / s), np.dot(U.T, b)))

# Menampilkan solusi
print("Solusi sistem persamaan linear:")
for i, sol in enumerate(x):
    print(f"x{i+1} = {sol}")
