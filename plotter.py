import pandas as pd
import matplotlib.pyplot as plt

# CSV Dosyasını Okuma ve Değişkenleri Tanımlama

data = pd.read_csv('data.csv').values
countryNames = []

years = [1950,1960,1970,1980,1990,2000,2010,2020]

# Verileri Gruplandırma Ve Grafiği Oluşturma

for i in range(data.size // 9):
    tempArray = []
    countryNames.append(data[i][0])
    for j in range(1,9):
        tempArray.append(data[i][j]/100)
    plt.plot(years,tempArray)

# Grafik Okunabilirliğini Arttırma Ve Grafiği Çizme

plt.legend(countryNames)
plt.xlabel('Yıllar')
plt.ylabel('Popülasyon')
plt.show()
    