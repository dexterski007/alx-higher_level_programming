-- list shows and genres
SELECT name
FROM tv_genres
WHERE name not IN
(SELECT name
FROM tv_genres
JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_shows.title = 'Dexter')
ORDER BY tv_genres.name ASC;
