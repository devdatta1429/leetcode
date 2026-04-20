with bonus_sal as (
    select employee_id,if ((employee_id%2)=1 and name not like 'M%',salary,0) as bonus
    from employees
)
select e.employee_id ,b.bonus
from employees e left join bonus_sal b on e.employee_id= b.employee_id
order by employee_id;