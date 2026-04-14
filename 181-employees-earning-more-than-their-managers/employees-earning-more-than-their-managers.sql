with high_sal as(
    select id,name,salary,managerId
    from employee
)
select e.name as employee
from employee as e join high_sal as h on e.managerId=h.id
where e.salary > h.salary
