import requests
from bs4 import BeautifulSoup

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/53.0.2785.116 Safari/537.36 OPR/40.0.2308.81',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'DNT': '1',
    'Accept-Encoding': 'gzip, deflate, lzma, sdch',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4'
}


# получение soup, в функцию передаются язык(на выбор пользователя) и слово(пользователь вводит)
def get_url(language, word):
    url = f'https://dictionary.cambridge.org/dictionary/english-{language.lower()}/{word}'
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    if soup.find('h1').text == '404. Page not found.':
        return 'Неверно введен язык, пожалуйста, введите его заново'

    elif soup.find('h1').text[:7] == 'English':
        return 'Такого слова не существует, либо оно отсутствует в словаре, пожалуйста, введите новое слово'

    return soup


# функция, которая выдает определения и перевод слова на нужном языке и части речи
def get_translate(language, word, pos):
    soup = get_url(language, word)
    lever = False

    for i in soup.find_all('div', class_='pr entry-body__el'):
        i = (list(filter(lambda x: x != '' and x != ' ' and x != '       '
                                   and x != 'Your browser doesn\'t support HTML5 audio',
                         i.text[len(word)::].split('\n'))))
        print(i)
        count = 0
        if pos in i[0][:i[0].find(' ')]:
            lever = True
            for j in i[1::]:
                if pos in j:
                    count += 1
            print(count)
    if lever:
        return ''
    else:
        return 'Для этого слова такой части речи не существует'


print(get_translate('russian', 'present', 'verb'))
