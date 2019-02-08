SELECT store.store_id, SUM(amount)
FROM store
JOIN staff
ON store.store_id = staff.store_id
JOIN payment
ON payment.staff_id = staff.staff_id 
GROUP BY 1
ORDER BY 2