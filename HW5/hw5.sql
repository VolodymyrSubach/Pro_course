SELECT t.TrackId, t.Name, t.Composer, a.Title, SUM(ii.UnitPrice), COUNT(ii.Quantity)
FROM invoice_items AS ii
	JOIN invoices AS i ON ii.InvoiceId = i.InvoiceId
	JOIN customers AS c ON i.CustomerId = c.CustomerId
	JOIN tracks AS t ON ii.TrackId = t.TrackId
	JOIN albums AS a ON t.AlbumId = a.AlbumId
GROUP BY ii.TrackId