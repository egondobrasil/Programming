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
def listar_alunos(alunos):
    print("\n--- Lista de Alunos ---")
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    for i, a in enumerate(alunos, start=1):
        print(f"{i}. Nome: {a['nome']} | Idade: {a['idade']} | Curso: {a['curso']}")
    print(f"Total: {len(alunos)} aluno(s).")

# Função remover_aluno
def remover_aluno(alunos):
    print("\n--- Remover Aluno ---")
    if not alunos:
        print("Nenhum aluno para remover.")
        return
    listar_alunos(alunos)
    try:
        indice = int(input("Número do aluno a remover: "))
        if 1<= indice <= len(alunos):
            removido = alunos.pop(indice -1)
            salvar_alunos(alunos)
            print(f"Alunos '{removido['nome']}' removido com sucesso.")
        else:
            print("Número inválido.")
    except ValueError:
            print("Digite um número válido.")

# Função buscar_por_nome: Busca inclusive nome parcial.
def buscar_por_nome(alunos):
    print("\n--- Buscar aluno por Nome ---")
    termo = input_nao_vazio("Digite parte do nome: ").lower()
    resultados = [
        (i,a) for i,a in enumerate(alunos, start=1)
        if termo in a["nome"].lower()
    ]
    if not resultados:
        print("Nenhum aluno encontrado.")
    else:
        for i,a in resultados:
            print(f"{i}. Nome: {a['nome']} | Idade: {a['idade']} | Curso: {a['curso']}")
        print(f"Encontrado(s): {len(resultados)} aluno(s).")


 
# Função editar_aluno
def editar_aluno(alunos):
    print("\n--- Editar Aluno ---")
    if not alunos:
        print("Nenhum aluno encontrado.")
        return
    listar_alunos(alunos)
    try:
        indice = int(input("Número do aluno para editar: "))
        if 1 <= indice <= len(alunos):
            aluno = alunos[indice -1]
            print(f"Editando: {aluno['nome']} | Idade: {aluno['idade']} | Curso: {aluno['curso']}")
            
            novo_nome = input(f"Novo nome (Enter para manter {aluno['nome']}'): ").strip()
            if novo_nome:
                aluno['nome'] = novo_nome

            nova_idade = input(f"Nova idade (Enter para manter {aluno['idade']}'): ").strip()
            if nova_idade:
                aluno['idade'] = nova_idade

            novo_curso = input(f"Novo curso (Enter para manter {aluno['curso']}'): ").strip()
            if novo_curso:
                aluno['curso'] = novo_curso

            salvar_alunos(alunos)
            print("Dados Atualizados com sucesso.")

        else:
            print("Número inválido.")
    except ValueError:
            print("Digite um número válido.")
 
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
                listar_alunos(alunos)
            case "3":
                remover_aluno(alunos)
            case "4":
                buscar_por_nome(alunos)
            case "5":
                editar_aluno(alunos)
            case "6":
                break
            case _:
                print("Opção invalida")
 
if __name__ == "__main__":
    menu()