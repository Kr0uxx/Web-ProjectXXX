import requests


# from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# функция для получения адреса по координатам
def get_address_from_coords(coords):
    parametrs = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "format": "json",
        "lang": "ru_RU",
        "kind": "house",
        "geocode": coords
    }

    try:
        r = requests.get(url="https://geocode-maps.yandex.ru/1.x/", params=parametrs)
        json_data = r.json()
        address_str = json_data["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["metaDataProperty"][
            "GeocoderMetaData"]["AddressDetails"]["Country"]["AddressLine"]
        return address_str

    except Exception:
        return "error in processing data - try again later"


# функция, если пользователь отправил координаты
def text(coordinates):
    # получение адреса от пользователя
    coords = coordinates
    # получение адреса из координат
    address_str = get_address_from_coords(coords)
    return address_str


# функция, если пользователь отправил геолокацию
def location(geolocation):
    message = geolocation
    # получение долготы и широты
    current_position = (message.location.longitude, message.location.latitude)
    coords = f"{current_position[0]},{current_position[1]}"
    # отправляем координаты в нашу функцию получения адреса
    address_str = get_address_from_coords(coords)
    return address_str
