import numpy as np

# Menggunakan library numpy untuk menyelesaikan sistem persamaan linier

# Masukkan koefisien matriks A
A = np.array(
    [
        [1, 3, -1, -1],
        [2, 5, -7, -5],
        [2, -1, 1, 3],
        [5, 2, -4, 2],
    ]
)

# Masukkan matriks kolom B
B = np.array([[1], [-2], [4], [6]])

# Menggunakan fungsi solve dari numpy untuk menyelesaikan sistem persamaan
# X adalah matriks kolom solusi
X = np.linalg.solve(A, B)

# Cetak solusi
print("Solusi dari sistem persamaan:")
print(X)
