import psycopg2 as pg2
import pandas as pd
import numpy as np
from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv()

DATABASE = os.getenv('PG_DATABASE')
USER = os.getenv('PG_USER')
PASSWORD = os.getenv('PG_PASSWORD')
HOST = os.getenv('PG_HOST')
PORT = os.getenv('PG_PORT')

print(DATABASE)
print(USER)

conn = pg2.connect(dbname=PG_DATABASE,
                   user=PG_USER,
                   password=PG_PASSWORD,
                   host=PG_HOST,
                   port=PG_PORT)

c = conn.cursor()

query = ''' select *
            from person.person
            limit 10;'''


c.execute(query)

for row in c:
    print(row)


conn.commit()
conn.close()
