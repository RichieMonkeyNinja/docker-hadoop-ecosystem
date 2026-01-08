with inactive_avg as (
	SELECT d.neighbourhood_cleansed as neighbourhood, AVG(f.price) as avg_price
	FROM clickhouse.airbnb_gold.fct_listings f join
	clickhouse.airbnb_gold.dim_listings d on d.id = f.id
	WHERE last_review <= CURRENT_DATE - INTERVAL '6' month and from_utf8(city) ='edinburgh'
	group by d.neighbourhood_cleansed
	),
		active_avg as (
		SELECT d.neighbourhood_cleansed as neighbourhood, AVG(f.price) as avg_price_6m
		FROM clickhouse.airbnb_gold.fct_listings f join
		clickhouse.airbnb_gold.dim_listings d on d.id = f.id
		WHERE last_review >= CURRENT_DATE - INTERVAL '6' month and from_utf8(city) ='edinburgh'
		group by d.neighbourhood_cleansed
	
		)
		select count(*) from inactive_avg i
		join active_avg a on i.neighbourhood = a.neighbourhood 
		where i.avg_price > a.avg_price_6m;
	
	
