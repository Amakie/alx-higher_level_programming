-- Lists the number of records with the same score in the second table in MySQL server.
-- Arranges in descending order
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;