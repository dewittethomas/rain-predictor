from pandas import df

def train_model(data):
    X = df.drop(columns=['rain_flag', 'time'])
    y = df['rain_flag']

    

