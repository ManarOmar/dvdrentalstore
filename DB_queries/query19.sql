SELECT cus.first_name,cus.last_name,cus.email
FROM customer AS cus
JOIN address AS a
ON cus.address_id = a.address_id
JOIN city AS ci 
ON ci.city_id = a.city_id
JOIN country AS co
ON co.country_id = ci.country_id
WHERE co.country = 'Canada'
