"""
Разработка кейса
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
import time
import csv

driver = webdriver.Firefox()

# Открытие сайта
url = 'https://www.cian.ru/snyat-kvartiru-1-komn-ili-2-komn/'
# открытие страницы
driver.get(url)
# Задержка для загрузки страницы
time.sleep(5)

# Поиск элементов, содержащих цены
# price_elements = driver.find_elements(By.XPATH, "//div[@data-name='PriceInfo]//span[@data-mark='MainPrice']/span")
price_elements = driver.find_elements(By.XPATH, '//span[@data-mark="MainPrice"]')

# Извлечение текста цен и сохранение их в список
prices = [element.text for element in price_elements]

# Закрытие драйвера
driver.quit()

# Запись цен в CSV файл
with open('prices.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Price'])  # Запись заголовка
    for price in prices:
        writer.writerow([price])

