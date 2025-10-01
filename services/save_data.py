import sqlite3

con = sqlite3.connect('weather_data.db')
cur = con.cursor()

def save_data(df, table_name):
    df.to_sql(table_name, con, if_exists='replace', index=False)
    con.commit()