import sqlite3

def main():
    conn = sqlite3.connect("banco_de_dados\Aula_Tres\ex2\ tarefas.db")
    cursor = conn.cursor()

    while True:
        opcao = int(input("1-cria tabela\n2-insere na tabela\n3-le a tabela\n4-atualiza a tabela\n5-deleta algo na tabela\n\nEscolha uma: "))
        match opcao:
            case 1:
                cria_tabela(cursor, conn)
            case 2:
                titulo = input("Digite o titulo a ser inserido na tabela: ")
                descricao = input("Digite o descricao do contato a ser inserido na tabela: ")
                status = input("Digite o status do contato a ser inserido na tabela: ")
                insere_na_tabela(cursor, conn, titulo, descricao, status)
            case 3:
                status = input("Digite o status que vc quer buscar: ")
                ler_tabela(cursor, status)
            case 4:
                id = int(input("Digite o id do usuario: "))
                titulo = input("Digite o titulo a ser inserido na tabela: ")
                descricao = input("Digite o descricao do contato a ser inserido na tabela: ")
                status = input("Digite o status do contato a ser inserido na tabela: ")
                atualiza_tabela(cursor, conn, id, titulo, descricao, status)
            case 5:
                id = int(input("Digite o id do usuario a ser deletado: "))
                deleta_na_tabela(cursor, conn, id)

        if deseja_continuar():
            break

def deseja_continuar():
    continuar = input("\ndeseja continuar? (sim / nao)")
    return False if continuar == "sim" else True 


def cria_tabela(cursor, conn):

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT,
            descricao TEXT,
            status TEXT DEFAULT "Pendente"
            )
    """)
    conn.commit()

def insere_na_tabela(cursor, conn, titulo, descricao, status):
    if titulo.strip() != '' and type(titulo) != None:
        cursor.execute("""
            INSERT INTO tarefas(titulo, descricao, status) VALUES (?,?,?)
        """, (titulo, descricao, status))
        conn.commit()

def ler_tabela(cursor, status):

    if status != '':
        cursor.execute(f"""
        SELECT * FROM tarefas WHERE status = "{status}"
    """)

    print(cursor.fetchall())

def atualiza_tabela(cursor, conn,id, titulo=None, descricao=None, status=None):
    if titulo != None:
        cursor.execute(""" 
            UPDATE tarefas SET titulo = ? WHERE id = ?
        """, (titulo, id))
    if descricao != None:
        cursor.execute(""" 
            UPDATE tarefas SET descricao = ? WHERE id = ?
        """, (descricao, id))
    if status != None:
        cursor.execute(""" 
            UPDATE tarefas SET status = ? WHERE id = ?
        """, (status, id))
    conn.commit()

def deleta_na_tabela(cursor, conn, id):
    cursor.execute(f"""
        DELETE FROM tarefas WHERE id = {id}
    """)
    conn.commit()

if __name__ == "__main__":
    main()

