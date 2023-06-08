# Write your MySQL query statement below
SELECT unique_id, name 
FROM Employees e1 LEFT OUTER JOIN EmployeeUNI e2 ON e1.id=e2.id