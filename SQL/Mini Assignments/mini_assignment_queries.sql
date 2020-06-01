SELECT f.title,
	(SELECT COUNT (i.film_id) FROM inventory i where i.film_id = f.film_id) as num_of_copy
	FROM film f
	order by f.title;

CREATE VIEW title_count AS
	SELECT f.title,
	(SELECT COUNT (i.film_id) FROM inventory i WHERE i.film_id = f.film_id) as num_of_copy
	FROM film f
	ORDER BY f.title;
SELECT * FROM title_count;

SELECT * FROM title_count where num_of_copy =7;