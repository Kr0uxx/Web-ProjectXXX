import requests
import os
import sys
from map_func import *


# предлагаем отправить именно координаты через запятую сначала долготу, потом ширину
def probki(coords):
    # address = text(coords)
    # запрос с получением картинки с пробками
    map_request = f"https://static-maps.yandex.ru/1.x/?ll={coords}&spn=0.01,0.01&l=map,trf"
    response = requests.get(map_request)

    if not response:
        print('Ошибка выполнения запроса:')
        print(map_request)
        print('Http статус:', response.status_code, '(', response.reason, ')')
        sys.exit(1)
    # возвращаем картинку
    return response.content
