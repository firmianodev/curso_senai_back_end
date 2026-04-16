import sqlite3

def main():
    conn = sqlite3.connect("banco_de_dados\Aula_Tres\contatos.db")
    cursor = conn.cursor()

    while True:
        opcao = int(input("1-cria tabela\n2-insere na tabela\n3-le a tabela\n4-atualiza a tabela\n5-deleta algo na tabela\n\nEscolha uma: "))
        match opcao:
            case 1:
                cria_tabela(cursor, conn)
            case 2:
                nome = input("Digite o nome a ser inserido na tabela: ")
                telefone = input("Digite o telefone do contato a ser inserido na tabela: ")
                email = input("Digite o email do contato a ser inserido na tabela: ")
                insere_na_tabela(cursor, conn, nome, telefone, email)
            case 3:
                ler_tabela(cursor)
            case 4:
                id = int(input("Digite o id do usuario: "))
                nome = input("Digite o nome a ser inserido na tabela: ")
                telefone = input("Digite o telefone do contato a ser inserido na tabela: ")
                email = input("Digite o email do contato a ser inserido na tabela: ")
                atualiza_tabela(cursor, conn, id, nome, telefone, email)
            case 5:
                id = int(input("Digite o id do usuario a ser deletado: "))
                deleta_na_tabela(cursor, conn, id)

        if deseja_continuar():
            break

def deseja_continuar():
    continuar = input("deseja continuar? (sim / nao)")
    return False if continuar == "sim" else True 


def cria_tabela(cursor, conn):

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Contatos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            telefone TEXT,
            email TEXT
            )
    """)
    conn.commit()

def insere_na_tabela(cursor, conn, nome, telefone, email):
    cursor.execute("""
        INSERT INTO Contatos(nome, telefone, email) VALUES (?,?,?)
    """, (nome, telefone, email))
    conn.commit()

def ler_tabela(cursor):

    cursor.execute("""
        SELECT * FROM Contatos
    """)
    print(cursor.fetchall())

def atualiza_tabela(cursor, conn,id, nome=None, telefone=None, email=None):
    if nome != None:
        cursor.execute(""" 
            UPDATE Contatos SET nome = ? WHERE id = ?
        """, (nome, id))
    if telefone != None:
        cursor.execute(""" 
            UPDATE Contatos SET telefone = ? WHERE id = ?
        """, (telefone, id))
    if email != None:
        cursor.execute(""" 
            UPDATE Contatos SET email = ? WHERE id = ?
        """, (email, id))
    conn.commit()

def deleta_na_tabela(cursor, conn, id):
    cursor.execute(f"""
        DELETE FROM Contatos WHERE id = {id}
    """)
    conn.commit()

if __name__ == "__main__":
    main()

