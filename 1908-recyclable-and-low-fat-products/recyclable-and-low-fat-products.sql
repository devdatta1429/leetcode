with product as(
    select product_id
    from Products
    where low_fats = "Y" and recyclable = "Y")

select * 
from product;