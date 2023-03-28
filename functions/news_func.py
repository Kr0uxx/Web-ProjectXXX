#https://newsapi.org/docs/endpoints/top-headlines

# categories = ['business', 'entertainment', 'general', 'health', 'science', 'sports', 'technology']
# country = ['ch', 'ru', 'fr', 'de', 'us', 'en']

import requests



key = 'a7aa77aa97884b9780c4f55b57811f18'

categories_list = ['business', 'entertainment', 'general', 'health', 'science', 'sports', 'technology']
country_list = ['ch', 'ru', 'fr', 'de', 'us', 'en']
    
    
def get_news(country='us', category='general'):
    global key, categories_list, country_list
    
    if country not in country_list:
        country = 'us'
    
    if category not in categories_list:
        category = 'general'
     
    req = requests.get('https://newsapi.org/v2/top-headlines?',
                       params={'country': country, 'category': category, 'pageSize': 21, 'apiKey': key})
    data = req.json()
    
    text = 'Here u r: \n\n'
    
    try:
        for i in range(0, 21):
            title = data['articles'][i]['title']
            desc = data['articles'][i]['description']
            s_url = data['articles'][i]['url']
            
            if desc is not None:
                text += f'----\n\nTitle: {title}\n\nDescription: {desc}\n\nUrl: {s_url} \n\n'
                
            else:
                text += f'----\n\nTitle: {title}\n\nUrl: {s_url} \n\n'
                    
        return text
            
    except Exception:
        if text == 'Here u r: \n\n':
            return 'Oops, smth went wrong... :('
        
        return text      
    
    
def get_spec_news(about):
    global key 
    
    try:
        text = 'Here u r: \n\n'
        
        req = requests.get('https://newsapi.org/v2/top-headlines?',
                           params={'q': about, 'apiKey': key})
        data = req.json()
        
        if not data:
            raise Exception
        
        for i in range(0, 21):
            title = data['articles'][i]['title']
            desc = data['articles'][i]['description']
            s_url = data['articles'][i]['url']
            
            if desc is not None:
                text += f'----\n\nTitle: {title}\n\nDescription: {desc}\n\nUrl: {s_url} \n\n'
                
            else:
                text += f'----\n\nTitle: {title}\n\nUrl: {s_url} \n\n'
                    
        return text
        
    except Exception:
        if text == 'Here u r: \n\n':
            return 'Oops, smth went wrong... :('
        
        return text
    
    
    
#print(get_news('ru', 'science'))
#print(get_spec_news('Путин'))