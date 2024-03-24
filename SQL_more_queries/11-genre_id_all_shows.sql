-- genre id
SELECT s.title, g.genre_id FROM tv_show_genres g RIGHT JOIN tv_shows s ON s.id = g.show_id ORDER BY s.title, g.genre_id;
