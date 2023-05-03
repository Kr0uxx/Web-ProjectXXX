# Использование API: http://numbersapi.com/<number>/<type>, где number — число, а type — тип факта
# (trivia — факт из жизни, math — математический факт, date и year — вопрос про дату (в формате MM/DD) и год).

import requests
import os
import asyncio
import aiohttp


async def get_date(data):
    try:
        month, day = data
        req = requests.get(f'http://numbersapi.com/{month}/{day}/date')
        text = str(req.text)
        
        return text

    except Exception:
        return 'Oooops, smth went wrong... :('


async def get_math(data):
    try:
        number = data
        req = requests.get(f'http://numbersapi.com/{number}/math')
        text = str(req.text)
        
        return text
    
    except Exception:
        return 'Oooops, smth went wrong... :('


async def get_num(data):
    number = str(data)
    req = requests.get(f'http://numbersapi.com/{number}')
    try:
        text = str(req.text)
        return text
    except Exception:
        return 'Oooops, smth went wrong... :('

# print(asyncio.run(get_date((1, 25))))
# print(asyncio.run(get_math(22)))
# print(asyncio.run(get_num(22)))
