-- Active: 1733485919709@@127.0.0.1@3306@teste_php

SELECT * FROM usuario;

TRUNCATE Table usuario;

INSERT INTO usuario(nome, senha, setor) VALUES ('Elias', '123', 'comum');
INSERT INTO usuario(nome, senha, setor) VALUES ('Adm', 'Adm', 'adm');

DROP Table usuario ;

ALTER TABLE USUARIO ADD COLUMN setor VARCHAR(10);

CREATE TABLE usuario (
    id_cliente int AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(30),
    lastname VARCHAR(30),
    sexo VARCHAR(30),
    fone VARCHAR(15),
    address VARCHAR(40),
    senha VARCHAR(30),
    email VARCHAR(50),
    setor VARCHAR(20) DEFAULT 'comum');