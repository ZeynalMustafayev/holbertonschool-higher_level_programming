--shows by genre
SELECT s.title, g.name FROM tv_shows s LEFT JOIN tv_show_genres sg ON s.id = sg.show_id LEFT JOIN tv_genres g ON g.id = sg.genre_id ORDER BY 1, 2
ASC;
