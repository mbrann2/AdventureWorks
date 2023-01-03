import functions
import psycopg2 as pg2
import pandas as pd
import numpy as np
import glob
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


def sql_to_excel(folderin, folderout):

    connection = functions.database_connection()

    cursor = connection.cursor()

    os.chdir(folderin)
    # read sql query
    for file in glob.glob('*.sql'):
        SQLQuery = functions.create_query_string(file)
        cursor.execute(SQLQuery)

        columns = [desc[0] for desc in cursor.description]
        data = cursor.fetchall()
        df = pd.DataFrame(list(data), columns=columns)

        writer = pd.ExcelWriter(f'{folderout}{file}.xlsx')
        df.to_excel(writer, sheet_name=sheetname)
        writer.save()

    connection.commit()
    connection.close()


if __name__ == "__main__":

    sql_to_excel('sql_queries/', '../excel_reports/')
