with cte as(
    select  id, visit_date,people,
                            lag(people,1) over (order by id) as prev1,
                            lag(people,2) over (order by id) as prev2, 
                            lead(people,1) over (order by id) as lead1,
                            lead(people,2) over (order by id) as lead2
    from Stadium 
)

select  id, visit_date, people 
from cte
-- where people >= 100 and lead1 >=100 and lead2 >=100 or
--       people >= 100 and prev1 >=100 and prev2 >=100 or
--       people >= 100 and prev1 >=100 and lead1 >=100 

where people >= 100 and ( (lead1 >=100 and lead2 >=100) or
                          (prev1 >=100 and prev2 >=100) or 
                          (prev1 >=100 and lead1 >=100))
order by visit_date;