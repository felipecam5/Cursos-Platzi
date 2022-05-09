SELECT *
FROM generate_series(1,4, 0.2)

SELECT *
FROM generate_series(5,1, -2)

SELECT *
FROM generate_series(4,4);

SELECT *
FROM generate_series(1.1,4.1,1.3);

SELECT current_date + s.a AS dates
FROM generate_series(0,14,7) AS s(a);

SELECT *
FROM generate_series('2020-09-01 00:00:00'::timestamp,'2020-09-04 12:00:00', '10 HOURS' );

SELECT *
FROM generate_series(CAST ('2020-09-01 00:00:00' AS timestamp),'2020-09-04 12:00:00', '10 HOURS' );

SELECT a.id,
	a.nombre,
	a.apellido,
	a.carrera_id,
	s.a
FROM platzi.alumnos AS a
	INNER JOIN generate_series(0,10) AS s(a)
	ON s.a = a.carrera_id
ORDER BY a.carrera_id;      

/* Hacer el Triangulo pero con un rango, como en la clase 21 */

SELECT lpad ('SQL',generate_series(1,10,2), '*')

SELECT lpad ('SQL',serie_genial, '*')
FROM generate_series(1,10,2) AS serie_genial;
