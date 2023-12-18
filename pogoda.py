import requests
import json
import time
# 'lat': 54.743766199999996, 'lon': 83.06268907860164, 'country': 'RU', 'state': 'Novosibirsk Oblast'}


API = '07bd3abda71092417b445c7e621b737a'
def get_info_weather():
    """Получение данных о погоде, по умолчанию Бердск"""
    city = ''
    # lat = geoloc(city)[0]
    # print(lat)
    # lon = geoloc(city)[1]
    # print(lon)
    
    id = '1510350'
    
    try:
        res = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?id={id}&lang=ru&appid={API}&units=metric')
        data = res.json()
        temp = f"Температура за бортом: {round(data['main']['temp'])}°C"
        print(temp)
        return temp
    except Exception as ex:
        print(ex)
        print('Проверьте подключение к интернету')
    
        

def geoloc(city):
    """Получение гедеоданыых"""
    URL= f"http://api.openweathermap.org/geo/1.0/direct?q={city}&lang=ru&limit={1}&mode=json&appid={API}"
    res = requests.get(url=URL)
    for i in res.json():
        lat = i['lat']
        lon = i['lon']
        
        return lat, lon


def main():
    # city = input('Введите город: ')
    
    get_info_weather()

    # geoloc(city=city)
if __name__ == "__main__":
    main()