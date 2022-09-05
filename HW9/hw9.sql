SELECT a.Title'Album name', g.Name'Genre', t.Composer'Artist or Group', ROUND(SUM(t.Milliseconds)/60000.0)'Duration(Minutes)',
ROUND((SUM(t.Bytes))/1048576.0, 2)', SUM(t.UnitPrice)'Album Price', COUNT(t.Name)'Count Tracks'
FROM albums a
	JOIN tracks t on a.AlbumId = t.AlbumId
	JOIN genres g on t.GenreId = g.GenreId
	JOIN artists ar on a.ArtistId = ar.ArtistId
	JOIN media_types mt on t.MediaTypeId = mt.MediaTypeId
WHERE mt.Name = 'MPEG audio file'
GROUP BY a.AlbumId
ORDER BY g.Name ASC, ar.Name ASC
