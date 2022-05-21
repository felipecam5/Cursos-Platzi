/* Ejemplo de una funcion con variables */

CREATE OR REPLACE FUNCTION movies_stats()
RETURNS VOID
LANGUAGE plpgsql
AS $$
DECLARE /* Las funciones se declaran dentro de la sentencia "DECLARE*/
    total_rated_r REAL := 0.0;
    total_larged_than_100 REAL :=0.0;
    total_published_2006 REAL := 0.0; /* Las variables se definen con el tipo (En este caso "REAL") y se inicializan con := */
    average_duracion REAL := 0.0;
    average_rental_price REAL :=0.0;
BEGIN
    total_rated_r := COUNT(*) FROM peliculas WHERE clasificacion = 'R';
    total_larged_than_100 := COUNT(*) FROM peliculas WHERE duracion > 100;
    total_published_2006 := COUNT(*) FROM pelicuas WHERE anio_publicacion = 2006; /* En esta parte, se guardan las consulatas en las variables*/
    average_duracion := AVG(duracion) FROM peliculas;
    average_rental_price := AVG(precio_renta) FROM peliculas;

    TRUNCATE TABLE peliculas_estadisticas; /* El Truncate Table quickly removes all rows from a set of tables*/

    INSERT INTO peliculas_estadisticas (tipo_estadistica, total)
    VALUES 
        ('Peliculas con clasificacion R', total_rated_r),
        ('Peliculas de mas de 100 minutos', total_larged_than_100),
        ('Peliculas publicadas en 2006', total_published_2006), /* Aqui inserto en la tabla peliculas_estadisticas, las variables*/
        ('Promedio de duracion en minutos',average_duracion ),
        ('Precio promedio de renta',average_rental_price );
END
$$;

SELECT movies_stats(); /* Corre la funcion*/