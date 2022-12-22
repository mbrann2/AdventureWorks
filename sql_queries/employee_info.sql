CREATE TEMP TABLE name_and_position AS (SELECT person.businessentityid,
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
;