import functions
import psycopg2 as pg2
import pandas as pd
import numpy as np
from dotenv import load_dotenv
from pathlib import Path
import os

import sys
sys.path.insert(0, '../src')
sys.path.insert(0, '../data')


load_dotenv()

DATABASE = os.getenv('PG_DATABASE')
USER = os.getenv('PG_USER')
PASSWORD = os.getenv('PG_PASSWORD')
HOST = os.getenv('PG_HOST')
PORT = os.getenv('PG_PORT')

print(DATABASE)
print(USER)

conn = pg2.connect(dbname=DATABASE,
                   user=USER,
                   password=PASSWORD,
                   host=HOST,
                   port=PORT)

c = conn.cursor()

query1 = functions.create_query_string('sql_queries/employee_info.sql')


c.execute(query1)


columns = [desc[0] for desc in c.description]
data = c.fetchall()
df = pd.DataFrame(list(data), columns=columns)

writer = pd.ExcelWriter('excel_reports/employee_info.xlsx')
df.to_excel(writer, sheet_name='Employee Info')
writer.save()


conn.commit()
conn.close()
