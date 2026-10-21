select actor_id,director_id
from ActorDirector
group by actor_id,director_id
having count(*) >= 3;



-- with cte as(
-- select actor_id, director_id, count(*) over (partition by actor_id,director_id) as maxs
-- from ActorDirector
-- )

-- select distinct actor_id, director_id
-- from cte
-- where maxs >=3;