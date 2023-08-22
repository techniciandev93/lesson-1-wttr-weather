import requests


def send_request(url):
    response = requests.get(url)
    return response.text


def wttr_weather_main():
    url = 'https://wttr.in/{}{}'

    dict_cities = {
        'Лондон': {'path': 'london', 'params': '?lang=ru&MnqT'},
        'Аэропорт Шереметьево': {'path': 'cvo', 'params': '?lang=ru&MnqT'},
        'Череповц': {'path': 'Череповец', 'params': '?lang=ru&MnqT'}
    }

    for city in dict_cities:
        path = dict_cities[city].get('path')
        params = dict_cities[city].get('params')
        params = params if params else ''
        full_url = url.format(path, params)
        resp_text = send_request(full_url)
        print(resp_text)


if __name__ == '__main__':
    wttr_weather_main()
