import requests


def get_weather(url):
    result = requests.get(url)
    if result.status_code == 200:
        return result.json()
    else:
        print('таки ответ не 200')
    

if __name__ == '__main__':
   data = get_weather("http://api.openweathermap.org/data/2.5/weather?id=524901&APPID=4eac87a5624e1d9f704d297992d3c747&units=metric")
   print(data)