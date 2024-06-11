"""
Обработка файла prices/csv
"""
import csv

# Чтение данных из файла prices.csv
with open('prices.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)  # Пропускаем заголовок
    prices = [row[0] for row in reader]

# Преобразование данных: удаление "₽/мес." и преобразование в число
processed_prices = []
for price in prices:
    # Удаление "₽/мес." и пробелов, затем преобразование в число
    processed_price = int(price.replace('₽/мес.', '').replace(' ', '').strip())
    processed_prices.append(processed_price)

# Запись преобразованных данных в новый CSV файл
with open('processed_prices.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Price'])  # Запись заголовка
    for price in processed_prices:
        writer.writerow([price])

print("Преобразование завершено. Данные сохранены в processed_prices.csv")