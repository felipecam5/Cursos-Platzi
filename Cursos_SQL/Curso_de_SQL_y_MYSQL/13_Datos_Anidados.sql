 INSERT INTO books (author_id, title) VALUES (6, 'El Laberinto de la Soledad');
 INSERT INTO books (author_id, title, `year` ) VALUES ((SELECT author_id FROM authors WHERE name ='Octavio Paz' LIMIT 1), 'El Laberinto de la Soledad', 1960);