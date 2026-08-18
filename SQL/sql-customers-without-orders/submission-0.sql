-- Write your query below
SELECT c.name
FROM customers c
LEFT JOIN orders o
ON c.id = o.customer_id
WHERE c.id  NOT IN (SELECT o.customer_id FROM orders o)
ORDER BY c.name