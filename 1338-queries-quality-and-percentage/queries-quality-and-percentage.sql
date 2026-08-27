with result as (
    select query_name,
            result,
            position,
            rating,
            (rating/position) as sub_rating
    from Queries
)

select query_name,
        round(avg(sub_rating),2) as quality,
        round(sum(rating < 3)*100 /count(*),2) as  poor_query_percentage
from result
group by query_name;