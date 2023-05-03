import asyncio
import os

import aiohttp


async def get_response(url, params):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as resp:
            return await resp.json()


async def find_anime(key_word):
    req = await get_response('https://kitsu.io/api/edge/anime?filter[text]=Cowboy Bebop', {})
    data = req
    print(data)


async def find_anime_name(key_word):
    req = await get_response('https://kitsu.io/api/edge/anime?atribute[canonicalTitle]=Cowboy Bebop', {})
    data = req
    print(data)
    # return data['activity']
    # img = data['data']['url']
    # return img


if os.name == 'nt':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

asyncio.run(find_anime(''))
