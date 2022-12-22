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

connection = functions.database_connection()
cursor = connection.cursor()

query1 = functions.create_query_string('sql_queries/over_threshold.sql')

cursor.execute(query1)

columns = [desc[0] for desc in cursor.description]
data = cursor.fetchall()
df = pd.DataFrame(list(data), columns=columns)

writer = pd.ExcelWriter('excel_reports/employees_over_threshold.xlsx')
df.to_excel(writer, sheet_name= 'Employees Over Vacation Hours Threshold')
writer.save()


connection.commit()
connection.close()