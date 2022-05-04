SELECT DISTINCT colegiatura
FROM platzi.alumnos
ORDER BY colegiatura DESC
OFFSET 1
LIMIT 1;

SELECT DISTINCT colegiatura
FROM platzi.alumnos AS a1
WHERE 1 = (
	SELECT COUNT (DISTINCT colegiatura)
	FROM platzi.alumnos AS a2
	WHERE a1.colegiatura <= a2.colegiatura
);

SELECT DISTINCT colegiatura, tutor_id
FROM platzi.alumnos
WHERE tutor_id = 20
ORDER BY colegiatura DESC
OFFSET 1
LIMIT 1;

SELECT *
FROM platzi.alumnos AS datos_alumnos
INNER JOIN (
	SELECT DISTINCT colegiatura
	FROM platzi.alumnos  
	WHERE tutor_id=20
	ORDER BY colegiatura DESC
	LIMIT 1 OFFSET 1
) AS segunda_mayor
ON datos_alumnos.colegiatura = segunda_mayor.colegiatura; /* Me trae tambien los estudiantes que pagan esa colegiatura, mediante un subquery*/

SELECT *
FROM platzi.alumnos AS datos_alumnos
WHERE colegiatura=(
	SELECT DISTINCT colegiatura
	from platzi.alumnos
	WHERE tutor_id=20
	ORDER BY colegiatura DESC 
	LIMIT 1 OFFSET 1
); /* Me trae tambien los estudiantes que pagan esa colegiatura, mediante un subquery pero mas sencillo*/

/* Reto: traer solo la segunda mitad de la tabla */

SELECT *
FROM platzi.alumnos
WHERE id >=(
	SELECT COUNT(*)/2 
	FROM platzi.alumnos
);

SELECT ROW_NUMBER() OVER() AS row_id, *
FROM platzi.alumnos
OFFSET (
	SELECT COUNT(id)/2
	FROM platzi.alumnos

);