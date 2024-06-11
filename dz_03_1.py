"""
Необходимо спарсить цены на диваны с сайта divan.ru в csv файл,
обработать данные, найти среднюю цену и вывести ее,
а также сделать гистограмму цен на диваны
"""
import requests
from bs4 import BeautifulSoup
import csv


# URL страницы
url = "https://www.divan.ru/category/divany-i-kresla"

# Заголовки для запроса, чтобы имитировать браузер
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}
# Выполнение GET-запроса к странице
# Создаём список, в который потом всё будет сохраняться
parsed_data = []
try:
    response = requests.get(url, headers=headers)
    print(f"Статус {response.status_code}")

    # Парсинг HTML-контента страницы
    soup = BeautifulSoup(response.content, 'html.parser')
    # Пример нахождения дивана (зависит от структуры HTML)
    items = soup.find_all('div', class_='lsooF')
    # print(items)

    for item in items:
        # Нахождение наименования дивана
        name = item.find('a', class_='ui-GPFV8 qUioe ProductName ActiveProduct').text.strip()
        print(f"name {name}")
        # Нахождение цены дивана
        price = item.find('span', class_='ui-LD-ZU KIkOH').text.strip()
        print(f"Price {price}")
        # Нахождение ссылки на светильник
        link = item.find('a', class_='ui-GPFV8 qUioe ProductName ActiveProduct')['href']
        print(f"Ссылка {link}")
        full_link = f"https://www.divan.ru{link}"
        # Вносим найденную информацию в список
        parsed_data.append([name, price, full_link])

except:
    print('произошла ошибка при парсинге')

# Прописываем открытие нового файла, задаём ему название и форматирование
# 'w' означает режим доступа, мы разрешаем вносить данные в таблицу
with open("divan.csv", 'w', newline='', encoding='utf-8') as file:
    # Используем модуль csv и настраиваем запись данных в виде таблицы
    # Создаём объект
    writer = csv.writer(file)
    # Создаём первый ряд
    writer.writerow(['Название дивана', 'Цена', 'Ссылка на диван'])
    # Прописываем использование списка как источника для рядов таблицы
    writer.writerows(parsed_data)
print("Цены успешно сохранены в файл prices_divan.csv")