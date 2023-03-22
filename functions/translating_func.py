from googletrans import Translator, constants


def translator_qu(txt):
    translator = Translator()
    
    lang_list = ['en', 'ru', 'es', 'de', 'fr', 'zh-TW']
    
    data = ''
    
    for i in lang_list:
        translation = translator.translate(txt, dest=i)     
        data += f"{translation.text}   ({translation.dest})\n\n"
    
    return data

    #print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")
    #Hola Mundo (es) --> Привет, мир (ru)
    
    
#print(translator('Привет, сладкие мои'))