-- with rank_year as(
--     select user_id,
--     time_stamp as last_stamp,rank() over (partition by user_id order by time_stamp desc) as year_rank
--     from Logins
--     where year(time_stamp)=2020 
-- )
-- select user_id,last_stamp
-- from rank_year
-- where year_rank=1;

select user_id,
       max(time_stamp) as last_stamp
from Logins
where year(time_stamp) = 2020
group by user_id;