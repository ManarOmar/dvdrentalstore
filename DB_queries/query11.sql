SELECT s.staff_id, s.first_name, SUM(p.amount) AS rung_up ,DATE_PART('month',payment_date) AS rung_month
FROM payment AS P
JOIN staff AS s
ON p.staff_id = s.staff_id
WHERE payment_date BETWEEN '2007-01-01' AND '2007-02-01'
GROUP BY 1,2,4