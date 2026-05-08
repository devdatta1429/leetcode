with movie as (
    select * 
    from Cinema
    where id % 2 = 1
)
select * 
from movie
where description != 'boring'
order by rating desc;