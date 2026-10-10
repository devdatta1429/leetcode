with asd as (
    select date_format(trans_date,'%Y-%m') as month ,
            country,
            count(*) as trans_count,
            sum(amount) as trans_total_amount
    from Transactions
    group by date_format(trans_date,'%Y-%m'), country
),
qwe as (
    select date_format(trans_date,'%Y-%m') as month,
            country,
            count(*) as approved_count,
            sum(amount) as approved_total_amount 
    from Transactions
    where state='approved'
    group by date_format(trans_date,'%Y-%m'), country
)

select a.month as month,
        a.country, 
        a.trans_count, 
        coalesce(q.approved_count, 0) as approved_count, 
        a.trans_total_amount, 
        coalesce(q.approved_total_amount, 0) as approved_total_amount
from asd a left join qwe q 
    on a.month = q.month and
     a.country <=> q.country;