with exam as(
    select e.id,
            e.name as Employee,
            e.salary as Salary,
            e.departmentId ,
            d.id as de,
            d.name as Department,
            dense_rank() over (partition by d.id order by e.salary desc) as rnk
    from Employee e join Department d on e.departmentId=d.id
)

select Department, Employee, Salary
from exam 
where rnk <=3;