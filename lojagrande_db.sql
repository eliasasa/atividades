CREATE DATABASE IF NOT EXISTS loja_grande;
USE loja_grande;
 
CREATE TABLE IF NOT EXISTS sexos (
    id_sexo INT PRIMARY KEY AUTO_INCREMENT,
    sexo VARCHAR(46) -- vai que pneumoultramicroscopicossilicovulcanoconiótico vira um sexo, né?
);
 
CREATE TABLE IF NOT EXISTS situacao_icms (
    id_st_icms INT PRIMARY KEY AUTO_INCREMENT,
    st_icms INT,
    descricao_icms VARCHAR(255)
);
 
CREATE TABLE IF NOT EXISTS transportadoras (
    id_transp INT PRIMARY KEY AUTO_INCREMENT,
    nome_transp VARCHAR(255)
);
 
CREATE TABLE IF NOT EXISTS situacao_cadastro (
    id_st_cadastro INT PRIMARY KEY AUTO_INCREMENT,
    st_cadastro VARCHAR(255) -- O que eu não sei o que é vira VARCHAR(255), que o pessoal do código lide com isso depois kkkkk
);
 
CREATE TABLE IF NOT EXISTS produto (
    id_produto INT PRIMARY KEY AUTO_INCREMENT,
    descricao VARCHAR(255),
    variante VARCHAR(100),
    p_s VARCHAR(255), -- sei nem o que é kkkk 
    codigo INT,
    qtde_base INT,
    qtde INT,
    um VARCHAR(50), -- também não sei o que seria
    custo_unitario FLOAT,
    custo_total FLOAT,
    qtde_fixa_variavel FLOAT,
    ordem VARCHAR(100),
    c_i VARCHAR(100),
    origem VARCHAR(255),
    status_produto VARCHAR(255)
);
 
CREATE TABLE IF NOT EXISTS precos (
    id_tb_preco INT PRIMARY KEY AUTO_INCREMENT,
    id_produto INT,
    preco FLOAT,
    id_vendedor INT,
    FOREIGN KEY (id_produto) REFERENCES produto (id_produto)
);
 
CREATE TABLE IF NOT EXISTS cliente (
    id_cliente INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL,
    email VARCHAR(100),
    email_danfe VARCHAR(100),
    email_cobranca VARCHAR(100),
    email_loja_virtual VARCHAR(100),
    telefone_comercial VARCHAR(20),
    ramal VARCHAR(9),
    telefone_residencial VARCHAR(20),
    telefone_celular VARCHAR(20),
    fax VARCHAR(50),
    cpf VARCHAR(11) NOT NULL,
    rg VARCHAR(7) NOT NULL,
    id_recomendador INT, -- tornar isso uma FOREIGN KEY da tabela cliente
    endereco VARCHAR(255), -- talvez eu deva criar uma tabela endereço, pouparia alguns KB por poder ter uma tabela para o estado, a cidade, etc.
    situacao_icms INT, -- criar tabela situacao_icms
    inscricao_estadual VARCHAR(9),
    inscricao_suframa VARCHAR(50),
    sexo INT, -- criar tabela sexos
    data_nascimento DATE,
    transportadora_1 INT, -- Criar tabela transportadoras
    transportadora_2 INT,
    tabela_preco INT, -- criar tabela dos preços?
    mod_frete_padrao VARCHAR(50),
    situacao_cadastro INT, -- Criar tabela das situações do cadastro
    linha_peef VARCHAR(50),
    aliquota FLOAT,
    FOREIGN KEY (id_recomendador) REFERENCES cliente (id_cliente),
    FOREIGN KEY (sexo) REFERENCES sexos (id_sexo),
    FOREIGN KEY (situacao_icms) REFERENCES situacao_icms (id_st_icms),
    FOREIGN KEY (transportadora_1) REFERENCES transportadoras (id_transp),
    FOREIGN KEY (transportadora_2) REFERENCES transportadoras (id_transp),
    FOREIGN KEY (situacao_cadastro) REFERENCES situacao_cadastro (id_st_cadastro),
    FOREIGN KEY (tabela_preco) REFERENCES precos (id_tb_preco)
);
 
