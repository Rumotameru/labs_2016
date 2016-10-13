import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


        #Здесь расписанны только несделанные пункты(начиная с 6ого)

random.seed(0)
  #Считываем данные в массив numpy
data = pd.read_csv("img.txt", sep = " ", header = None)
data = np.array(data)
#Создаём рандомные 100 строчек различными способами
top100 = random.choice(data)
random100 = np.array(random.sample(list(data), 100))
for i in range(99):
    top100 = np.vstack([top100, random.choice(data)])
  #Создаём графики строчек
plt.subplot(321)
plt.imshow(top100, cmap = plt.get_cmap('gray'))
plt.subplot(322)
plt.imshow(random100, cmap = plt.get_cmap('gray'))
  #Создаём графики необработанных данных
plt.subplot(323)
plt.imshow(data, cmap = plt.get_cmap('gray'))
plt.subplot(324)
plt.hist(data.flatten())
  #Эквализируем данные
for i in range(len(data)):
    percentiles = get_percentile(data[i], 4)
    if min(data[i]) > 0: 
        percentiles[0] = 0.0
    data[i] = values_equalization(data[i], percentiles, add_random = True)
plt.subplot(325)
plt.imshow(data, cmap = plt.get_cmap('gray'))
plt.subplot(326)
plt.hist(data.flatten()) 
plt.show()

data = data.flatten()
print(data.mean())
