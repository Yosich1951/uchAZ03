"""
построить гистограмму по данным из processed_prices.csv
"""
import csv
import matplotlib.pyplot as plt

# Чтение данных из файла processed_prices.csv
prices = []
with open('processed_prices.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)  # Пропускаем заголовок
    for row in reader:
        prices.append(int(row[0]))

# Построение гистограммы
plt.figure(figsize=(10, 6))  # Настройка размера графика
plt.hist(prices, bins=10, edgecolor='black')  # Построение гистограммы с 10 корзинами
plt.title('Распределение цен на квартиры')
plt.xlabel('Цена ( млн ₽)')
plt.ylabel('Количество квартир')
plt.grid(True)

# Отображение гистограммы
plt.show()