ALTER TABLE precos
ADD CONSTRAINT fk_vendedor
FOREIGN KEY (id_vendedor)
REFERENCES cliente (id_cliente);
 
CREATE TABLE IF NOT EXISTS ordem_servico (
    id_ordem_servico INT PRIMARY KEY AUTO_INCREMENT,
    documento TEXT,
    emissao DATE,
    id_cliente INT,
    previsao DATE,
    descricao TEXT,
    execucao VARCHAR(255),
    servico VARCHAR(255),
    variante VARCHAR(100),
    quantidade FLOAT,
    valor FLOAT,
    FOREIGN KEY (id_cliente) REFERENCES cliente (id_cliente)
);
 
CREATE TABLE IF NOT EXISTS nf_venda_peca (
    id_nf_venda_peca INT PRIMARY KEY AUTO_INCREMENT,
    documento TEXT,
    sequencia INT,
    emissao DATE,
    vencimento DATE,
    previsao_faturamento FLOAT,
    aprovacao_cliente DATE,
    hr_aprovacao VARCHAR(50),
    embarque INT,
    prazo_entrega DATE,
    n_pedido_compra INT,
    id_vendedor INT,
    id_cliente INT,
    end_entrega VARCHAR(255),
    tb_preco INT,
    transportadora_1 INT,
    transportadora_2 INT,
    tipo_frete VARCHAR(50),
    valor_frete FLOAT,
    porcentagem FLOAT,
    valor_desconto_rateado FLOAT,
    contato VARCHAR(20),
    FOREIGN KEY (id_cliente) REFERENCES cliente (id_cliente),
    FOREIGN KEY (transportadora_1) REFERENCES transportadoras (id_transp),
    FOREIGN KEY (transportadora_2) REFERENCES transportadoras (id_transp),
    FOREIGN KEY (id_vendedor) REFERENCES cliente (id_cliente),
    FOREIGN KEY (tb_preco) REFERENCES precos (id_tb_preco)
);
 
CREATE TABLE IF NOT EXISTS login (
    user_name VARCHAR(50),
    password VARCHAR(50),
    id_cliente INT,
    FOREIGN KEY (id_cliente) REFERENCES cliente (id_cliente)
);

-- Tabela sexos
INSERT INTO sexos (sexo) VALUES 
('Masculino'), 
('Feminino'), 
('Não se aplica');

-- Tabela situacao_icms
INSERT INTO situacao_icms (st_icms, descricao_icms) VALUES 
(0, 'Isento de ICMS'), 
(1, 'Tributado integralmente'), 
(2, 'Substituição Tributária'), 
(3, 'Diferido');

-- Tabela transportadoras
INSERT INTO transportadoras (nome_transp) VALUES 
('Correios'), 
('FedEx'), 
('DHL Express'), 
('Jadlog'), 
('Total Express');

-- Tabela situacao_cadastro
INSERT INTO situacao_cadastro (st_cadastro) VALUES 
('Ativo'), 
('Inativo'), 
('Bloqueado'), 
('Pendente de Verificação');

-- Tabela produto
INSERT INTO produto (descricao, variante, p_s, codigo, qtde_base, qtde, um, custo_unitario, custo_total, qtde_fixa_variavel, ordem, c_i, origem, status_produto) 
VALUES 
('Smartphone Samsung Galaxy S21', '128GB Preto', 'P001', 10101, 500, 480, 'Unidade', 3500.00, 1680000.00, 1.0, 'OR-001', 'CI-SM-GS21', 'Coreia do Sul', 'Disponível'), 
('Notebook Dell XPS 13', '16GB RAM, 512GB SSD', 'P002', 20202, 300, 290, 'Unidade', 6500.00, 1885000.00, 1.0, 'OR-002', 'CI-NB-XPS13', 'Estados Unidos', 'Disponível'), 
('Monitor LG Ultrawide 34"', '2560x1080', 'P003', 30303, 150, 140, 'Unidade', 2100.00, 315000.00, 1.0, 'OR-003', 'CI-MN-UL34', 'China', 'Disponível');

