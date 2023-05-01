import requests
import os
import sys
from map_func import *
import aiohttp

async def get_response(url, params):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as resp:
            return await resp

# предлагаем отправить именно координаты через запятую сначала долготу, потом ширину
async def traffic(coords):
    # address = text(coords)
    # запрос с получением картинки с пробками
    map_request = f"https://static-maps.yandex.ru/1.x/?ll={coords}&spn=0.01,0.01&l=map,trf"
    response = await get_response(map_request, {})

    if not response:
        #print('Ошибка выполнения запроса:')
        #print(map_request)
        #print('Http статус:', response.status_code, '(', response.reason, ')')
        return 'error - try again later'
    # возвращаем картинку
    return response.content
