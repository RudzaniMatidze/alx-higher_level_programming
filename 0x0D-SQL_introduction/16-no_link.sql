-- Lists all records of the table second_table in MySQL server.
-- Records are ordered by descending score.
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC;
