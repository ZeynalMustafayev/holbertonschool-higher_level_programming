-- genres
SELECT g.name AS genre, count(sg.show_id) AS number_of_shows FROM tv_show_genres sg LEFT JOIN tv_genres g ON sg.genre_id = g.id GROUP BY g.name ORDER BY 2 DESC;
