# Write your MySQL query statement below

SELECT name FROM customer where id not in (select id from customer where referee_id=2)

# select nAme from cusTomer where referee_id != 2 or referee_id is NULL