# SELECT * FROM sakila.customer;
# SELECT * FROM customer WHERE store_id = 2
SELECT 
    c.customer_id AS customer_id,
    CONCAT(c.first_name, ' ', c.last_name) AS name,
    COUNT(r.rental_id) AS number_of_rental
FROM customer AS c
JOIN rental AS r ON c.customer_id = r.customer_id
GROUP BY c.customer_id, c.first_name, c.last_name
ORDER BY number_of_rental DESC;
