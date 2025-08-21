CREATE TABLE eventos (
    id SERIAL PRIMARY KEY,
    evento VARCHAR(255) NOT NULL,
    data_inicio DATE,
    data_fim DATE,
    responsavel VARCHAR(255),
    categoria VARCHAR(100), -- saber se é de IA, Marketing ou RH
    descricao TEXT
);