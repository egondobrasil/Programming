#pip install mysql-connector-python
import mysql.connector
 
# Conectando banco de dados
def conectar():
    return mysql.connector.connect(
        host="localhost", # Endereço do servidor Mysql
        user="root", # usuário do banco
        password="", # senha do Mysql
        database="escola" # Nome do banco de dados
    )
 
def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    # sql para criação da tabela
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS alunos (
        id_aluno INT AUTO_INCREMENT PRIMARY KEY,
        nome_aluno VARCHAR(70),
        email VARCHAR(100),
        celular VARCHAR(20),
        rg VARCHAR(20)
    );
    """)
    print("Tabela criada com sucesso!")
    #fechar conexão
    conn.close()
 
# Função de adicionar aluno
def adicionar_aluno(nome,email,celular,rg):
    conn = conectar()
    cursor = conn.cursor()
    # Sql para incluir o registro
    cursor.execute("""
    INSERT INTO alunos (nome_aluno,email,celular,rg) values(%s, %s, %s, %s)
    """, (nome, email, celular, rg))
    conn.commit() # Confirma a transação
    print("Aluno adicionado com sucesso!")
    conn.close()
 
 # Função listar alunos
def listar_alunos():
    conn = conectar()
    cursor = conn.cursor()
    #sql para a consulta
    cursor.execute("SELECT * FROM alunos")
    alunos = cursor.fetchall() # Pegar todos os alunos
    print("Lista de Alunos")
    for aluno in alunos:
        print(f"ID: {aluno[0]} | Nome: {aluno[1]} | E-Mail: {aluno[2]} | Celular: {aluno[3]} | RG: {aluno[4]}")
    conn.close()
 
# Função para atualizar o aluno
def atualizar_aluno(id_aluno, nome, email, celular, rg):
    conn = conectar()
    cursor = conn.cursor()
    #sql para update no registro
    cursor.execute("""
        UPDATE alunos set nome_aluno = %s, email = %s, celular = %s, rg = %s
        WHERE id_aluno = %s                  
     """, (nome, email, celular, rg, id_aluno))
    conn.commit()
    print(f"Aluno com o ID {'id_aluno'} atualizado com sucesso!")
    conn.close()
 
#Função de excluir registro
def excluir_aluno(id_aluno):
    conn = conectar()
    cursor = conn.cursor()
    #SQL para exclusão
    cursor.execute("DELETE FROM alunos where id_aluno = %s", (id_aluno,))
    conn.commit()
    print(f"Aluno com o ID {id_aluno} excluído com sucesso!")
    conn.close()
 
def menu():
    while True:
        print("\n1. Criar Tabela")
        print("2. Adicionar Alunos")
        print("3. Listar Alunos")
        print("4. Alterar Aluno")
        print("5. Excluir Aluno")
        print("6. Sair do sistema")
        escolha = input("Escolha uma opção: ")
 
        if escolha == "1":
            criar_tabela()
        elif escolha == "2":
            nome = input("Nome: ")
            email = input("E-mail: ")
            celular = input("Celular: ")
            rg = input("RG: ")
            adicionar_aluno(nome,email,celular,rg)
        elif escolha == "3":
            listar_alunos()
        elif escolha == "4":
            listar_alunos()
            id_aluno = int(input("ID do aluno a ser atualizado: "))
            nome = input("Nome: ")
            email = input("E-mail: ")
            celular = input("Celular: ")
            rg = input("RG: ")
            atualizar_aluno(id_aluno,nome,email,celular,rg)
        elif escolha == "5":
            listar_alunos()
            id_aluno = int(input("ID do aluno a ser excluido: "))
            excluir_aluno(id_aluno)
        elif escolha == "6":
            print("Saindo do sistema.")
            break
        else:
            print("Opção Invalida")
 
 
#executar o menu
menu()