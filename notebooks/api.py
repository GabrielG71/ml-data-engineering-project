
import requests
import time

def get_weather(lat, lon, date):
  #Obtendo dados da API, utilizamos os parâmetros latitude, longitude, data inicial e final, para obter a temperatura, precipitação e weathercode.
  try:
    url = "https://archive-api.open-meteo.com/v1/archive"
    params = {
        "latitude": lat,
        "longitude": lon,
        "start_date": date,
        "end_date": date,
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum,weathercode",
        "timezone": "America/Sao_Paulo"
    }
    #Fazendo requisição
    r = requests.get(url, params=params)
    r.raise_for_status()
    return r.json()
  except Exception:
    return None