SELECT f.film_id, f.title, l.name AS name_language
FROM film AS f
JOIN language AS l
ON f.language_id = l.language_id
WHERE f.title like 'Q%' OR f.title like 'K%'AND l.name = 'English' 