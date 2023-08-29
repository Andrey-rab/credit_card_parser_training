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

