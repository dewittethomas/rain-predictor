import requests

def fetch_api_data(lat, long, start_date, end_date, tz="Europe/Berlin"):
    api_url = f'https://archive-api.open-meteo.com/v1/archive?latitude={lat}&longitude={long}&start_date={start_date}&end_date={end_date}&daily=temperature_2m_min,temperature_2m_max,temperature_2m_mean,rain_sum,wind_speed_10m_max,wind_direction_10m_dominant,precipitation_sum,sunshine_duration,shortwave_radiation_sum,wind_gusts_10m_max&timezone={tz}'
    res = requests.get(api_url)
    data = res.json()
    return data