import requests
from flask import Flask, redirect, url_for, render_template,request
import os

#cant get env variable to work with flask & api
# key = os.environ.get('WEATHER_KEY')
# print(key)

app = Flask(__name__)
app.config['DEBUG'] = True

# home page returns inline html
#routes to path to get this function
@app.route("/", methods = ["GET","POST"])
def index():
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=4b6b68f7c077148d29c5d6d9162f005d'    
    if request.method == "POST":
        city = request.form["city-input"]
    else:
        city = 'minneapolis'

    r = requests.get(url.format(city)).json()
     

    #create weather object to hold api data
    weather = {
        'city': city,
        'temp': r['main']['temp'],
        'descript': r['weather'][0]['description'],
        'icon':  r['weather'][0]['icon']
        }
    print(weather)
    return render_template('weather.html', weather=weather)

if __name__ == "__main__":
    app.run()