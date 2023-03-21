import speech_recognition as sr

#надо будет передать язык
#файл будет лежать в папке files под название !   wav_file.wav  !
#но его нужно создать еще будет 

def voice(lang):
    try:
        lang_dict = {'Russian': 'ru-RU',
                     'UK English': 'en-GB',
                     'US English': 'en-US',
                     'French': 'fr-CA',
                     'Dutch': 'de-DE',
                     'Italian': 'it-IT',
                     'Spanish': 'es-ES'}
        
        voice = sr.Recognizer()       
        with sr.AudioFile('files/wav_file.wav') as source:
            audio_text = voice.listen(source)
            text = voice.recognize_google(audio_text, language=lang_dict[lang])           
            
            return text
        
    except Exception:
        return 'error'
    
#Adding french langauge option
#text = r.recognize_google(audio_text, language = "fr-FR")
    
def voice_main():
    languages = ['Russian', 'UK English', 'US English', 'French', 'Dutch', 'Italian', 'Spanish']
    
    for i in languages:
        txt = voice(i)  
        
        if txt != 'error':
            if txt != '':
                return txt 
            else:
                return 'Opssss, seems to be empty... :('
        
    return 'error'


#print(voice_main())