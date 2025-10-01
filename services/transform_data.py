import pandas as pd
import numpy as np

def transform_data(data):
    df = pd.DataFrame(data['daily'])

    df['rain_flag'] = (df['rain_sum'] > 0).astype(int)
    df['rain_yesterday'] = df['rain_sum'].shift(1).fillna(0)
    df['temp_3day_avg'] = df['temperature_2m_mean'].rolling(3).mean().bfill()
    df['month'] = pd.to_datetime(df['time']).dt.month
    df['day_of_year'] = pd.to_datetime(df['time']).dt.dayofyear
    df['wind_dir_sin'] = np.sin(np.radians(df['wind_direction_10m_dominant']))
    df['wind_dir_cos'] = np.cos(np.radians(df['wind_direction_10m_dominant']))

    return df