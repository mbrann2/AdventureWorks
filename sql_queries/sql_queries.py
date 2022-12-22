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

conn = pg2.connect(dbname=DATABASE,
                   user=USER,
                   password=PASSWORD,
                   host=HOST,
                   port=PORT)

c = conn.cursor()

query1 = ''' CREATE TEMP TABLE name_and_position AS (SELECT person.businessentityid,
										person.firstname, 
										person.lastname,
										employee.jobtitle,
										employee.vacationhours
										FROM person.person
										JOIN humanresources.employee
										USING (businessentityid))
;

CREATE TEMP TABLE employee_info AS (SELECT firstname "First Name",
									lastname "Last Name",
									jobtitle "Job Title",
									vacationhours "Vacation Hours",
									emailaddress.emailaddress "Email Address"
									FROM name_and_position
									JOIN person.emailaddress
									USING (businessentityid))
;

            SELECT *
			FROM employee_info
			WHERE "Vacation Hours" >= 40
			ORDER BY "Vacation Hours" DESC
;'''

c.execute(query1)


columns = [desc[0] for desc in c.description]
data = c.fetchall()
df = pd.DataFrame(list(data), columns=columns)

writer = pd.ExcelWriter('excel_reports/employee_info.xlsx')
df.to_excel(writer, sheet_name='Employee Info')
writer.save()


conn.commit()
conn.close()
