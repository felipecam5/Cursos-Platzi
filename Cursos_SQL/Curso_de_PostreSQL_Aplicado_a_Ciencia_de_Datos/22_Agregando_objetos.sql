/* SE PUEDEN UTILIZAR LAS FUNCIONES DE AGREACIÓN CON JSON*/

/*La idea es convertir el JSON en STRING y luego el STRINg en INTEGER*/


SELECT 
	MIN (
		CAST(
			info -> 'items' ->> 'cantidad' AS INTEGER
		)
	)
FROM ordenes2;    

SELECT 
	AVG (
		CAST(
			info -> 'items' ->> 'cantidad' AS INTEGER
		)
	)
FROM ordenes2;

SELECT 
	SUM (
		CAST(
			info -> 'items' ->> 'cantidad' AS INTEGER
		)
	)
FROM ordenes2;