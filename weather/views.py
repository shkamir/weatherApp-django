from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm
# open weather api key
api_key = 'YOUR OPEN WEATHER MAP API KEY HERE'
def index(request):
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={}"

    if request.method == 'POST':
 
        form = CityForm(request.POST or None)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            City.objects.create(name=name)


    form = CityForm()

    cities = City.objects.all()
    weather_data = []
    for city in cities:

        r = requests.get(url.format(city.name,api_key)).json()


        city_weather = {
            "city": city.name,
            "temperature": r["main"]['temp'],
            "description": r['weather'][0]['description'],
            "icon": r["weather"][0]["icon"],
        }
        weather_data.append(city_weather)
        

    context = {
        "weather_data":weather_data,
        "form": form
    }
    return render(request, 'weather/index.html', context)
