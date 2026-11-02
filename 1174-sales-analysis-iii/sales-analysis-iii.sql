-- select p.product_id,p.product_name
-- from Sales s join Product p on s.product_id=p.product_id
-- group by p.product_id 
-- having min(s.sale_date) >= '2019-01-01' and max(s.sale_date) <= '2019-03-31'
-- order by p.product_id; 
SELECT p.product_id, p.product_name
FROM Product p
JOIN Sales s
    ON p.product_id = s.product_id
GROUP BY p.product_id, p.product_name
HAVING MIN(s.sale_date) >= '2019-01-01'
   AND MAX(s.sale_date) <= '2019-03-31';