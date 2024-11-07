import requests

Latitude = '16.505329'
Longitude = '80.661209'


def extract_weather_data():
    """ Extract weather data from Open-Meteo API """
    endpoint = f"https://api.open-meteo.com/v1/forecast?latitude={Latitude}&longitude={Longitude}&current_weather=True"

    response = requests.get(endpoint)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch weather data:{response.status_code}")

def transform_weather_data(weather_data):
    """Transform the Extracted weather data"""
    current_weather = weather_data['current_weather']
    transformed_data = {
        "Latitude"  : Latitude,
        "Longitude" : Longitude,
        "temperature" : current_weather['temperature'],
        "windspeed" : current_weather['windspeed'],
        "winddirection" : current_weather['winddirection'],
        "weathercode" : current_weather['weathercode'],
    }

    return transformed_data




