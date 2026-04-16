import sqlite3

if __name__ == "__main__":
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()

    # cursor.execute("""
    #     SELECT * FROM Cliente
    # """)
    # conn.commit()

    # cursor.execute("""
    #     SELECT Nome FROM Produto WHERE Preco > 10.00 ORDER BY Nome
    # """)
    # conn.commit()

    # cursor.execute("""
    #     SELECT Cliente.Nome, Pedido.Data FROM Cliente INNER JOIN Pedido ON Cliente.ID = Pedido.ClienteID 
    # """)
    # conn.commit()

    # cursor.execute("""
    #     SELECT Produto.Nome, SUM(Pedido.Quantidade) 
    #     FROM Pedido 
    #     INNER JOIN PRODUTO ON Pedido.ProdutoID = Produto.ID
    #     GROUP BY Produto.Nome  
    # """)
    # conn.commit()

    # cursor.execute("""
    #     SELECT Produto.Nome, Pedido.Quantidade
    #     FROM Pedido 
    #     INNER JOIN PRODUTO ON Pedido.ProdutoID = Produto.ID WHERE Pedido.Quantidade = 0
    #     GROUP BY Produto.Nome 
    # """)
    # conn.commit()
    # conn.close()





 




