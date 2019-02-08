# dvdrentalstore
The DVD rental database was ported from the sakila sample database for PostgreSQL with some adjustments.
The DVD rental database represents business processes of a DVD rental store. The DVD rental database has many objects including:


* 15 tables
* 1 trigger
* 7 views
* 8 functions
* 1 domain
*13 sequences

The queries here is answers on these questions:
1- You need a list of all the actors’ first name and last name?
2- Display the first and last name of each actor in a single column in upper case letters. Name the column Actor Name
3- You need to find the id, first name, and last name of an actor, of whom you know only the first name of "Joe." What is one query would you use to obtain this information?
4- Find all actors whose last name contain the letters GEN. Make this case insensitive
5- Find all actors whose last names contain the letters LI. This time, order the rows by last name and first name, in that order. Make this case insensitive.
6- Using IN, display the country_id and country columns of the following countries: Afghanistan, Bangladesh, and China
7- Add a middle_name column to the table actor. Specify the appropriate column type
8- List the last names of actors, as well as how many actors have that last name.
9- List last names of actors and the number of actors who have that last name, but only for names that are shared by at least two actors
10- List each film and the number of actors who are listed for that film. Use tables film_actor and film. Use inner join.
11-  Use a JOIN to display the total amount rung up by each staff member in January of 2007. Use tables staff and payment. You’ll have to google for this one, we didn’t cover it explicitly in class. 
12- Use a JOIN to display the first and last names, as well as the address, of each staff member. Use the tables staff and address
13- Using the tables payment and customer and the JOIN command, list the total paid by each customer. List the customers alphabetically by last name
14- The music of Queen and Kris Kristofferson have seen an unlikely resurgence. As an unintended consequence, films starting with the letters K and Q have also soared in popularity. display the titles of movies starting with the letters K and Q whose language is English.
15- Use subqueries to display all actors who appear in the film Alone Trip.
16- Write a query to display for each store its store ID, city, and country.
17- Write a query to display how much business, in dollars, each store brought in.
18- Display the most frequently rented movies in descending order.
19- You want to run an email marketing campaign in Canada, for which you will need the names and email addresses of all Canadian customers. Use joins to retrieve this information.
20- In your new role as an executive, you would like to have an easy way of viewing the Top five genres by gross revenue. Use the solution from the problem above to create a view. 
21- How would you display the view that you created in previous question?
22- You find that you no longer need the view top_five_genres. Write a query to delete it.
