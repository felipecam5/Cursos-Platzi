SELECT *
FROM platzi.alumnos
FETCH FIRST 1 ROWS ONLY; /* o LIMIT 1;*/

SELECT *
FROM (
	SELECT ROW_NUMBER() OVER() AS row_id,*
	FROM platzi.alumnos
) AS alumnos_with_row_num
WHERE row_id =1
;

/* El reto de esta clase es: Retornar los primeros cinco(5) registros de la tabla de todas las formas posibles.*/

SELECT * 
FROM platzi.alumnos
LIMIT 5;

SELECT *
FROM platzi.alumnos
WHERE id <=5;

SELECT *
FROM platzi.alumnos
WHERE id >= 1 and id <=5;

SELECT *
FROM platzi.alumnos
WHERE id BETWEEN 1 AND 5;

SELECT *
FROM platzi.alumnos
FETCH FIRST 5 ROWS ONLY;

SELECT*
FROM (
    SELECT ROW_NUMBER() OVER() AS row_id,*
    FROM platzi.alumnos
) AS alumnos_with_row_number
WHERE row_id <= 5
;