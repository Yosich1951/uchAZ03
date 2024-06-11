"""
обработать данные, найти среднюю цену и вывести ее,
а также сделать гистограмму цен на диваны
"""
import matplotlib.pyplot as plt
import csv
import numpy as np
import pandas as pd


file_path = 'divan.csv'
# Чтение данных из файла prices.csv
with open(file_path, 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)  # Пропускаем заголовок
    prices = [row[1] for row in reader]
# print(prices)

# Преобразование данных: удаление "₽/мес." и преобразование в число
processed_prices = []
for price in prices:
    # Удаление "руб." и пробелов, затем преобразование в число
    processed_price = int(price.replace('руб.', '').replace(' ', '').strip())
    processed_prices.append(processed_price)

# конвертирование в массив
price_arr  = np.array(processed_prices)
# расчет среднего
arr_mean = price_arr.mean()
print(f"Средняя цена дивана: {int(arr_mean)} руб")

# альтернативный подход Цена
df_all = pd.read_csv(file_path)
# print(df_all.head())
df = df_all['Цена']
# print(df.head())
proc_prices = []
for row in df.values:
    # Удаление "руб." и пробелов, затем преобразование в число
    proc_price = int(row.replace('руб.', '').replace(' ', '').strip())
    proc_prices.append(proc_price)
column = 'Цена дивана, руб'
df_proc = pd.DataFrame(proc_prices, columns=[column])
# print(df_proc.head())
div_mean = df_proc[column].mean()
print(f"Средняя цена дивана: {int(div_mean)} руб")

# Построение гистограммы
plt.figure(figsize=(10, 6))  # Настройка размера графика
plt.hist(df_proc[column], bins=10, edgecolor='black')  # Построение гистограммы с 10 корзинами
plt.title('Распределение цен на диваны')
plt.xlabel(column)
plt.ylabel('Количество диванов')
plt.grid(True)
plt.show()
