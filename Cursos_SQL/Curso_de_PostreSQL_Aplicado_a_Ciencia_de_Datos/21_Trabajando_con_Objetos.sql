/* En Postgres SQL se puede trabajar con objetos JSON*/

/* 1.Creando una Tabla con campos tipo JSON*/

CREATE TABLE ordenes2(
    id serial NOT NULL PRIMARY KEY,
    info json NOT NULL
);

/* 2. Insertando valores tipo json*/

INSERT INTO ordenes2(info)
VALUES(
		'{"cliente": "David Sanchez","items":{"producto":"Biberón", "cantidad": "24"}}'
),

(
		'{"cliente": "Felipe Camacho","items":{"producto":"Carro de Juguete", "cantidad": "1"}}'
),

(
		'{"cliente": "Maria Rodriguez","items":{"producto":"Tren de Juguete", "cantidad": "2"}}'
);

/* 3.Accediendo a la información del Campo JSON mediante sentencias SQL*/

SELECT * FROM ordenes2; 

SELECT
    info -> 'cliente' AS cliente
    FROM ordenes2;                     /* Devuelven todo pero en formato JSON, con "", el cual no sirve mucho*/

 SELECT 
	info -> 'items' ->>'producto' AS cliente
	FROM ordenes2;   /* Ahora sí me devuelve un string, utilizando (->>)*/ 

SELECT 
	info ->> 'cliente' AS cliente
	FROM ordenes2
	WHERE info -> 'items' ->> 'producto' = 'Biberón';    


 


