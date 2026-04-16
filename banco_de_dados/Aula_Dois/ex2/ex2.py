import sqlite3

if __name__ == "__main__":
    conn = sqlite3.connect("banco_de_dados\Aula_Dois\loja.db")
    cursor = conn.cursor()

    # cursor.execute("""
    #     CREATE TABLE IF NOT EXISTS produtos (
    #         id INTEGER PRIMARY KEY AUTOINCREMENT,
    #         nome TEXT,
    #         preco DECIMAL)
    # """)
    # conn.commit()

    # nome = input("Digite o nome de um produto: ")
    # preco = input("Digite o preco desse produto: ")
    # cursor.execute("""
    #      INSERT INTO produtos (nome, preco) values (?,?)
    # """, (nome, preco))
    # conn.commit()

    cursor.execute(f"""
        UPDATE produtos SET preco = 650 WHERE id = 1
    """)
    conn.commit()

    # cursor.execute("""
    #     SELECT * FROM produtos
    # """)
    # produtos = cursor.fetchall()
    # for produto in produtos:
    #   print(f"id: {produto[0]} | nome : {produto[1]} | preco: {produto[2]} ")

    