-- Tabela precos
INSERT INTO precos (id_produto, preco, id_vendedor) 
VALUES 
(1, 3899.00, 1), 
(2, 6999.00, 2), 
(3, 2299.00, 1);

-- Tabela cliente
INSERT INTO cliente (nome, email, email_danfe, email_cobranca, email_loja_virtual, telefone_comercial, ramal, telefone_residencial, telefone_celular, fax, cpf, rg, id_recomendador, endereco, situacao_icms, inscricao_estadual, inscricao_suframa, sexo, data_nascimento, transportadora_1, transportadora_2, mod_frete_padrao, situacao_cadastro, linha_peef, aliquota) 
VALUES 
('Carlos Eduardo da Silva', 'carlos.silva@email.com', 'danfe.carlos@email.com', 'cobranca.carlos@email.com', 'carlos.loja@email.com', '1133445566', '123', '1133445567', '999888777', '1133445568', '12345678901', '1234567', NULL, 'Rua dos Andradas, 100', 1, '123456789', 'SUFRAMA100', 1, '1985-04-12', 1, 2, 'CIF', 1, 'Linha 1', 12.00), 
('Fernanda Martins Souza', 'fernanda.souza@email.com', 'danfe.fernanda@email.com', 'cobranca.fernanda@email.com', 'fernanda.loja@email.com', '1122334455', '124', '1122334456', '988776655', '1122334457', '98765432101', '2345678', 1, 'Av. Paulista, 200', 2, '987654321', 'SUFRAMA200', 2, '1990-08-22', 3, 4, 'FOB', 2, 'Linha 2', 18.00);

-- Tabela ordem_servico
INSERT INTO ordem_servico (documento, emissao, id_cliente, previsao, descricao, execucao, servico, variante, quantidade, valor) 
VALUES 
('OS-001', '2023-09-01', 1, '2023-09-05', 'Troca de tela de smartphone', 'Completo', 'Reparo de tela', 'Samsung Galaxy S21', 1.0, 500.00), 
('OS-002', '2023-09-02', 2, '2023-09-06', 'Instalação de SSD em notebook', 'Em andamento', 'Instalação de hardware', 'Dell XPS 13', 1.0, 300.00);

-- Tabela nf_venda_peca
INSERT INTO nf_venda_peca (documento, sequencia, emissao, vencimento, previsao_faturamento, aprovacao_cliente, hr_aprovacao, embarque, prazo_entrega, n_pedido_compra, id_vendedor, id_cliente, end_entrega, tb_preco, transportadora_1, transportadora_2, tipo_frete, valor_frete, porcentagem, valor_desconto_rateado, contato) 
VALUES 
('NF-001', 1, '2023-08-01', '2023-08-31', 5000.00, '2023-08-02', '14:00', 1, '2023-09-01', 1001, 1, 1, 'Rua dos Andradas, 100', 1, 1, 2, 'FOB', 100.00, 5.0, 200.00, 'Carlos'), 
('NF-002', 1, '2023-08-05', '2023-09-05', 3000.00, '2023-08-06', '10:00', 2, '2023-09-06', 1002, 2, 2, 'Av. Paulista, 200', 2, 3, 4, 'CIF', 150.00, 10.0, 300.00, 'Fernanda');

-- Tabela login
INSERT INTO login (user_name, password, id_cliente) 
VALUES 
('carlos.silva', 'password123', 1), 
('fernanda.souza', 'password456', 2);



-- CORREÇÕES 

--FGKEY codependentes >>> (!!!rodar primeiro!!!)

/*clientes: FOREIGN KEY (tabela_preco) REFERENCES precos (id_tb_preco)

"ALTER TABLE precos
ADD CONSTRAINT fk_vendedor
FOREIGN KEY (id_vendedor)
REFERENCES cliente (id_cliente);"*/

