

select f.id,f.host_id,d.property_type,f.price FROM clickhouse.airbnb_gold.dim_listings d
join clickhouse.airbnb_gold.fct_listings f
on d.id =f.id
where from_utf8(f.city) = 'london' and from_utf8(d.property_type) = 'Entire cottage'
order by f.price;



