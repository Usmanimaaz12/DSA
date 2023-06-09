SELECT customer_id, COUNT(v.visit_id) as count_no_trans
FROM Visits v LEFT OUTER JOIN Transactions t ON v.visit_id=t.visit_id
WHERE transaction_id is NULL 
GROUP BY customer_id