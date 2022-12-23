SELECT
		date_part('year', date(orderdate))::integer as "Year",
		date_part('month', date(orderdate))::integer as "Month",
		cast(sum(subtotal) AS money) as "Subtotal",
		count(*) AS "Orders per Month"
FROM sales.salesorderheader
GROUP BY "Year", "Month"
ORDER BY "Year", "Month"
LIMIT 30
;