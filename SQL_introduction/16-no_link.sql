-- not null
SELECT score, name FROM second_table WHERE NAME != '' or NAME IS NOT NULL ORDER BY score DESC;
