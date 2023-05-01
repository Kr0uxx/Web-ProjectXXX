import aiohttp
import asyncio
import requests

key = '64c7e00c68104cf5ac819fa7eb8807cb'


# Функции для парсинга instructions, т.к. они всегда написаны по разному и порой через жопу
def recursion_delete(string):
    if string.find('<') > -1:
        return recursion_delete(string[:string.find('<')] + string[string.find('>') + 1:])
    else:
        return string


def instruction_parser(instruction):
    if instruction[:8] == '<ol><li>':
        instruction = instruction.split('</li><li>')
    elif instruction[:3] == '<p>':
        instruction = instruction.split('</p><p>')
    elif '\n' in instruction:
        instruction = instruction.split('\n')
    else:
        return instruction, 0
    for i in instruction:
        instruction[instruction.index(i)] = recursion_delete(i)
    return instruction, 1


async def get_response(url, params):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as resp:
            return await resp.json()


# запрашивает у пользователя строку тегов
def get_random_recipe(tags=''):
    # теги
    # veryPopular, vegetarian, vegan, veryHealthy, cheap, greek, italian, african, american, british, cajun, caribbean,
    # chinese, eastern european, european, french, german, greek, indian, irish, italian, japanese, jewish, korean,
    # latin american, mediterranean, mexican, middle eastern, nordic, southern, spanish, thai, vietnamese
    global key
    req = requests.get('https://api.spoonacular.com/recipes/random',
                       params={'limitLicense': True, 'tags': tags, 'apiKey': key})
    data = req.json()
    print(data)
    text = f'Here is a random recipe for u: \n'
    for recipe in data['recipes']:
        title = recipe['title']
        img = recipe['image']
        price = round(recipe['pricePerServing'] / 100, 2)  # цена за 1 порцию
        time = recipe['readyInMinutes']  # время приготовления
        servings = recipe['servings']  # количество порций
        ingredients = recipe['extendedIngredients']
        text += f'{title}\n' \
                f'{img}\n' \
                f'time: {time} min\n' \
                f'price per serving: {price}$\n' \
                f'servings: {servings}\n' \
                f'amount price: {round(price * servings, 2)}$\n' \
                f'ingredients:\n'

        # Добавление ингредиентов
        for ingredient in ingredients:
            measures = ingredient['measures']['metric']
            text += f'   •{ingredient["name"]} ({measures["amount"]} {measures["unitShort"]})\n'

        instruction = recipe['instructions']
        text += '\nInstruction:\n'
        if instruction_parser(instruction)[1] == 0:
            text += f'  {instruction_parser(instruction)[0]}\n'
        else:
            instruction = instruction_parser(instruction)[0]
            for step in instruction:
                text += f'  {instruction.index(step) + 1}){step}\n'

        text += '\n'

    return text


print(get_random_recipe('cajun'))
