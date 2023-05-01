import requests
import os
import sys
from map_func import *
import aiohttp
import asyncio

if os.name == 'nt':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def get_response(url, params):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as resp:
            return await resp.json

# предлагаем отправить именно координаты через запятую сначала долготу, потом ширину
async def traffic(coords):
    # address = text(coords)
    # запрос с получением картинки с пробками
    map_request = f"https://static-maps.yandex.ru/1.x/?ll={coords}&spn=0.01,0.01&l=map,trf"
    print(map_request)
    response = await get_response(map_request, {})
    
    
    if not response:
        #print('Ошибка выполнения запроса:')
        #print(map_request)
        #print('Http статус:', response.status_code, '(', response.reason, ')')
        return 'error - try again later'
    # возвращаем картинку
    return response.content
