# python_excel.py
# pip install xlsxwriter
import xlsxwriter
 
# Criar uma tabela excel
workbook = xlsxwriter.Workbook('cadastro_alunos.xlsx')
 
# Adiciona dados na planilha
worksheet = workbook.add_worksheet("Cadastro de Alunos")
 
# Cabeçalho
headers = ["Nome","Curso","E-mail","Celular","Matriculado"]
 
for col, header in enumerate(headers):
    worksheet.write(0, col, header)
 
# Dados ficticios
 
pessoas = [
    ["Ana Beatriz", "Javascript", "ana.b@gmail.com", "(11) 9123-4567", True],
    ["Carlos Alberto", "PHP", "carlos.a@hotmail.com", "(11) 9123-7654", False],
    ["Mariana Silva", "Python", "mariana.s@hotmail.com", "(11) 9123-8765", True],
 
    ["Ricardo Mendes", "Java", "ricardo.m@gmail.com", "(11) 9134-1122", True],
    ["Fernanda Costa", "Python", "fernanda.c@hotmail.com", "(21) 9822-3344", False],
    ["João Pedro", "C#", "joao.p@gmail.com", "(31) 9988-2211", True],
    ["Patrícia Ramos", "Ruby", "patricia.r@gmail.com", "(41) 9776-5432", False],
    ["Lucas Andrade", "Go", "lucas.a@hotmail.com", "(51) 9844-2233", True],
    ["Aline Torres", "PHP", "aline.t@gmail.com", "(71) 9917-6622", False],
    ["Marcelo Farias", "Javascript", "marcelo.f@gmail.com", "(85) 9882-5566", True],
    ["Beatriz Moura", "Kotlin", "beatriz.m@yahoo.com", "(87) 9823-9988", False],
    ["Henrique Duarte", "Swift", "henrique.d@hotmail.com", "(47) 9122-7766", True],
    ["Tatiane Lopes", "Java", "tatiane.l@gmail.com", "(62) 9944-1122", False],
    ["Renato Carvalho", "Python", "renato.c@gmail.com", "(63) 9956-8877", True],
    ["Gabriela Souza", "C++", "gabriela.s@hotmail.com", "(91) 9812-3322", False],
    ["Thiago Santos", "C#", "thiago.s@gmail.com", "(92) 9845-2211", True],
    ["Juliana Rocha", "Ruby", "juliana.r@yahoo.com", "(31) 9876-1234", False],
    ["Eduardo Martins", "Javascript", "eduardo.m@hotmail.com", "(11) 9998-7755", True],
    ["Sabrina Keller", "Go", "sabrina.k@gmail.com", "(21) 9811-6665", False],
    ["Daniel Pires", "PHP", "daniel.p@gmail.com", "(48) 9992-3344", True]
]
 
# Escrever dados na planilha
row = 1
for pessoa in pessoas:
    for col, dado in enumerate(pessoa):
        worksheet.write(row, col, dado)
    row += 1

worksheet.autofit() # Ajusta a largura das colunas automaticamente
workbook.close() #Fecha o excel