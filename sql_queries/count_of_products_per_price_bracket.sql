select 
		case when listprice > 0 and listprice <= 10    then 'A'
           when listprice > 10 and listprice <= 25   then 'B'
		   when listprice > 25 and listprice <= 50  then 'C'
		   when listprice > 50 and listprice <= 100 then 'D'
			when listprice > 100 and listprice <= 500 then 'E'
			when listprice > 500 and listprice <= 1000 then 'F'
			when listprice > 1000 and listprice <= 2000 then 'G'
           else 'H'
      end "Price Bracket",
      case when listprice > 0 and listprice <= 10    then '1 - 10'
           when listprice > 10 and listprice <= 25   then '11 - 25'
		   when listprice > 25 and listprice <= 50  then '26 - 50'
		   when listprice > 50 and listprice <= 100 then '51 - 100'
			when listprice > 100 and listprice <= 500 then '101 - 500'
			when listprice > 500 and listprice <= 1000 then '501 - 1000'
			when listprice > 1000 and listprice <= 2000 then '1001 - 2000'
			else 'over 2000'
      end "Price Range",
      count(*) as "Total Within Range"
   from
      production.product
	  group by 1, 2
		order by 1
;