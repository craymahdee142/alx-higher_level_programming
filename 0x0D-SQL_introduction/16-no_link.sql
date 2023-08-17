-- List all rec records of the second_table

SELECT score, name FROM second_table name IS NOT NULL AND name != '' ORDER BY score DESC;
