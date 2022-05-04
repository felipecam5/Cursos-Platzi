SELECT *
FROM (
	SELECT ROW_NUMBER() OVER() AS row_id,*
	FROM platzi.alumnos
)AS alumnos_with_row_num
WHERE row_id IN (1,5,10,12,15,20);

SELECT *
FROM platzi.alumnos
WHERE id IN (1,2,4,5);

SELECT *
FROM platzi.alumnos
WHERE id IN (
	SELECT id
	FROM platzi.alumnos
	WHERE tutor_id=30
);

/* Reto: Traer ahora a todos los que no estén en la lista, es decir, lo contrario a lo de arriba.*/

SELECT *
FROM platzi.alumnos
WHERE id IN(
	SELECT id
	FROM platzi.alumnos
	WHERE tutor_id!=30 AND tutor_id!=9
);

SELECT *
FROM platzi.alumnos
WHERE id NOT IN(2,3,4,5);

SELECT *
FROM platzi.alumnos
WHERE id NOT IN(
	SELECT id
	FROM platzi.alumnos
	WHERE tutor_id=30 OR tutor_id=9
);