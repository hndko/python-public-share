import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# Data harga rumah dari 2019 sampai 2023
tahun = np.array([2019, 2020, 2021, 2022, 2023])
harga_rumah = np.array([250, 275, 300, 320, 350])

# Mengubah bentuk array tahun menjadi matriks 2 dimensi
X = tahun[:, np.newaxis]

# Membuat model regresi linear
model = LinearRegression()

# Melatih model menggunakan data
model.fit(X, harga_rumah)

# Memprediksi harga rumah dari 2019 sampai 2023
tahun_prediksi = np.array([2019, 2020, 2021, 2022, 2023])
X_prediksi = tahun_prediksi[:, np.newaxis]
harga_prediksi = model.predict(X_prediksi)

# Menampilkan hasil prediksi
for tahun, harga in zip(tahun_prediksi, harga_prediksi):
    print(f"Prediksi harga rumah untuk tahun {tahun}: ${harga:.2f} ribu")

# Menampilkan plot data asli dan prediksi
plt.scatter(tahun, harga_rumah, color="red", label="Data Asli")
plt.plot(tahun_prediksi, harga_prediksi, color="blue", label="Prediksi")
plt.title("Prediksi Harga Rumah")
plt.xlabel("Tahun")
plt.ylabel("Harga Rumah (ribu $)")
plt.legend()
plt.show()
