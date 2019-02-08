SELECT s.staff_id, s.first_name, s.last_name, a.address AS staff_address
FROM staff AS s
JOIN address AS a
ON a.address_id = s.address_id
