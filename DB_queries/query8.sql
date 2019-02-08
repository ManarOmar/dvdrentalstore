SELECT a.actor_id, t1.last_name, t1.last_name_count
FROM (
    SELECT last_name, count(*) AS last_name_count
    FROM actor
    GROUP BY 1) AS t1
JOIN actor AS a
ON a.last_name = t1.last_name