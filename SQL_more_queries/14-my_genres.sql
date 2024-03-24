-- my genres
SELECT g.name AS name FROM tv_genres g INNER JOIN tv_show_genres sg ON g.id = sg.genre_id INNER JOIN tv_shows s ON s.id = sg.show_id WHERE s.title = 'Dexter' ORDER BY g.name ASC;
