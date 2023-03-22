import wikipedia
import requests
import json


#возвращает ссылку на изображение из википедии 
def get_wiki_image(search_term):
    try:
        result = wikipedia.search(search_term, results = 1)
        wikipedia.set_lang('en')
        wkpage = wikipedia.WikipediaPage(title = result[0])
        title = wkpage.title
        
        req = requests.get("http://en.wikipedia.org/w/api.php?",
                           params={'action': 'query', 'prop': 'pageimages', 'format': 'json', 'piprop': 'original', 'titles': search_term})
        
        data = json.loads(req.text)
        img_link = list(data['query']['pages'].values())[0]['original']['source']
        
        return img_link  
     
    except:
        return 0


#wiki_image = get_wiki_image('Abraham Lincoln')
#print(wiki_image)

# https://upload.wikimedia.org/wikipedia/commons/a/ab/Abraham_Lincoln_O-77_matte_collodion_print.jpg