# Write your MySQL query statement below
SELECT product_name,year,price 
FROM Sales s LEFT OUTER JOIN Product p ON s.product_id=p.product_id