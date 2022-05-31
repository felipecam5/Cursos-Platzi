/* Utilizando el DENSE_RANK() no se salta posiciones así hayan ranking repetidos*/
SELECT DENSE_RANK () OVER (
	ORDER BY COUNT(*) DESC) AS lugar, peliculas.pelicula_id,
	peliculas.titulo, COUNT(*) AS numero_rentas
FROM peliculas
INNER JOIN inventarios ON peliculas.pelicula_id = inventarios.pelicula_id
INNER JOIN rentas ON inventarios.inventario_id = rentas.inventario_id
GROUP BY peliculas.pelicula_id
ORDER BY numero_rentas DESC


/* Utilizando el RANK() se salta posiciones asi hay ranking repetidos*/

SELECT RANK() OVER (
	ORDER BY COUNT(*) DESC) AS lugar, peliculas.pelicula_id,
	peliculas.titulo, COUNT(*) AS numero_rentas
FROM peliculas
INNER JOIN inventarios ON peliculas.pelicula_id = inventarios.pelicula_id
INNER JOIN rentas ON inventarios.inventario_id = rentas.inventario_id
GROUP BY peliculas.pelicula_id
ORDER BY numero_rentas DESC

/*Rango percentil*/

SELECT PERCENT_RANK() OVER (
	ORDER BY COUNT(*) DESC) AS lugar, peliculas.pelicula_id,
	peliculas.titulo, COUNT(*) AS numero_rentas
FROM peliculas
INNER JOIN inventarios ON peliculas.pelicula_id = inventarios.pelicula_id
INNER JOIN rentas ON inventarios.inventario_id = rentas.inventario_id
GROUP BY peliculas.pelicula_id
ORDER BY numero_rentas DESC
