from flask import Flask
from Msc_wthr_task import get_weather
from datetime import datetime
import settings

city_id = 524901
apikey = settings.OPEN_WEATHER_MAP_APIKEY

app = Flask(__name__)

@app.route('/')
def index():
    url = 'http://api.openweathermap.org/data/2.5/weather?id=%s&APPID=%s&units=metric' % (city_id, apikey)    
    weather = get_weather(url) 
    cur_date = datetime.now().strftime('%d.%m.%Y')
    print(cur_date)
    result = '<p><b>City:</b> %s</p>' % weather['name']
    result += '<p><b>Date:</b> %s</p>' % cur_date
    result += '<p><b>Temperature:</b> %s</p>' % weather['main']['temp']
    result += '<p><b>Wind:</b> %s</p>' % weather['wind']['speed'] 
    return result

if __name__ == '__main__':
    app.run()