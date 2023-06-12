def gauss_jordan_elimination(matrix, vector):
    n = len(matrix)

    # Menggabungkan matriks dan vektor menjadi augmented matrix
    augmented_matrix = [matrix[i] + [vector[i]] for i in range(n)]

    # Melakukan eliminasi Gauss-Jordan
    for i in range(n):
        # Pencarian baris dengan elemen terbesar di kolom i
        max_row = i
        for j in range(i + 1, n):
            if abs(augmented_matrix[j][i]) > abs(augmented_matrix[max_row][i]):
                max_row = j

        # Menukar baris teratas dengan baris dengan elemen terbesar
        augmented_matrix[i], augmented_matrix[max_row] = (
            augmented_matrix[max_row],
            augmented_matrix[i],
        )

        # Membuat elemen utama menjadi 1
        pivot = augmented_matrix[i][i]
        for j in range(i, n + 1):
            try:
                augmented_matrix[i][j] /= pivot
            except ZeroDivisionError:
                augmented_matrix[i][j] = 0

        # Mengeliminasi elemen-elemen di bawah dan di atas elemen utama
        for j in range(n):
            if j != i:
                factor = augmented_matrix[j][i]
                for k in range(i, n + 1):
                    augmented_matrix[j][k] -= factor * augmented_matrix[i][k]

    # Menghasilkan solusi
    solution = [augmented_matrix[i][n] for i in range(n)]
    return solution


# Input matriks dan vektor
matrix = [[3, 8, -3, -14], [2, 3, -1, -2], [1, -2, 1, 10], [1, 5, -2, -12]]
vector = [2, 1, 0, 1]

# Menyelesaikan sistem persamaan linier menggunakan metode eliminasi Gauss-Jordan
solution = gauss_jordan_elimination(matrix, vector)

# Menampilkan solusi
print("Solusi:")
for i in range(len(solution)):
    print("x{} = {}".format(i + 1, solution[i]))
