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
                       params={'q': coords, 'units': 'metric', 'lang': 'en', 'APPID': app_id})
    
    #'lang': 'ru' для ru версии 
    

    data = req.json()
    
    dictt = {}
    
    dictt['weather'] = data['weather'][0]['description']
    dictt['temperature'] = data['main']['feels_like']
    
    sp = data['wind']['speed']
    d = data['wind']['deg']
    
    dictt['wind'] = f"{sp} m/sec ; {d} deg"
    dictt['visibility'] = str(int(data['visibility']) / 1000)
    dictt['humidity'] = data['main']['humidity']
    
    dictt['png'] = moji(data['weather'][0]['main'])
    
    txt = f"Oh, here u r:\n\n {dictt['png']}\n\n {dictt['weather'].capitalize()} \n\n Temperature: {dictt['temperature']} C \n Wind: {dictt['wind']} \n Visibility: {dictt['visibility']} km \n Humidity: {dictt['humidity']} %\n"
      
    return txt
    

# EXAMPLE --- print(weather('Ural'))



#https://yandex.ru/dev/weather/doc/dg/concepts/about.html 
#https://habr.com/ru/post/315264/
#https://openweathermap.org/
#https://openweathermap.org/current