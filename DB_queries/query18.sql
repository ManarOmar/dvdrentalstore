SELECT f.film_id, f.title, count(*) AS frequency_rental
FROM rental AS r
JOIN inventory AS i
ON i.inventory_id = r.inventory_id
JOIN film AS f
ON f.film_id = i.film_id
GROUP BY 1,2
ORDER BY 3 DESC