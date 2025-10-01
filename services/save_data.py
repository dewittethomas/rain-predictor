from utils import connect_to_db

def save_data(df, table_name):
    con, cur = connect_to_db('weather_data.db')
    df.to_sql(table_name, con, if_exists='replace', index=False)
    con.commit()