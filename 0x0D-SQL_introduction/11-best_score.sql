-- Script that that lists all records of the table ordered by score (top first)
SELECT score, name 
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
