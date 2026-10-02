with cte as(
select num,
        lag(num,1) over(order by id) as num1,
        lag(num,2) over(order by id) as num2
from logs)



select distinct(num) as ConsecutiveNums 
from cte
where num = num1 and num = num2;