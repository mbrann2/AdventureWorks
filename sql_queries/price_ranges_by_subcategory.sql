DROP TABLE IF EXISTS product_with_subcategory;
CREATE TEMP TABLE product_with_subcategory AS (SELECT productsubcategory.productcategoryid,
											   productsubcategory.productsubcategoryid AS sub_id,
											   productsubcategory.name AS subcategory_name,
												product.listprice
											   FROM production.productsubcategory
											   JOIN production.product
											   USING (productsubcategoryid)) 
;
DROP TABLE IF EXISTS product_id_prices;
CREATE TEMP TABLE product_id_prices AS (SELECT productcategory.name AS product_name,
										productcategoryid as cat_id,
										subcategory_name,
										sub_id,
										listprice
										FROM product_with_subcategory
										JOIN production.productcategory
										USING (productcategoryid))
;

SELECT 	product_name AS "Category Name",
		subcategory_name AS "Subcategory Name",
		MIN(listprice) AS "Minimum Price",
		MAX(listprice) AS "Maximum Price",
		MAX(listprice) - MIN(listprice) AS "Price Differential",
		count(*) AS "Number of Products"
FROM product_id_prices
GROUP BY product_name, subcategory_name
ORDER BY product_name
;