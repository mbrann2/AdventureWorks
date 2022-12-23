import functions
import psycopg2 as pg2
import pandas as pd
import numpy as np
from dotenv import load_dotenv
from pathlib import Path
import os


def create_query_string(sql_full_path):
    with open(sql_full_path, 'r') as f_in:
        lines = f_in.read()

    return lines


def database_connection():

    load_dotenv()

    database = os.getenv('PG_DATABASE')
    user = os.getenv('PG_USER')
    password = os.getenv('PG_PASSWORD')
    host = os.getenv('PG_HOST')
    port = os.getenv('PG_PORT')

    conn = pg2.connect(dbname=database,
                       user=user,
                       password=password,
                       host=host,
                       port=port)

    return conn


def sql_to_excel(filein, fileout, sheetname='sheet'):

    connection = functions.database_connection()

    cursor = connection.cursor()

    # read sql query
    query1 = functions.create_query_string(filein)

    cursor.execute(query1)

    columns = [desc[0] for desc in cursor.description]
    data = cursor.fetchall()
    df = pd.DataFrame(list(data), columns=columns)

    writer = pd.ExcelWriter(fileout)
    df.to_excel(writer, sheet_name=sheetname)
    writer.save()

    connection.commit()
    connection.close()


if __name__ == "__main__":

    final_out('sql_queries/employee_info.sql',
              'excel_reports/employee_info.xlsx', 'Employee Info')
