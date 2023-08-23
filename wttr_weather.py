import requests


def send_request(url, params):
    response = requests.get(url, params=params)
    if response.ok:
        return response.text
    else:
        response.raise_for_status()


def create_url(data_city, url):
    path = data_city.get('path')
    ready_params = data_city.get('params')
    ready_url = url.format(path)
    return ready_url, ready_params


if __name__ == '__main__':
    url_wttr = 'https://wttr.in/{}'

    cities = {
        'Лондон': {'path': 'london', 'params': {'lang': 'ru', 'M': '', 'n': '', 'q': '', 'T': ''}},
        'Аэропорт Шереметьево': {'path': 'CVO', 'params': {'lang': 'ru', 'M': '', 'n': '', 'q': '', 'T': ''}},
        'Череповц': {'path': 'Череповец', 'params': {'lang': 'ru', 'M': '', 'n': '', 'q': '', 'T': ''}}
    }

    for city in cities:
        full_url, params_city = create_url(cities[city], url_wttr)
        resp_text = send_request(full_url, params_city)
        print(resp_text)
