############################################## IMPORTAÇÕES DAS BIBLIOTECAS ##############################################

import os
import time
import json
import re
import random
import sys
from CODES.utilits import aguardar,limpar_tela
import smtplib
from email.message import EmailMessage
import mimetypes
from CODES.usuario import Usuario

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
                
            elif all(char.isalpha() or char.isspace() for char in nome_cadastro): #GARANTE QUE O NOME SÓ TENHA LETRAS E ESPAÇÕES
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
                print("Matrícula não confere. Tem que ter:\n1-11 caracteres\n2-Não conter espaçoes\n3-Não conter Letras ou Caracteres Especiais\n.")
                aguardar(3)
                limpar_tela()
                continue

            elif not matricula_cadastro.isdigit():
                print("Matrícula não confere. Tem que ter:\n1-11 caracteres\n2-Não conter espaçoes\n3-Não conter Letras ou Caracteres Especiais\n.")
                aguardar(3)
                limpar_tela()
                continue

            else:
                print(f"A matrícula {matricula_cadastro} foi cadastrada!")
                break 

    aguardar(3)
    limpar_tela()
    
    ############################################## SETOR (BLOCO) ############################################################
    while 1>0:
        print("[1]DEFS\n[2]DEINFO\n[3]REITORIA\n[4]DEPARTAMENTO DE COMPUTAÇÃO\n[5]OUTRO\n")
        opcoes_estratificacao=["1","2","3","4","5"]
        estratificacao=input("Qual o blocos/setor que você atua? ")
        if not estratificacao in opcoes_estratificacao:
            print("Valor não é válido!")
            continue
        elif estratificacao=="1":
            estratificacao1="DEFS"
            break
        elif estratificacao=="2":
            estratificacao1="DEINFO"
            break
        elif estratificacao=="3":
            estratificacao1="REITORIA"
            break
        elif estratificacao=="4":
            estratificacao1="DEPARTAMENTO DE COMPUTAÇÃO"
            break
        elif estratificacao=="5":
            estratificacao1=input("Qual o nome do bloco/setor?")
            break
        
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
                print("\nA senha deve conter:\n1- Letra Maiúscula\n2-Letra Minúscula\n3-Número\n4-Caractere Especial\n5-Conter de 8 a 12 caracters\n")
                aguardar(3)
                limpar_tela()
                continue

            elif not any(char.isupper() for char in senha_cadastro) or not any(char.islower() for char in senha_cadastro):
                print("\nA senha deve conter:\n1- Letra Maiúscula\n2-Letra Minúscula\n3-Número\n4-Caractere Especial\n5-Conter de 8 a 12 caracters\n")
                aguardar(3)
                limpar_tela()
                continue

            elif not any(char in caracteres_especiais for char in senha_cadastro):
                print("\nA senha deve conter:\n1- Letra Maiúscula\n2-Letra Minúscula\n3-Número\n4-Caractere Especial\n5-Conter de 8 a 12 caracters\n")
                aguardar(3)
                limpar_tela()
                continue

            elif len(senha_cadastro)<8 or len(senha_cadastro)>12:
                print("\nA senha deve conter:\n1- Letra Maiúscula\n2-Letra Minúscula\n3-Número\n4-Caractere Especial\n5-Conter de 8 a 12 caracters\n")
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
                print("Digite 0 para sair")
                aguardar(3)
                limpar_tela()

            elif senha_cadastro1=="0":
                print("Saindo...")
                aguardar(3)
                limpar_tela()
                return
            
            elif not senha_cadastro==senha_cadastro1:
                print("A senha não confere! ")
                print("Digite 0 para sair")
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
            
    usuario= Usuario(nome_cadastro, matricula_cadastro, estratificacao, email_cadastro, senha_cadastro).to_dict()
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
            "senha": senha_cadastro,
            "bloco/setor": estratificacao1
        }

        # Define o arquivo JSON correto
        if tipo_usuário == "1":
            arquivo_json = os.path.join("Arquivos_JSON", "dados_ADM.json")
        elif tipo_usuário == "2":
            arquivo_json = os.path.join("Arquivos_JSON", "dados_FUNCIONARIO.json")

        

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


    

        




