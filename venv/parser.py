# Библ. для работы с запросами
import requests
# Библ. которая разбирает html страницк и делает из неё объект
from bs4 import BeautifulSoup
# Модуль CSV, который создает csv файл
import csv

# Домен, который мы парсим и страница
HOST = 'https://bankiros.ru/'
URL = 'https://bankiros.ru/credit-cards'

# Отдаём загаловки, для того, чтобы ресурс не подумал, что мы боты.
HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'user-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
}

# Функция, которая получает html
def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    #f = requests.
    return r
# отладка
# html = get_html(URL)
# print(html)

#Получаем контент с html
def get_content(html):
    # Получаем объект страницы
    soup = BeautifulSoup(html, 'html.parser')
    #парсим блоки карт
    items = soup.findAll('div', class_='xxx-listing-list__item')
    cards = []
    for item in items:
        # асоциативный словарь. Здесь показываем, что будем собирать
        cards.append(
            {
                # strip=True удаляет лишние пробелы
                'title': item.find('div', class_='xxx-listing-card__title-wrap').get_text(strip=True),
                'link_product': item.find('div', class_='xxx-listing-card__title-wrap').find('a').get('href'),
                'brand': item.find('div', class_='xxx-listing-card__title-wrap').find('span').get_text(),
                #'img_card': item.find('div', class_='xxx-listing-card__img').find('img').get('src'),
                'img_card': item.find('div', class_='xxx-listing-card__img').find('img').get('data-url-img')
            }
        )
    return cards
    #print(items)
# отладка
# html = get_html(URL)
# content = get_content(html.text)
# print(content)

def parser():
    # Получать кол-во пагинации
    PAGINATION = input('Укажите кол-во страниц для парсинга: ')
    PAGINATION = int(PAGINATION)
    html = get_html(URL)
    if html.status_code == 200:
        cards = []
        # Циклом проходим по страницам и парсим каждую, подставляя в params счетчик (номер страницы)
        for i in range(1, PAGINATION+1):
            print(f'Парсинг страницы: {i}')
            html = get_html(URL, params=f'page={i}')
            # добавляем в словарь cards полученный контент со страницы
            cards.extend(get_content(html.text))
            # print(get_content(html.text))
        print(cards)
        print(f'Парсинг завершился! Получино страниц: {i}')
    else:
        print('Error')
    #return html

print(parser())