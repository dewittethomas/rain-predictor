import sqlite3

def connect_to_db(db_name):
    con = sqlite3.connect(db_name)
    cur = con.cursor()
    return con, cur