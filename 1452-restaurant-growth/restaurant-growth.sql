with cte as (select visited_on,
                    sum(amount) as amount
            from Customer
            group by visited_on)
            ,
     qwe as(select visited_on, amount,
                            lag(amount,1) over (order by visited_on) as day_1,
                            lag(amount,2) over (order by visited_on) as day_2,
                            lag(amount,3) over (order by visited_on) as day_3,
                            lag(amount,4) over (order by visited_on) as day_4,
                            lag(amount,5) over (order by visited_on) as day_5,
                            lag(amount,6) over (order by visited_on) as day_6
            from cte)

select visited_on ,(amount + day_1 + day_2 + day_3 + day_4 + day_5 + day_6) as amount ,
                round((amount + day_1 + day_2 + day_3 + day_4 + day_5 + day_6)/7,2) as average_amount
from qwe
WHERE day_6 IS NOT NULL
ORDER BY visited_on;
                

-- WITH cte AS (
--     SELECT
--         visited_on,
--         SUM(amount) AS amount
--     FROM Customer
--     GROUP BY visited_on
-- ),
-- qwe AS (
--     SELECT
--         visited_on,
--         amount,
--         LAG(amount, 1) OVER (ORDER BY visited_on) AS day_1,
--         LAG(amount, 2) OVER (ORDER BY visited_on) AS day_2,
--         LAG(amount, 3) OVER (ORDER BY visited_on) AS day_3,
--         LAG(amount, 4) OVER (ORDER BY visited_on) AS day_4,
--         LAG(amount, 5) OVER (ORDER BY visited_on) AS day_5,
--         LAG(amount, 6) OVER (ORDER BY visited_on) AS day_6
--     FROM cte
-- )
-- SELECT
--     visited_on,
--     (amount + day_1 + day_2 + day_3 + day_4 + day_5 + day_6) AS amount,
--     ROUND(
--         (amount + day_1 + day_2 + day_3 + day_4 + day_5 + day_6) / 7,
--         2
--     ) AS average_amount
-- FROM qwe
-- WHERE day_6 IS NOT NULL
-- ORDER BY visited_on;