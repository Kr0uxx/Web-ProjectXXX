#получает координаты и возвращает место или error
import requests


token = '3d552f1f-eb93-4a0c-9d6c-4f52aad5060d'

#создаем функцию get_address_from_coords с параметром coords, куда мы будем посылать координаты и получать готовый адрес.
def get_address_from_coords(coords):
    
    PARAMS = {
        "apikey": token,
        "format":"json",
        "lang":"ru_RU",
        "kind":"house",
        "geocode": coords
    }

    try:
        r = requests.get(url="https://geocode-maps.yandex.ru/1.x/", params=PARAMS)
        #получаем данные
        json_data = r.json()
        #вытаскиваем из всего пришедшего json именно строку с полным адресом.
        address_str = json_data["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["metaDataProperty"]["GeocoderMetaData"]["AddressDetails"]["Country"]["AddressLine"]
        #возвращаем полученный адрес
        return address_str
    
    except Exception as e:
        #если не смогли, то возвращаем ошибку
        return "error"