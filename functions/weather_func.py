#ищет погоду в месте запроса 
import requests

app_id = '9679c05520936f7d691139a917576317'


def moji(txt):
    
    dict_m = {
        'Thunderstorm': '🌩',
        'Drizzle': '🌦',
        'Rain': '🌧',
        'Snow': '🌨',
        'snow': '🌨',
        'Clear': '☀️',
        'Clouds': '🌥'
        }
    try:
        return dict_m[txt]
    except Exception:
        return '🌫'


def weather(coords):
    req = requests.get("https://api.openweathermap.org/data/2.5/weather?",
                       params={'q': coords, 'units': 'metric', 'lang': 'ru', 'APPID': app_id})
    
    #'lang': 'en' для англ версии 
    

    data = req.json()
    
    dictt = {}
    
    dictt['weather'] = data['weather'][0]['description']
    dictt['temperature'] = data['main']['feels_like']
    
    sp = data['wind']['speed']
    d = data['wind']['deg']
    
    dictt['wind'] = f'{sp}, {d}'
    dictt['visibility'] = data['visibility']
    dictt['humidity'] = data['main']['humidity']
    
    dictt['png'] = moji(data['weather'][0]['main'])
    
    txt = f"Фух, нашли:\n\n {dictt['png']}\n\n {dictt['weather'].capitalize()} \n\n Температура: {dictt['temperature']} C \n Ветер: {dictt['wind']} \n Видимость: {dictt['visibility']} m \n Влажность: {dictt['humidity']} %"
      
    return txt
    
    
# EXAMPLE --- print(weather('Ural'))



#https://yandex.ru/dev/weather/doc/dg/concepts/about.html 
#https://habr.com/ru/post/315264/
#https://openweathermap.org/
#https://openweathermap.org/current