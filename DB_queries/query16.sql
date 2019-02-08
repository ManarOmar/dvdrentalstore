SELECT s.store_id, ci.city, co.country
FROM store AS S
JOIN address as a
ON a.address_id = s.address_id
JOIN city AS ci
ON ci.city_id = a.city_id
JOIN country AS co
ON co.country_id = ci.country_id 