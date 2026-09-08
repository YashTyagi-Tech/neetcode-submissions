-- Write your query below
SELECT customers.name from customers LEFT JOIN orders on customers.id=orders.customer_id WHERE orders.id IS NULL