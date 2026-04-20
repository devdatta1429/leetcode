with emails_keep as (
    select min(id) as id
    from person
    group by email
)

delete from person
where id not in (select id from emails_keep); 

-- with keep_ids as (
--     select min(id) as id
--     from person
--     group by email
-- )

-- delete from person
-- where id not in (
--     select id from keep_ids
-- );