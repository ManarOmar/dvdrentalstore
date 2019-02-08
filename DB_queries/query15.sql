SELECT actor_id, first_name, last_name
FROM (SELECT f.title, a.actor_id, a.first_name, a.last_name
      FROM film AS f
      JOIN film_actor AS fa
      ON fa.film_id = f.film_id
      JOIN actor AS a
      ON a.actor_id = fa.actor_id
      WHERE f.title = 'Alone Trip')AS t1