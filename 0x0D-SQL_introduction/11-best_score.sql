-- Lists all records in the table second table with a score
-- Records are arranged in descending score.
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;