# Write your MySQL query statement below

with never_order as (
    select c.name as customers,count(o.customerId) as have
    from customers c left join orders o on c.id=o.customerId
    group by c.id
)
select Customers
from never_order
where have=0;