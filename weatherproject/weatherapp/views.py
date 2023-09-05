from django.shortcuts import render
import requests
import datetime

# Create your views here.
def index(request):
    
    if 'city' in request.POST:
        city=request.POST['city']
    else:
        city='Batumi'
    
    
    appid='eda52f12a3e16f9e7d8bec1674a92285'
    URL= 'https://api.openweathermap.org/data/2.5/weather'
    PARAMS={'q':city, 'appid':appid, 'units':'metric'}
    r=requests.get(url=URL, params=PARAMS)
    res=r.json()
    description=res['weather'][0]['description']
    icon=res['weather'][0]['icon']
    temp=res['main']['temp'] 

    day=datetime.date.today()


    return render(request, 'weatherapp/index.html', {'description':description, 'icon':icon, 'temp':temp, 'day':day, 'city':city})