import sqlite3

if __name__ == "__main__":
    conn = sqlite3.connect("banco_de_dados\Aula_Dois\ biblioteca.db")
    cursor = conn.cursor()

    # cursor.execute("""
    #     CREATE TABLE IF NOT EXISTS Livros (
    #         id INTEGER PRIMARY KEY AUTOINCREMENT,
    #         titulo TEXT,
    #         autor TEXT,
    #         ano_publicado INTEGER           
    #     )
    # """)
    # conn.commit()

    # cursor.execute("""
    #     INSERT INTO Livros (titulo, autor, ano_publicado) values (?,?,?)
    # """, ("it", "king", 1990))
    # conn.commit()

    # cursor.execute("""
    #     INSERT INTO Livros (titulo, autor, ano_publicado) values (?,?,?)
    # """, ("a profecia", "desconhecido", 1980))
    # conn.commit()

    # cursor.execute("""
    #     INSERT INTO Livros (titulo, autor, ano_publicado) values (?,?,?)
    # """, ("psicose", "bloch", 1990))
    # conn.commit()

    # cursor.execute("""
    #     SELECT * FROM Livros 
    # """)
    # livros = cursor.fetchall()


    titulo = input("Digite o titulo de um livo: ")
    autor = input("Digite o nome do autor do livro: ")
    ano_lancamento = int(input("Digite o ano de lancamento do livro: "))
    cursor.execute("""
         INSERT INTO Livros (titulo, autor, ano_publicado) values (?,?,?)
    """, (titulo, autor, ano_lancamento))
    conn.commit()