ALTER TABLE cliente DROP FOREIGN KEY cliente_ibfk_7;

ALTER TABLE cliente DROP COLUMN tabela_preco;

ALTER TABLE precos DROP FOREIGN KEY fk_vendedor;

-- Adicionar coluna CNPJ (null) caso o cliente não tenha um CPF e vice-versa
ALTER TABLE cliente ADD COLUMN cnpj VARCHAR(14) DEFAULT NULL;

-- Sexo not null >
ALTER TABLE sexos MODIFY COLUMN sexo VARCHAR(46) NOT NULL;

-- Em ordem_servico, servico, documento, emissao e quantidade não é 'NOT NULL' // Valor não 'DEFAULT = 0',
ALTER TABLE ordem_servico
MODIFY COLUMN servico VARCHAR(255) NOT NULL,
MODIFY COLUMN documento TEXT NOT NULL,
MODIFY COLUMN emissao DATE NOT NULL,
MODIFY COLUMN quantidade FLOAT NOT NULL DEFAULT 0;

-- Em produto status, custo_total e serviço não estão definidos 'NOT NULL'
ALTER TABLE produto
MODIFY COLUMN status_produto VARCHAR(255) NOT NULL,
MODIFY COLUMN custo_total FLOAT NOT NULL DEFAULT 0.00,
MODIFY COLUMN descricao VARCHAR(255) NOT NULL;


-- Em nota fiscal , documento, sequencia, emissao, aprovação do cliente, hora da aprovação, não é 'NOT NULL' // Valor não é default = 0
ALTER TABLE nf_venda_peca
MODIFY COLUMN documento TEXT NOT NULL,
MODIFY COLUMN sequencia INT NOT NULL,
MODIFY COLUMN emissao DATE NOT NULL,
MODIFY COLUMN aprovacao_cliente DATE NOT NULL,
MODIFY COLUMN hr_aprovacao VARCHAR(50) NOT NULL,
MODIFY COLUMN valor_frete FLOAT NOT NULL DEFAULT 0.00,
MODIFY COLUMN valor_desconto_rateado FLOAT NOT NULL DEFAULT 0.00;

--  Regime de tributação
CREATE TABLE IF NOT EXISTS regime_tributacao (
    id_regime INT PRIMARY KEY AUTO_INCREMENT,
    descricao VARCHAR(255) NOT NULL
);

ALTER TABLE cliente
ADD COLUMN regime_tributacao INT,
ADD FOREIGN KEY (regime_tributacao) REFERENCES regime_tributacao(id_regime);

-- Renomear tabelas
RENAME TABLE sexos TO sexo;
RENAME TABLE transportadoras TO transportadora;
RENAME TABLE precos TO preco;

-- Correção de endereço (por estar em varchar, não é muito pratico)

CREATE TABLE IF NOT EXISTS estado (
    id_estado INT PRIMARY KEY AUTO_INCREMENT,
    nome_estado VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS cidade (
    id_cidade INT PRIMARY KEY AUTO_INCREMENT,
    nome_cidade VARCHAR(100) NOT NULL,
    id_estado INT,
    FOREIGN KEY (id_estado) REFERENCES estado(id_estado)
);

CREATE TABLE IF NOT EXISTS enderecos (
    id_endereco INT PRIMARY KEY AUTO_INCREMENT,
    rua VARCHAR(255) NOT NULL,
    numero VARCHAR(10),
    complemento VARCHAR(100),
    id_cidade INT,
    FOREIGN KEY (id_cidade) REFERENCES cidade(id_cidade)
);

-- Add coluna id em clientes
ALTER TABLE cliente ADD COLUMN id_endereco INT;
-- Referenciando 
ALTER TABLE cliente ADD FOREIGN KEY (id_endereco) REFERENCES enderecos(id_endereco);

-- Remover coluna antiga
ALTER TABLE cliente DROP COLUMN endereco;

-- Em um contexto profissional, acredito que remover a coluna endereco sem conservar suas informações anteriores não seja a melhor ideia
-- Eu faria os novos inserts mas cansei por hoje 