import requests


def send_request(url, params):
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.text


def create_url(data_city, url):
    path = data_city['path']
    ready_params = data_city.get('params')
    ready_url = url.format(path)
    return ready_url, ready_params


if __name__ == '__main__':
    wttr_url = 'https://wttr.in/{}'

    data_params = {'lang': 'ru', 'M': '', 'n': '', 'q': '', 'T': ''}
    cities = {
        'Лондон': {'path': 'london', 'params': data_params},
        'Аэропорт Шереметьево': {'path': 'SVO', 'params': data_params},
        'Череповец': {'path': 'Череповец', 'params': data_params}
    }

    for city in cities:
        full_url, params_city = create_url(cities[city], wttr_url)
        resp_text = send_request(full_url, params_city)
        print(resp_text)
