-- List number with same secore in second_table

SELECT score, COUNT(1) AS number FROM second_table GROUP BY score ORDER BY number DESC;
