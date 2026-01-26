# cadastro.py
# Cadastro de alunos gravando as informações em um arquivo JSON
# Listas, Dicionarios, Persistencia de dados
import json
from pathlib import Path
 
ARQUIVO = Path("alunos.json")
 
# Função carregar_alunos
def carregar_alunos():
    if ARQUIVO.exists():
        try:
            with ARQUIVO.open("r", encoding="utf-8") as f:
                dados = json.load(f)
                if isinstance(dados, list):
                    return dados
                else:
                    print("Formato JSON Invalido")
        except json.JSONDecodeError:
            print("Erro ao codificar o JSON")
    return []
   
 
# Função salvar_alunos
def salvar_alunos(alunos):
    with ARQUIVO.open("w", encoding="utf-8") as f:
        json.dump(alunos, f, ensure_ascii=False, indent=2)
 
#--- Validações
# Função input_nao_vazio
def input_nao_vazio(msg):
    while True:
        valor = input(msg).strip()
        if valor:
            return valor
        print("Campo obrigatório, tente novamente.")
 
# Função input_idade
def input_idade(msg="idade: "):
    while True:
        valor = input(msg).strip()
        if valor.isdigit() and 8 < int(valor) < 80:
            return valor
        print("Idade inválida. Tente novamente 9 a 79 anos.")
 
#---- Operações
# Função adicionar_aluno
def adicionar_aluno(alunos):
    print("\n--- Adicionar aluno ---")
    nome = input_nao_vazio("Nome do Aluno: ")
    idade= input_idade("Idade do Aluno: ")
    curso= input("Curso: ")
    aluno = {"nome": nome, "idade": idade,"curso": curso}
    alunos.append(aluno)
    salvar_alunos(alunos)
    print("Aluno cadastrado com Sucesso.")
# Função listar_alunos
 
# Função remover_aluno
 
# Função buscar_aluno_nome
 
# Função editar_aluno
 
#------------------ menu ------------------------
def menu():
    alunos = carregar_alunos()
    while True:
        print("\n=== Sistema de Cadastro de Alunos (JSON) ===")
        print("1 - Adicionar aluno")
        print("2 - listar alunos")
        print("3 - Remover aluno")
        print("4 - Buscar aluno")
        print("5 - Editar aluno")
        print("6 - Sair")
        opcao = input("Escolha a opção desejada: ").strip()
 
        match opcao:
            case "1":
                adicionar_aluno(alunos)
            case "2":
                print("Opcao 2")
            case "3":
                print("Opcao 3")
            case "4":
                print("Opcao 4")
            case "5":
                print("Opcao 5")
            case "6":
                break
            case _:
                print("Opção invalida")
 
if __name__ == "__main__":
    menu()