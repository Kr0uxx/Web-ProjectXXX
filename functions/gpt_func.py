import openai 


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
