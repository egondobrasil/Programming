# Importar as bibliotecas necessárias
# Colocar o index.html em uma pasta e abrir com o chrome
# Colocar o pessoas.csv na pasta do projeto
 
import csv  # ler o arquivo csv
# pip install csv
import time  # Controlar pausas no script
# pip install time
 
# pip install selenium
from selenium import webdriver  # controlar o navegador
from selenium.webdriver.common.by import By  # para localizar elementos na página
from selenium.webdriver.common.keys import Keys  # Interagir com os campos de texto
from selenium.webdriver.support.ui import WebDriverWait  # Para aguardar elementos
from selenium.webdriver.support import expected_conditions as ec  # Para condições de espera
 
# Caminho para o arquivo CSV
CSV_PATH = 'pessoas.csv'  # Caminho do arquivo csv com os dados
 
# Atenção: Pegue o endereço correto de onde está aplicação (index.html)
HTML_PATH = 'https://professorcelso.com.br/robo/'  # Caminho do HTML
 
# Iniciar o Navegador Chrome
options = webdriver.ChromeOptions()  # Cria opções para o chrome
options.add_experimental_option('detach', True)  # mantém o navegador aberto após o script
options.add_argument('--start-maximized')  # Inicia o navegador maximizado
 
# Abre o arquivo HTML local no navegador
# O selenium irá abrir a página index.html para a automação
driver = webdriver.Chrome(options=options)
driver.get(HTML_PATH)
 
# CORREÇÃO AQUI: WebDriverWait(driver, 10) → antes estava errado
wait = WebDriverWait(driver, 10)  # Aguarda até 10 segundos por elementos
 
# Função para preencher e submeter o formulário de forma genérica
# Não depende dos nomes dos campos, apenas da ordem dos campos no formulário e no csv
# Fazer os ajustes para garantir que os dados sejam preenchidos na ordem correta.
def preencher_formulario_generico(valores):
 
    # Aguardar formulário estar presente
    wait.until(ec.presence_of_element_located((By.TAG_NAME, 'form')))
 
    # Localiza o formulário (assume que há apenas um na página)
    form = driver.find_element(By.TAG_NAME, 'form')
 
    # Buscar todos os campos input, textarea e select dentro do formulário
    campos = form.find_elements(By.CSS_SELECTOR, 'input, textarea, select')
 
    # Ajusta a ordem dos valores para corresponder à ordem dos campos do formulário
    if len(valores) >= 5:
        # organizar os valores do CSV na ordem desejada
        valores_ordenados = [valores[0], valores[3], valores[1], valores[2], valores[4]]
    else:
        valores_ordenados = valores
 
    # Preencher cada campo do formulário com o valor correspondente
    for valor, campo in zip(valores_ordenados, campos):
        try:
            campo.clear()  # Limpa o campo antes de preencher
        except Exception:
            pass  # Nem todo campo suporta clear()
        campo.send_keys(valor)  # preenche o campo
 
    # Tenta encontrar e clicar no botão de submit
    try:
        botao = form.find_element(By.CSS_SELECTOR, 'button[type="submit"],input[type="submit"]')
        botao.click()
    except Exception:
        pass
 
    time.sleep(3)  # Aguarda 3 segundos antes de inserir o próximo registro
 
 
# Lê o CSV e alimenta o formulário de forma genérica
# LOOP MOVIDO PARA FORA DA FUNÇÃO → CORREÇÃO DO ERRO
with open(CSV_PATH, encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        if not row or len(row) < 1:
            continue
        preencher_formulario_generico(row)
 
# Exibe uma mensagem ao final do processo
print('Processo Concluído')
# FIM