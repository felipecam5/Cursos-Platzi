/* 1.ROW_NUMBER(): nos da el numero de la tupla que estamos utilizando en ese momento.  */
SELECT ROW_NUMBER() OVER(ORDER BY fecha_incorporacion) AS row_id, *
FROM platzi.alumnos;

/* 2. FIRST_VALUE(column): devuelve el primer valor de una serie de datos.  */
SELECT FIRST_VALUE(colegiatura) OVER(PARTITION by carrera_id) AS row_id, *
FROM platzi.alumnos;

/* 3.LAST_VALUE(column): Devuelve el ultimo valor de una serie de datos.  */
SELECT LAST_VALUE(colegiatura) OVER(PARTITION by carrera_id) AS row_id, *
FROM platzi.alumnos;

/* 4. NTH_VALUE(column, row_number): Recibe la columna y el numero de row que queremos devolver de una serie de datos  */
SELECT NTH_VALUE(colegiatura, 2) OVER(PARTITION by carrera_id) AS row_id, *
FROM platzi.alumnos;

/* 5. RANK(): nos dice el lugar que ocupa de acuerdo a el orden de cada tupla, deja gaps entre los valores.  */
SELECT *,
	RANK() OVER(PARTITION BY carrera_id ORDER BY colegiatura DESC) as colegiatura_rank
FROM platzi.alumnos
ORDER BY carrera_id, colegiatura_rank;

/* 6. DENSE_RANK(): Es un rango mas denso que trata de eliminar los gaps que nos deja RANK.  */
SELECT *,
	DENSE_RANK() OVER(PARTITION BY carrera_id ORDER BY colegiatura DESC) as colegiatura_rank
FROM platzi.alumnos
ORDER BY carrera_id, colegiatura_rank;

/* 7. PERCENT_RANK(): Categoriza de acuerdo a lugar que ocupa igual que los anteriores pero por porcentajes.  */
/* El Percent Rank utiliza la formula: (rank-1)/(total_rows -1)*/

SELECT *,
	PERCENT_RANK() OVER(PARTITION BY carrera_id ORDER BY colegiatura DESC) as colegiatura_rank
FROM platzi.alumnos
ORDER BY carrera_id, colegiatura_rank;