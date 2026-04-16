import sqlite3

if __name__ == "__main__":
    conn = sqlite3.connect("banco_de_dados\Aula\escola.db")
    cursor = conn.cursor()
    notas = [ 1, 2,5,3,4,9,8,7,4,6]
    nomes = ["leo", "teco", "jr"]

    # cursor.execute("""
    #     CREATE TABLE IF NOT EXISTS Alunos (
    #         id INTEGER PRIMARY KEY AUTOINCREMENT,
    #         nome TEXT,
    #         idade INTEGER,
    #         curso TEXT
    #                )
    # """)
    # conn.commit()

    # for i in range(0,3):
    #     cursor.execute("""
    #         INSERT INTO Alunos (nome, idade, curso) values (?,?,?)
    #     """, (nomes[i], 20, "back-end"))
    # conn.commit()

    # cursor.execute("""
    #     SELECT nome FROM Alunos 
    # """)
    # conn.commit()

    # cursor.execute("""
    #     SELECT nome FROM Alunos WHERE curso = "backend"
    # """)
    # conn.commit()

    # cursor.execute("""
    #     DELETE FROM Alunos WHERE id = 1
    # """)
    # conn.commit()

    # cursor.execute("""
    #     SELECT * FROM Alunos WHERE idade > 20
    # """)
    # conn.commit()

    # cursor.execute("""
    #     SELECT * FROM Alunos WHERE nome LIKE "A%"
    # """)

    # cursor.execute("""
    #     SELECT * FROM Alunos GROUP BY idade LIMIT 3
    # """)

    # cursor.execute("""
    #     SELECT * FROM Alunos ORDER BY nome DESC
    # """)

    # cursor.execute("""
    #     CREATE TABLE IF NOT EXISTS Notas (
    #         id INTEGER PRIMARY KEY AUTOINCREMENT,
    #         aluno_id INTEGER,
    #         diciplina TEXT,
    #         nota DECIMAL,
    #         FOREIGN KEY (aluno_id) REFERENCES alunos(id)        
    #         )
    # """)
    # conn.commit()

    # for i in range(0,3):
    #     cursor.execute("""
    #         INSERT INTO Notas (aluno_id, diciplina, nota) values (?,?,?)
    #     """, (i, "backend", notas[i]))
    # conn.commit()

    # cursor.execute("""
    #     SELECT Alunos.nome, Notas.diciplina, Notas.nota FROM Alunos INNER JOIN Notas ON Alunos.id = Notas.aluno_id 
    # """)
    # print(cursor.fetchall())

    # conn.close()