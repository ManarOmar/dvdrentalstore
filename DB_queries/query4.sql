SELECT actor_id, first_name, last_name
FROM actor
WHERE LOWER(last_name) LIKE '%gen%' 