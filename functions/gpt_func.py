import openai 
from requests.exceptions import ReadTimeout
from openai.error import RateLimitError, InvalidRequestError
import telebot
from telebot import types
from datetime import datetime


# Предоставляем ключ API 
openai.api_key = "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"


def ask(prompt, a): # def которая отвечает за получение ответа , чтобы задать вопрос ask('вопрос')
    completion = openai.Completion.create(engine="text-davinci-003", 
                                          prompt=prompt, 
                                          temperature=0.5, 
                                          max_tokens=1000)
    
    if a == 1:
        answ = completion.choices[0]['text']
        answer = f'Ответ на вопрос\n\n{prompt} :\n\n{answ}'
        
    elif a == 0:
        answ = completion.choices[0]['text']
        answer = f'{answ}'
    
    return answer
