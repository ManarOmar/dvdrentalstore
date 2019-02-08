SELECT fa.film_id,f.title AS film_title, count(*) AS number_of_actors
FROM film_actor AS fa
JOIN film AS f 
ON fa.film_id = f.film_id
GROUP BY 1,2
ORDER BY 1

