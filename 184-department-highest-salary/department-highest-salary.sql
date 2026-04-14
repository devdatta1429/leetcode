# Write your MySQL query statement below
with high_sal as(
    select e.departmentid,e.name as Employee,e.salary,d.name as department, 
    dense_rank()over(partition by e.departmentid order by e.salary desc) as as_sal
    from Employee e join department d on e.departmentid=d.id
)

select department,employee,salary
from high_sal
where as_sal=1;
