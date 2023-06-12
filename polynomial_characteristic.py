import numpy as np


def polynomial_characteristic(matrix):
    return np.poly(matrix)


def eigen(matrix):
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    return eigenvalues, eigenvectors


def find_diagonal_matrix(matrix):
    eigenvalues, eigenvectors = eigen(matrix)
    P = eigenvectors
    P_inv = np.linalg.inv(P)
    diagonal_matrix = np.diag(eigenvalues)
    transformed_matrix = np.dot(P_inv, np.dot(matrix, P))
    return P, diagonal_matrix, transformed_matrix


# Contoh penggunaan program
matrix = np.array([[3, 1, 1], [-4, -2, -5], [2, 2, 5]])

# Hitung karakteristik polinomial
characteristic = polynomial_characteristic(matrix)
print("Karakteristik Polinomial:")
print(characteristic)

# Hitung eigenvalues dan eigenvectors
eigenvalues, eigenvectors = eigen(matrix)
print("Eigenvalues:")
print(eigenvalues)
print("Eigenvectors:")
print(eigenvectors)

# Cari matriks P untuk transformasi diagonalisasi
P, diagonal_matrix, transformed_matrix = find_diagonal_matrix(matrix)
print("Matriks P:")
print(P)
print("Matriks Diagonal:")
print(diagonal_matrix)
print("Transformasi Matriks:")
print(transformed_matrix)
