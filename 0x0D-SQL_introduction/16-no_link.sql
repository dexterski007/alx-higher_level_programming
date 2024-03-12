-- list all records with exceptions
SELECT score, name
FROM second_table
WHERE name != ''
ORDER BY score DESC;
