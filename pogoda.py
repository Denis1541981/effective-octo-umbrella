import requests
import json
import time



def get_info_weather():
    """Получение данных о погоде, по умолчанию Бердск"""

    id = '1510350'
    lat = 54.858795
    lon = 82.962293
    
    try:
        res = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&lang=ru&appid={API}&units=metric')
        data = res.json()
        temp = f"Температура за бортом: {round(data['main']['temp'])}°C"
        return temp
    except Exception as ex:
        print(ex)
        print('Проверьте подключение к интернету')
    
        

def geoloc(city="Бердск"):
    """Получение гедеоданыых"""
    URL = f"https://api.openweathermap.org/geo/1.0/direct?q={city}&lang=ru&limit={1}&mode=json&appid={API}"
    res = requests.get(url=URL)
    if res.raise_for_status():
        return None
    items = res.json()[0]
    lat = items.get('lat')
    lon = items.get('lon')
    return lat, lon



def main():
    print(get_info_weather())


if __name__ == "__main__":
    main()
