"""
Построение диаграмм разных типов
matplotlib
"""
import matplotlib.pyplot as plt

x = [2, 6, 8, 14, 20]
y = [6, 4, 10, 12, 16]

# линейный график
# plt.plot(x, y)
# plt.title(' Пример простого линейного графика')
# plt.xlabel('ось x')
# plt.ylabel('ось y')

# гистограмма
# data = [5, 6, 7, 4, 6, 5, 7, 8, 9, 10, 11, 8, 9, 10, 7, 6, 5, 7, 8, 9, 10, 7, 6, 5]
# plt.hist(data, bins=3)
# plt.xlabel('часы сна')
# plt.ylabel('количество людей')
# plt.title('гистограмма количества часов сна')

# диграмма рассеяния
x = [1, 4, 6 ,7]
y = [3, 5, 8, 10]
plt.scatter(x, y)
plt.xlabel('ось x')
plt.ylabel('ось y')
plt.title('Тестовая диаграмма рассеяния')

plt.show()