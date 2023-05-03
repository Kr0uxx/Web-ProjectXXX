import aiohttp
import asyncio
import requests


async def get_response(url, params):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as resp:
            return await resp.json()


async def send(email, text, person):
    url = "https://rapidprod-sendgrid-v1.p.rapidapi.com/alerts/1"
    response = await get_response(url,
                                  {"type": "stats_notification", "email_to": "example@test.com", "frequency": "daily",
                                   "content-type": "application/json",
                                   "X-RapidAPI-Key": "3053af2a23msh51dc8d631ba6ccap1d6dc0jsn58f1c962469e",
                                   "X-RapidAPI-Host": "rapidprod-sendgrid-v1.p.rapidapi.com"})

    print(response)


url = "https://rapidprod-sendgrid-v1.p.rapidapi.com/alerts/1"

payload = {"type": "stats_notification",
           "email_to": "artem.17sn@gmail.com",
           "frequency": "daily"
           }
headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": "3053af2a23msh51dc8d631ba6ccap1d6dc0jsn58f1c962469e",
    "X-RapidAPI-Host": "rapidprod-sendgrid-v1.p.rapidapi.com"
}

response = requests.patch(url, json=payload, headers=headers)

# print(response.json())
