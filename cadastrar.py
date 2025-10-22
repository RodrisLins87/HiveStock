############################################## IMPORTAÇÕES DAS BIBLIOTECAS ##############################################

import os
import time
import json
import re
import random
import sys

import smtplib
from email.message import EmailMessage
import mimetypes

############################################## FUNÇÕES DECLARADAS   ##############################################
 
escolhas_login= ["1","2","3","4"] 
caracteres_especiais = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', ',', '.', '?', ':', '"', '{', '}', '|', '<', '>']
possibilidades_cadastro=["1","2"]


def email_valido(email):
    """VERIFICA SE O EMAIL É VÁLIDO"""
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(padrao, email))

def code_verificação():
      """FUNÇÃO QUE GERA CÓDIGO ALEATÓRIO DE VERIFICAÇÃO"""
      return str(random.randint(100000, 999999))


aguardar = time.sleep 

def limpar_tela():
    """Limpa o terminal a cada instante que foi determinado"""
    if os.name == 'nt': 
        os.system('cls')
    else:  
        os.system('clear')

def menu():
    """O MENU INICIAL DA HIVESTOCK"""
    print("\n Bem-Vindo a HiveStock \n")

    print("[1] Criar Cadastro")
    print("[2] LOGIN")
    print("[3] Recuperar Acesso")
    print("[4] Sair \n")


   


def menu_usuario():
    """O MENU DO TIPO DE USUÁRIO"""
    print("Selecione o seu tipo de usuário:")
    print("\n[1] ADMINISTRADOR \n[2] FUNCIONÁRIO")

