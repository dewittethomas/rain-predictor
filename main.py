import os
from dotenv import load_dotenv

import requests
import pandas as pd
from sqlalchemy import create_engine

load_dotenv()

postgres_host = os.getenv("POSTGRES_HOST")
postgres_user = os.getenv("POSTGRES_USER")  
postgres_password = os.getenv("POSTGRES_PASSWORD")
postgres_db = os.getenv("POSTGRES_DB")

engine = create_engine(f'postgresql://{postgres_user}:{postgres_password}@{postgres_host}:5432/{postgres_db}')

API_URL = "https://archive-api.open-meteo.com/v1/archive?latitude=51.2155&longitude=2.927&start_date=2015-09-01&end_date=2025-09-01&daily=temperature_2m_min,temperature_2m_max,temperature_2m_mean,rain_sum,wind_speed_10m_max,wind_direction_10m_dominant,precipitation_sum,sunshine_duration,shortwave_radiation_sum,wind_gusts_10m_max&timezone=Europe%2FBerlin"
res = requests.get(API_URL)
data = res.json()

df = pd.DataFrame(data['daily'])
df.to_sql('rain_prediction', engine, if_exists='replace')