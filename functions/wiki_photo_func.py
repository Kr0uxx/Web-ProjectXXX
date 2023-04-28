import wikipedia
import requests
import json
import aiohttp

# https://en.wikipedia.org/w/api.php?action=help&modules=query

async def get_response(url, params):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as resp:
            return await resp.json()

# возвращает ссылку на изображение из википедии
async def get_wiki_image(search_term):
    try:
        result = wikipedia.search(search_term, results=1)

        wikipedia.set_lang('en')
        wkpage = wikipedia.WikipediaPage(title=result[0])
        title = wkpage.title

        req = await get_response("http://en.wikipedia.org/w/api.php?", params={'action': 'query', 'prop': 'pageimages', 'format': 'json', 'piprop': 'original', 'titles': title})

        data = json.loads(req.text)

        img_link = list(data['query']['pages'].values())[0]['original']['source']

        return img_link

    except Exception as e:
        return '0'

# wiki_image = get_wiki_image('Sun Tzu')
# print(wiki_image)

# https://upload.wikimedia.org/wikipedia/commons/a/ab/Abraham_Lincoln_O-77_matte_collodion_print.jpg