def cadastro_usuario():

    while 1>0:

            nome_cadastro=input("Qual o seu nome completo? ").strip()
            if not nome_cadastro:
                print("O campo precisa ser preenchido! ")
                aguardar(3)
                limpar_tela()
                continue 
                
            elif all(char.isalpha() and char.isspace() for char in nome_cadastro): #GARANTE QUE O NOME SÓ TENHA LETRAS E ESPAÇÕES
                print("Nome cadastrado!")
                break 
            else:
                print("Nome inválido!")
                aguardar(3)
                limpar_tela()
            
            
    aguardar(3)
    limpar_tela()

    ############################################## CADASTRO (MATRÍCULA DO USUÁRIO) ##############################################

    while 1>0:
            matricula_cadastro=input("Qual a sua matrícula? ").strip()

            if not matricula_cadastro:
                print("O campo precisa ser preenchido!")
                aguardar(3)
                limpar_tela()
                continue

            elif not len(matricula_cadastro)==11:
                print("Matrícula não confere")
                aguardar(3)
                limpar_tela()
                continue

            elif not matricula_cadastro.isdigit():
                print("Matrícula não confere!\n ")
                print("\n Digite apenas números. Sem espaços, letras ou caracteres especiais!")
                aguardar(3)
                limpar_tela()
                continue

            else:
                print(f"A matrícula {matricula_cadastro} foi cadastrada!")
                break 

    aguardar(3)
    limpar_tela()
        
    ############################################## CADASTRO (EMAIL DO USUÁRIO) ##############################################  

    while 1>0:
            email_cadastro=input("Qual o seu email? ")
            if not email_cadastro:
                print("O campo precisa ser preenchido!")
                aguardar(3)
                limpar_tela()
                continue 
            elif not email_valido(email_cadastro):
                print("Email não é válido!")
                aguardar(3)
                limpar_tela()
                continue
            else:
                print(f"Email cadastrado! {email_cadastro}")
                break 

    aguardar(3)
    limpar_tela()

    ############################################## CADASTRO (CRIAÇÃO DE SENHA) ##############################################  

    while 1>0:
            senha_cadastro=input("Crie uma senha de acesso: ").strip()

            if not senha_cadastro:
                print("O campo precisa ser preenchido!")
                aguardar(3)
                limpar_tela()
                continue 

            elif not any(char.isalpha() for char in senha_cadastro) or not any(char.isdigit() for char in senha_cadastro):
                print("\nA senha deve conter letras e números!\n")
                aguardar(3)
                limpar_tela()
                continue

            elif not any(char.isupper() for char in senha_cadastro) or not any(char.islower() for char in senha_cadastro):
                print("\nA senha precisa conter letra maiúscula e minúscula! ")
                aguardar(3)
                limpar_tela()
                continue

            elif not any(char in caracteres_especiais for char in senha_cadastro):
                print("A senha precisa de caractere especial")
                aguardar(3)
                limpar_tela()
                continue

            elif len(senha_cadastro)<8 or len(senha_cadastro)>12:
                print("A senha deve conter de 8 a 12 caracteres! ")
                aguardar(3)
                limpar_tela()
                continue 

            else:
                print("Senha cadastrada!")
                break 
        
    aguardar(3)
    limpar_tela()

    ############################################## CADASTRO (CONFIRMAÇÃO DA SENHA) ##############################################  

    while 1>0:
            senha_cadastro1= input("Confirme sua senha de acesso: ")
            if not senha_cadastro1:
                print("O campo precisa ser preenchido! \n")
                aguardar(3)
                limpar_tela()
                continue
            elif not senha_cadastro==senha_cadastro1:
                print("A senha não confere! ")
                aguardar(3)
                limpar_tela()
                continue
            else:
                print("Senha cadastrada!\n")
                break

    aguardar(3)
    limpar_tela()

    ############################################## ENVIO DE EMAIL (JUNTO COM O CÓDIGO DE VERIFICAÇÃO) ##############################################  

    codigo=code_verificação()
    remetente="hivestock.logistica@gmail.com"
    destinatario={email_cadastro}
    assunto_email="Código de verificação"
    mensagem_email=f"""
    Olá, {nome_cadastro}! Seja Bem-vindo a HiveStock!
    A HiveStock é uma aplicação que visa a eficiência e melhora nos processos de estoque e logística!
        O seu código de verificação foi:
                {codigo}

    """
    senha_email="inzq mgbn hhdz ewqg"

    msg=EmailMessage()
    msg['From']=remetente
    msg['To']=destinatario
    msg['Subject']=assunto_email
    msg.set_content(mensagem_email)

    with smtplib.SMTP_SSL("SMTP.gmail.com",465) as email:
        email.login(remetente,senha_email)
        email.send_message(msg)

    print("Email de verificação enviado! ")

    ############################################## CONFIRMAÇÃO DE VERIFICAÇÃO ##############################################

    tentativas=3
    while tentativas>0:
        verificacao_usuario=input("Qual o código de verificação? ")
        if verificacao_usuario==codigo:
            print("Verificação concluída!")
            break
        else:
            print("Código incorreto!")
            tentativas-=1
            continue
        
        if tentativas==0:
            print("Falha na verificação!")
            sys.exit()

    ############################################## SALVANDO DADOS NO JSON #############################################################

    while 1>0:
        menu_usuario()
        tipo_usuário = input("Qual o seu tipo de usuário? ")
        
        if tipo_usuário not in possibilidades_cadastro:
            print("Valor não é válido! ")
            continue

        # Cria dicionário do usuário
        usuario = {
            "nome": nome_cadastro,
            "matricula": matricula_cadastro,
            "email": email_cadastro,
            "senha": senha_cadastro
        }

        # Define o arquivo JSON correto
        if tipo_usuário == "1":
            arquivo_json = "dados_ADM.json"
        elif tipo_usuário == "2":
            arquivo_json = "dados_FUNCIONARIO.json"

        # Carrega dados do JSON ou cria vazio se não existir
        if os.path.exists(arquivo_json):
            with open(arquivo_json, "r") as f:
                try:
                    dados = json.load(f)
                except json.JSONDecodeError:
                    dados = {}
        else:
            dados = {}

        
        if "usuarios" not in dados:
            dados["usuarios"] = []

        
        duplicado = False
        for u in dados["usuarios"]:
            if u.get("email") == usuario["email"] or u.get("matricula") == usuario["matricula"]:
                duplicado = True
                break

        if duplicado:
            print("⚠️ Usuário já cadastrado! (email ou matrícula já existem)")
            aguardar(3)
            limpar_tela()
            sys.exit()  # ou return se quiser voltar ao menu
        else:
            # Adiciona o usuário
            dados["usuarios"].append(usuario)

            # Salva no JSON
            with open(arquivo_json, "w") as f:
                json.dump(dados, f, indent=4)

            print("✅ Cadastro salvo com sucesso!")
            aguardar(3)
            limpar_tela()
            break


    

        




