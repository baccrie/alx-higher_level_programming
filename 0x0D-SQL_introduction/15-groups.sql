-- selects with caution
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER  BY SCORE DESC;
