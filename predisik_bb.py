import numpy as np
from sklearn.linear_model import LinearRegression

# Data latihan
tinggi = np.array([[150], [160], [165], [170], [175], [180], [185], [190], [195]])
berat = np.array([45, 50, 55, 60, 65, 70, 75, 80, 85])

# Membuat model regresi linear
regressor = LinearRegression()
regressor.fit(tinggi, berat)

# Memasukkan tinggi yang akan diprediksi
tinggi_prediksi = np.array([[170], [175], [180]])

# Melakukan prediksi berat badan
berat_prediksi = regressor.predict(tinggi_prediksi)

# Menampilkan hasil prediksi
for i in range(len(tinggi_prediksi)):
    print("Tinggi:", tinggi_prediksi[i][0], "Prediksi Berat:", "{:.2f}".format(berat_prediksi[i]))

