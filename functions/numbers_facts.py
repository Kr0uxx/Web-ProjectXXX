# Использование API: http://numbersapi.com/<number>/<type>, где number — число, а type — тип факта
# (trivia — факт из жизни, math — математический факт, date и year — вопрос про дату (в формате MM/DD) и год).

import requests
import os
import asyncio
import aiohttp


categories_list = ['trivia', 'math', 'date']


async def get_response(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return await resp.json()


async def get_news(category, *data):
    global categories_list

    if len(data) == 2:
        month, day = data
        req = await get_response(f'http://numbersapi.com/{month}/{day}/{category}')
    elif len(data) == 1:
        number = data
        req = await get_response(f'http://numbersapi.com/{number}/{category}')

    request = req
    text = 'Here u r: \n\n'
    try:
        text += str(request.text())
        return text

    except Exception:
        if text == 'Here u r: \n\n':
            return 'Oooops, smth went wrong... :('
        return text
