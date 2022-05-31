/* Recordatorio de como utilizar date_part para extraer partes de fechas.*/

SELECT date_part('year', rentas.fecha_renta) AS anio,
	date_part('month', rentas.fecha_renta) AS mes,
	peliculas.titulo, COUNT(*) as numero_rentas
FROM rentas
	INNER JOIN inventarios ON rentas.inventario_id = inventarios.inventario_id
	INNER JOIN peliculas ON peliculas.pelicula_id = inventarios.pelicula_id
GROUP BY anio, mes, peliculas.titulo
ORDER BY peliculas.titulo;

SELECT date_part('year', rentas.fecha_renta) AS anio,
	date_part('month', rentas.fecha_renta) AS mes,
	COUNT(*) AS numero_rentas
FROM rentas
	GROUP BY anio, mes
	ORDER BY anio,mes;