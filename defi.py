import requests
import pyuseragents


def auth():
    url = 'https://api.de.fi/v1/users/auth/sign-in'
    data = {
         'emailOrUsername': 'mail@mail.ru',  # Сюда вставляете почту
         'password': '123566', #Сюда пароль
    }
    session = requests.Session()
    session.headers.update(headers)
    return session.post(url, data=data).text # Возвращает вам ваш access-token

headers = {
        'authority': 'api.de.fi',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk-UA;q=0.6,uk;q=0.5', 
        'authorization': 'Bearer access-token', #После "Bearer " вставляете свой access-token
        'origin': 'https://de.fi',
        'referer': 'https://de.fi/',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': pyuseragents.random(),
    }

def follow(ID):
    url = f'https://api.de.fi/v1/users/connections/follow/{ID}'

    session = requests.Session()
    session.headers.update(headers)
    session.proxies.update({'https':'http://username:password@ip:port'}) #Сюда прокси кидаете, слева тип проксей(https/socks5), справа прокси в формате http://username:password@ip:port
    a = session.post(url)
    if a.status_code == 429:
        print("Too many reqs")
    else:
        print(f'followed to {ID}')
    return a.text


