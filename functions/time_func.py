# возвращает самые популярные города со временем
# также возвращает местное время


import requests


def time():
    # https://timeapi.io/api/Time/current/zone?timeZone=Europe/Amsterdam

    list_zones = ['Europe/London', 'Europe/Moscow', 'Europe/Berlin',
                  'America/Los_Angeles', 'America/Toronto',
                  'Asia/Dubai', 'Asia/Hong_Kong', 'Asia/Tokyo',
                  'Africa/Lagos'
                  ]

    txt = 'The time of our vast planet:\n\n'

    for i in list_zones:
        req = requests.get("https://timeapi.io/api/Time/current/zone?",
                           params={'timeZone': i})

        data = req.json()

        # print(i, '---------------', data)

        txt += f"{i.split('/')[1]} : {data['time']} \n"

    txt += "\nHaven't found the right time? Follow the link bellow!\n\nhttps://www.timeanddate.com/worldclock/?low=c"

    return txt
