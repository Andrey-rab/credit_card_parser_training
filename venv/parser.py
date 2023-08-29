# Библ. для работы с запросами
import requests
# Библ. которая разбирает html страницк и делает из неё объект
from bs4 import BeautifulSoup
# Модуль CSV, который создает csv файл
import csv

# Домен, который мы парсим и страница
HOST = 'https://www.vbr.ru/'
URL = 'https://www.vbr.ru/banki/kreditnyekarty/'

# Отдаём загаловки, для того, чтобы ресурс не подумал, что мы боты.
HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}

# Функция, которая получает html
def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r
html = get_html(URL)
print(html)
