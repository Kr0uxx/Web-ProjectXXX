import requests
from wiki_photo_func import get_wiki_image 
from translating_func import translator_qu

def quote(): 
    req = requests.get('https://favqs.com/api/qotd') 
    data = req.json()
    
    author = data["quote"]["author"]
    txt = data['quote']['body']
    img_url = get_wiki_image(author)
    
    text = f"{author} - \n\n"
    text += f"{translator_qu(txt)}"
    
    if img_url == '0':
        return text, 'error'
    
    return text, img_url
    

#a, b = quote()
#print(a)
#print('ссылка:  ',  b)