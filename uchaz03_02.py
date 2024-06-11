"""
Библиотека NumPy
"""
import numpy as np
import matplotlib.pyplot as plt

# массив
a = np.array([1, 2, 3, 4])
print(a)
#заполненный нулями
b = np.zeros((3, 3))
print(b)
# заполненный единицами
c = np.ones((2,5))
print(c)
# заполненный рандомными числами от 0 до 1
r = np.random.random((4, 5))
print(r)
# заполненный последовательностью чисел
ran = np.arange(0, 10,2)
print(ran)
# заполненный числами, равно распределёнными между друг другом
lin = np.linspace(0, 13, 10)
print(lin)

# Генерируем массив с диапазоном значений от -10 до 10,
# делаем между ними равное распределение
x = np.linspace(-10, 10, 100)
# Вычисляем значение данных:
y = x**2
# Создаём график:
plt.plot(x, y)
plt.xlabel("ось X")
plt.ylabel("ось Y")
plt.title("График функции y = x**2")
# Делаем сетку на фоне графика:
plt.grid(True)
plt.show()