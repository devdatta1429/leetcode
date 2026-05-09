with cmd as (
    select contest_id , count(*) as count1
    from Register
    group by contest_id)


# Write your MySQL query statement below
select contest_id, round(( count1/ (select count(*) from users) * 100),2) as percentage 
from cmd
order by percentage desc, contest_id asc;