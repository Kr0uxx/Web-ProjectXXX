import openai 
from requests.exceptions import ReadTimeout
from openai.error import RateLimitError, InvalidRequestError
from datetime import datetime


# Предоставляем ключ API 
openai.api_key = "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"


def ask(prompt, a): # def которая отвечает за получение ответа , чтобы задать вопрос ask('вопрос')
    try:
        completion = openai.Completion.create(engine="text-davinci-003", prompt=prompt, temperature=0.5, max_tokens=1000)
    
        if a == 1:
            answ = completion.choices[0]['text']
            answer = f'Ответ на вопрос\n\n{prompt} :\n\n{answ}'
        
        elif a == 0:
            answ = completion.choices[0]['text']
            answer = f'{answ}'
    
        return answer
    except Exception as e:
        #print(e)
        return 'Функция временно закрыта из за проблем с Open Ai и их чертовым ключом'



#print(ask('Кто такой Путин', 0))