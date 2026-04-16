CREATE TABLE Cliente (
ID INTEGER PRIMARY KEY AUTOINCREMENT,
Nome TEXT NOT NULL,
Email TEXT
);
CREATE TABLE Produto (
ID INTEGER PRIMARY KEY AUTOINCREMENT,
Nome TEXT NOT NULL,
Preco DECIMAL(10,2)
);
CREATE TABLE Pedido (
ID INTEGER PRIMARY KEY AUTOINCREMENT,
ClienteID INTEGER,
ProdutoID INTEGER,
Quantidade INTEGER,
Data DATE,
FOREIGN KEY (ClienteID) REFERENCES Cliente(ID),
FOREIGN KEY (ProdutoID) REFERENCES Produto(ID)
);

CREATE TABLE Fornecedor (
    ID INTEGER PRIMARY KEY,
    Nome TEXT NOT NULL,
    cnpj TEXT(14)
)

DROP TABLE Fornecedor

ALTER TABLE INTO Cliente ADD Telefone TEXT(15)

INSERT INTO Cliente (ID, NOME, Email) VALUES (1, "Joana", "joana@email.com")

INSERT INTO Produto (ID, NOME, PRECO) VALUES (10, "Café", 8,50)

INSERT INTO Pedido (ID, ClienteID, ProdutoID, Quantidade, Data) VALUES (0, 1, 10, 3, "25/03/26")

UPDATE Cliente SET Email = "joana.silva@email.com" WHERE ID = 1

DELETE FROM Pedido WHERE ID = 0

SELECT * FROM Cliente

SELECT Nome FROM Produto WHERE Preco > 10.00 ORDER BY Nome

SELECT Clinte.Nome, Pedido.Data FROM Cliente INNER JOIN Pedido ON Cliente.ID = Pedido.ClienteID  

SELECT Produto.Nome, SUM(Pedido.Quantidade) 
FROM Pedido 
INNER JOIN PRODUTO ON Pedido.ProdutoID = Produto.ID
GROUP BY Produto.Nome  

SELECT Produto.Nome, Pedido.Quantidade
FROM Pedido 
INNER JOIN PRODUTO ON Pedido.ProdutoID = Produto.ID WHERE Produto.Quantidade = 0
GROUP BY Produto.Nome 
