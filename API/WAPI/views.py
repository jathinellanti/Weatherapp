from django.shortcuts import render
import requests
from datetime import datetime


def home(request):
    return render(request, 'WAPI/home.html')

def forecast(request):
    if request.method == 'POST':
        location = request.POST.get('location')
        user_api = 'fc5265634804c6a02f729536824e0220'  # Replace with your OpenWeatherMap API key

        # Construct the API URLs for current weather and 5-day forecast
        current_weather_api_link = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={user_api}"
        forecast_api_link = f"https://api.openweathermap.org/data/2.5/forecast?q={location}&appid={user_api}"

        # Make requests to the APIs
        current_weather_api_response = requests.get(current_weather_api_link)
        forecast_api_response = requests.get(forecast_api_link)

        current_weather_data = current_weather_api_response.json()
        forecast_data = forecast_api_response.json()

        if current_weather_data['cod'] == 200 and forecast_data['cod'] == '200':
            # Process the current weather data
            current_temp = current_weather_data['main']['temp'] - 273.15
            current_weather_desc = current_weather_data['weather'][0]['description']
            current_humidity = current_weather_data['main']['humidity']
            current_wind_speed = current_weather_data['wind']['speed']

            # Extract and process the 5-day forecast data
            forecasts = []
            for forecast in forecast_data['list']:
                date_time = datetime.fromtimestamp(forecast['dt'])
                temperature = forecast['main']['temp'] - 273.15
                weather_desc = forecast['weather'][0]['description']
                humidity = forecast['main']['humidity']
                wind_speed = forecast['wind']['speed']

                forecast_info = {
                    'date_time': date_time,
                    'temperature': temperature,
                    'weather_desc': weather_desc,
                    'humidity': humidity,
                    'wind_speed': wind_speed,
                }
                forecasts.append(forecast_info)

            context = {
                'location': location,
                'current_temp': current_temp,
                'current_weather_desc': current_weather_desc,
                'current_humidity': current_humidity,
                'current_wind_speed': current_wind_speed,
                'forecasts': forecasts,
            }
            return render(request, 'WAPI/forecast.html', context)
        else:
            error_message = "Invalid City. Please check your City name."
            return render(request, 'WAPI/forecast.html', {'error_message': error_message})

    return render(request, 'WAPI/forecast.html')

def mumbai(request):
        location = 'MUMBAI'
        user_api = 'fc5265634804c6a02f729536824e0220'

        # Construct the API URL
        current_weather_api_link = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={user_api}"
        forecast_api_link = f"https://api.openweathermap.org/data/2.5/forecast?q={location}&appid={user_api}"

        # Make requests to the APIs
        current_weather_api_response = requests.get(current_weather_api_link)
        forecast_api_response = requests.get(forecast_api_link)

        current_weather_data = current_weather_api_response.json()
        forecast_data = forecast_api_response.json()

        if current_weather_data['cod'] == 200 and forecast_data['cod'] == '200':
            # Process the current weather data
            current_temp = current_weather_data['main']['temp'] - 273.15
            current_weather_desc = current_weather_data['weather'][0]['description']
            current_humidity = current_weather_data['main']['humidity']
            current_wind_speed = current_weather_data['wind']['speed']

            # Extract and process the 5-day forecast data
            forecasts = []
            for forecast in forecast_data['list']:
                date_time = datetime.fromtimestamp(forecast['dt'])
                temperature = forecast['main']['temp'] - 273.15
                weather_desc = forecast['weather'][0]['description']
                humidity = forecast['main']['humidity']
                wind_speed = forecast['wind']['speed']

                forecast_info = {
                    'date_time': date_time,
                    'temperature': temperature,
                    'weather_desc': weather_desc,
                    'humidity': humidity,
                    'wind_speed': wind_speed,
                }
                forecasts.append(forecast_info)

            context = {
                'location': location,
                'current_temp': current_temp,
                'current_weather_desc': current_weather_desc,
                'current_humidity': current_humidity,
                'current_wind_speed': current_wind_speed,
                'forecasts': forecasts,
            }
            return render(request, 'WAPI/mumbai.html', context)
        else:
            error_message = "Invalid City. Please check your City name."
            return render(request, 'WAPI/mumbai.html', {'error_message': error_message})

        return render(request, 'WAPI/mumbai.html')



