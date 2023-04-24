import requests
from bs4 import BeautifulSoup
import pymorphy2

morph = pymorphy2.MorphAnalyzer()

link = "https://www.cbr.ru/currency_base/daily/"
r = requests.get(link)

soup = BeautifulSoup(r.text, "html.parser")
listt = soup.find('tbody').text.split("\n\n")
currencies_names = []
for i in listt[2::]:
    currencies_names.append(i.split("\n")[2::])


# currencies_names - список со всеми актуальными курсами валют


# функция для корректировки формы слов у названия валюты в родительный падеж, единственное число,
# чтобы пользователю было максимально комфортно
def correct_currency_form(currency_name):
    if currency_name == "Турецких лир":
        return "турецкой лиры"
    currency_name = currency_name.split()
    if len(currency_name) == 1:
        return morph.parse(currency_name[0])[0].inflect({'sing', 'gent'}).word
    elif len(currency_name) > 1 and morph.parse(currency_name[0])[0].tag.POS != 'NOUN':
        return morph.parse(currency_name[0])[0]. \
            inflect({'sing', 'gent', morph.parse(currency_name[1])[0].tag.gender}).word + ' ' + \
            morph.parse(currency_name[1])[0].inflect({'sing', 'gent'}).word
    else:
        string = ''
        for j in currency_name[1::]:
            string += j + ' '
        return morph.parse(currency_name[0])[0].inflect({'sing', 'gent'}).word + ' ' + \
            string.rstrip()


# функция, возвращающая актуальный курс валюты на выбор(передается буквенное сокращение валюты)
def get_actual_rate(input_currency):
    # те валюты, которые будут доступны пользователю:
    # currencies_list = ["USD", "EUR", "CNY", "GBP", "JPY", "CHF", "UAH", "TRY", "AUD"]
    rate = 0
    currency = ''
    for name in currencies_names[:-1]:
        if name[0] == input_currency:
            currency = name[2]
            rate = float(name[3].replace(',', '.')) / float(name[1].replace(',', '.'))
    return f"Курс для 1 {correct_currency_form(currency)} составляет {rate} RUB."


'''print(get_actual_rate('USD'))
print(get_actual_rate('EUR'))
print(get_actual_rate('CNY'))
print(get_actual_rate('GBP'))
print(get_actual_rate('JPY'))
print(get_actual_rate('CHF'))
print(get_actual_rate('UAH'))
print(get_actual_rate('TRY'))
print(get_actual_rate('AUD'))'''
