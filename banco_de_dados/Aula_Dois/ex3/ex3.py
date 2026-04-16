import sqlite3

if __name__ == "__main__":
    conn = sqlite3.connect("banco_de_dados\Aula_Dois\ex3\clientes.db")
    cursor = conn.cursor()
    cont = 0

    # cursor.execute("""
    #     CREATE TABLE IF NOT EXISTS clientes (
    #         id INTEGER PRIMARY KEY AUTOINCREMENT,
    #         nome TEXT,
    #         email TEXT,
    #         ativo INTEGER)
    # """)
    # conn.commit()

    # while cont <= 1:
    #     nome = input("Digite o nome do cliente: ")
    #     email = input("Digite o email desse cliente: ")
    #     ativo = int(input("O cliente esta ativo? (0 / 1)"))
    #     cursor.execute("""
    #         INSERT INTO clientes (nome, email, ativo) values (?,?,?)
    #     """, (nome, email, ativo))
    #     conn.commit()
    #     cont += 1

    # usuarios_inativos = cursor.execute("""
    #     SELECT nome FROM clientes WHERE ativo = 0
    # """)
    # conn.commit()
    # print(cursor.fetchall())

    # cursor.execute("""
    #     DELETE FROM clientes WHERE ativo = 0
    # """)
    # conn.commit()

    cursor.execute("""
        SELECT * FROM clientes
    """)
    print(cursor.fetchall())