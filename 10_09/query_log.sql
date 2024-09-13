CREATE DATABASE logdesk;
USE logdesk;

CREATE TABLE cadastro (
    id_cli int PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100),
    senha VARCHAR(30),
    texto tinytext
);

INSERT INTO cadastro VALUES (NULL, 'Elias','elias123', 'poopdood');

SELECT * FROM cadastro;

DROP Table cadastro;

TRUNCATE Table cadastro;