/* Sacando el top 10 de rentas*/

SELECT ROW_NUMBER() OVER (
	ORDER BY COUNT(*) DESC) AS lugar, peliculas.pelicula_id,
	peliculas.titulo, COUNT(*) AS numero_rentas
FROM peliculas
INNER JOIN inventarios ON peliculas.pelicula_id = inventarios.pelicula_id
INNER JOIN rentas ON inventarios.inventario_id = rentas.inventario_id
GROUP BY peliculas.pelicula_id
ORDER BY numero_rentas DESC
LIMIT 10;

/* IMPORTANTE

    En el query pasado, lo mas importante y novedoso es :

    SELECT ROW_NUMBER() OVER (
	ORDER BY COUNT(*) DESC) AS lugar

    Lo que sucede, es que se necesita un campo propio con el ranking para que un dashboard pueda mostrarlo.

    El anterior query utiliza la window function ROW_NUMBER() OVER() para llenar un campo con el orden de filas
*/
