-- Lists all records of the second table having a name value in MySQL server.
-- Arranges in descending order
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC