/* Agregación de datos - Utilizar funciones MAX, MIN, COUNT para sacar totales o sumarizar información*/

SELECT MAX(precio_renta) FROM peliculas; /* Funcion MAX*/

SELECT titulo, MAX(precio_renta) FROM peliculas
GROUP BY titulo;

SELECT MIN(precio_renta) FROM peliculas;

SELECT titulo, MIN(precio_renta) FROM peliculas /* Función MIN*/
GROUP BY titulo;

SELECT SUM(precio_renta) FROM peliculas; /* Función SUM*/

SELECT clasificacion, COUNT(*) FROM peliculas /* Función COUNT*/
GROUP BY clasificacion;

SELECT AVG(precio_renta) FROM peliculas; /* Función AVG*/

SELECT clasificacion, AVG(precio_renta) AS precio_promedio FROM peliculas
GROUP BY clasificacion
ORDER BY precio_promedio DESC;

SELECT clasificacion, AVG(duracion) AS duracion_promedio FROM peliculas
GROUP BY clasificacion
ORDER BY duracion_promedio DESC;

SELECT clasificacion, AVG(duracion_renta) AS duracion_renta_promedio FROM peliculas
GROUP BY clasificacion
ORDER BY duracion_renta_promedio DESC;