def delhi(request):
    location = 'DELHI'
    user_api = 'fc5265634804c6a02f729536824e0220'

    # Construct the API URL
    current_weather_api_link = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={user_api}"
    forecast_api_link = f"https://api.openweathermap.org/data/2.5/forecast?q={location}&appid={user_api}"

    # Make requests to the APIs
    current_weather_api_response = requests.get(current_weather_api_link)
    forecast_api_response = requests.get(forecast_api_link)

    current_weather_data = current_weather_api_response.json()
    forecast_data = forecast_api_response.json()

    if current_weather_data['cod'] == 200 and forecast_data['cod'] == '200':
        # Process the current weather data
        current_temp = current_weather_data['main']['temp'] - 273.15
        current_weather_desc = current_weather_data['weather'][0]['description']
        current_humidity = current_weather_data['main']['humidity']
        current_wind_speed = current_weather_data['wind']['speed']

        # Extract and process the 5-day forecast data
        forecasts = []
        for forecast in forecast_data['list']:
            date_time = datetime.fromtimestamp(forecast['dt'])
            temperature = forecast['main']['temp'] - 273.15
            weather_desc = forecast['weather'][0]['description']
            humidity = forecast['main']['humidity']
            wind_speed = forecast['wind']['speed']

            forecast_info = {
                'date_time': date_time,
                'temperature': temperature,
                'weather_desc': weather_desc,
                'humidity': humidity,
                'wind_speed': wind_speed,
            }
            forecasts.append(forecast_info)

        context = {
            'location': location,
            'current_temp': current_temp,
            'current_weather_desc': current_weather_desc,
            'current_humidity': current_humidity,
            'current_wind_speed': current_wind_speed,
            'forecasts': forecasts,
        }
        return render(request, 'WAPI/delhi.html', context)
    else:
        error_message = "Invalid City. Please check your City name."
        return render(request, 'WAPI/delhi.html', {'error_message': error_message})

    return render(request, 'WAPI/delhi.html')


def bangalore(request):
    location = 'BANGALORE'
    user_api = 'fc5265634804c6a02f729536824e0220'

    # Construct the API URL
    current_weather_api_link = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={user_api}"
    forecast_api_link = f"https://api.openweathermap.org/data/2.5/forecast?q={location}&appid={user_api}"

    # Make requests to the APIs
    current_weather_api_response = requests.get(current_weather_api_link)
    forecast_api_response = requests.get(forecast_api_link)

    current_weather_data = current_weather_api_response.json()
    forecast_data = forecast_api_response.json()

    if current_weather_data['cod'] == 200 and forecast_data['cod'] == '200':
        # Process the current weather data
        current_temp = current_weather_data['main']['temp'] - 273.15
        current_weather_desc = current_weather_data['weather'][0]['description']
        current_humidity = current_weather_data['main']['humidity']
        current_wind_speed = current_weather_data['wind']['speed']

        # Extract and process the 5-day forecast data
        forecasts = []
        for forecast in forecast_data['list']:
            date_time = datetime.fromtimestamp(forecast['dt'])
            temperature = forecast['main']['temp'] - 273.15
            weather_desc = forecast['weather'][0]['description']
            humidity = forecast['main']['humidity']
            wind_speed = forecast['wind']['speed']

            forecast_info = {
                'date_time': date_time,
                'temperature': temperature,
                'weather_desc': weather_desc,
                'humidity': humidity,
                'wind_speed': wind_speed,
            }
            forecasts.append(forecast_info)

        context = {
            'location': location,
            'current_temp': current_temp,
            'current_weather_desc': current_weather_desc,
            'current_humidity': current_humidity,
            'current_wind_speed': current_wind_speed,
            'forecasts': forecasts,
        }
        return render(request, 'WAPI/bangalore.html', context)
    else:
        error_message = "Invalid City. Please check your City name."
        return render(request, 'WAPI/bangalore.html', {'error_message': error_message})

    return render(request, 'WAPI/bangalore.html')


def kolkata(request):
    location = 'KOLKATA'
    user_api = 'fc5265634804c6a02f729536824e0220'

    # Construct the API URL
    current_weather_api_link = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={user_api}"
    forecast_api_link = f"https://api.openweathermap.org/data/2.5/forecast?q={location}&appid={user_api}"

    # Make requests to the APIs
    current_weather_api_response = requests.get(current_weather_api_link)
    forecast_api_response = requests.get(forecast_api_link)

    current_weather_data = current_weather_api_response.json()
    forecast_data = forecast_api_response.json()

    if current_weather_data['cod'] == 200 and forecast_data['cod'] == '200':
        # Process the current weather data
        current_temp = current_weather_data['main']['temp'] - 273.15
        current_weather_desc = current_weather_data['weather'][0]['description']
        current_humidity = current_weather_data['main']['humidity']
        current_wind_speed = current_weather_data['wind']['speed']

        # Extract and process the 5-day forecast data
        forecasts = []
        for forecast in forecast_data['list']:
            date_time = datetime.fromtimestamp(forecast['dt'])
            temperature = forecast['main']['temp'] - 273.15
            weather_desc = forecast['weather'][0]['description']
            humidity = forecast['main']['humidity']
            wind_speed = forecast['wind']['speed']

            forecast_info = {
                'date_time': date_time,
                'temperature': temperature,
                'weather_desc': weather_desc,
                'humidity': humidity,
                'wind_speed': wind_speed,
            }
            forecasts.append(forecast_info)

        context = {
            'location': location,
            'current_temp': current_temp,
            'current_weather_desc': current_weather_desc,
            'current_humidity': current_humidity,
            'current_wind_speed': current_wind_speed,
            'forecasts': forecasts,
        }
        return render(request, 'WAPI/kolkata.html', context)
    else:
        error_message = "Invalid City. Please check your City name."
        return render(request, 'WAPI/.html', {'error_message': error_message})

    return render(request, 'WAPI/kolkata.html')





