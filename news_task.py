
from flask import Flask, abort

from Msc_wthr_task import get_weather

from datetime import datetime

from news_list import all_news

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

@app.route('/news/<int:news_id>')
def news_by_id(news_id):
    news_to_show = [news for news in all_news if news['id'] == news_id]
    if len(news_to_show) == 1:
        result = '<h1>%(title)s</h1><p><i>%(date)s</i></p><p>%(text)s</p>'
        result = result % news_to_show[0]
        return result
    
    else:        
        abort(404)



if __name__ == '__main__':
    app.run(debug=True)





