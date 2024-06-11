"""
Построй диаграмму рассеяния для двух наборов случайных данных,
сгенерированных с помощью функции `numpy.random.rand`
import numpy as np
random_array = np.random.rand(5) # массив из 5 случайных чисел
print(random_array)
"""
import numpy as np
import matplotlib.pyplot as plt

# Генерация двух наборов случайных данных
num_samples = 5
random_array1 = np.random.rand(num_samples)
random_array2 = np.random.rand(num_samples)

# Построение диаграммы рассеяния
plt.scatter(random_array1, random_array2)

# Добавление заголовков и меток осей
plt.title("Диаграмма рассеяния для двух наборов случайных данных")
plt.xlabel("Набор данных 1")
plt.ylabel("Набор данных 2")
plt.grid(True)

# Отображение диаграммы рассеяния
plt.show()