with ref_id_2 as(
    select name
    from Customer
    where referee_id != 2 or referee_id is null
)

select * 
from ref_id_2;