SELECT c.customer_id, c.last_name, SUM(p.amount) AS total_paid
FROM customer AS c
JOIN payment AS p
ON c.customer_id = p.customer_id
GROUP BY 1,2
ORDER BY 2

 
 