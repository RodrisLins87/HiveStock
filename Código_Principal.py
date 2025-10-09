import os
import time
import json
from funções import cancelar_voltar

import smtplib
from email.message import EmailMessage
import mimetypes


aguardar = time.sleep

def limpar_tela():
    """Limpa o terminal a cada instante t"""
    if os.name == 'nt': 
        os.system('cls')
    else:  
        os.system('clear')
def menu():
    print("\n Bem-Vindo a HiveStock \n")

    print("[1] Criar Cadastro")
    print("[2] LOGIN")
    print("[3] Recuperar Acesso")
    print("[4] Sair \n")

menu()

escolhas_login= [1,2,3,4] 
caracteres_especiais = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', ',', '.', '?', ':', '"', '{', '}', '|', '<', '>']

while 1>0:
    try:
        entrada_1 = int(input("Selecione o que deseja: "))
        if entrada_1 not in escolhas_login:
            print("Valor não confere! Tente novamente.\n")
            aguardar(3)
            limpar_tela()
            menu()
          
        else:
            break

    except ValueError:
        print("Valor não confere. Tente novamente! \n") 
        aguardar(3)
        limpar_tela()
        menu()
           

if entrada_1==1:

    print("Vamos criar seu cadastro!")
    aguardar(3)
    limpar_tela()

    while 1>0:

        nome_cadastro=input("Qual o seu nome completo? ").strip()
        if not nome_cadastro:
            print("O campo tem que ser preenchido!")
            aguardar(3)
            limpar_tela()
            continue
            
        elif all(char.isalpha() or char.isspace() for char in nome_cadastro):
            print("Nome cadastrado!")
            break 
        else:
            print("Nome inválido!")
            aguardar(3)
            limpar_tela()
           
          
    aguardar(3)
    limpar_tela()

    while 1>0:

        cpf_cadastro=input("Informe o seu CPF: ").strip()
        if not cpf_cadastro:
            print("O campo precisa ser preenchido")
            aguardar(3)
            limpar_tela()
            continue
        elif not cpf_cadastro.isdigit():
            print("Digite só números. Sem espaços e pontos!")
            aguardar(3)
            limpar_tela()
            continue
        elif not len(cpf_cadastro)==11:
            print("CPF não confere!")
            aguardar(3)
            limpar_tela()
            continue
        else:
            print(f"CPF cadastrado! {cpf_cadastro} ")
            break

    aguardar(3)
    limpar_tela()
    
    while 1>0:
        matricula_cadastro=input("Qual a sua matrícula? ").strip()

        if not matricula_cadastro:
            print("O campo precisa ser preenchido!")
            aguardar(3)
            limpar_tela()
            continue

        elif not len(matricula_cadastro)==10:
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
    
    while 1>0:
        email_cadastro=input("Qual o seu email? ")
        if not email_cadastro:
            print("O campo precisa ser preenchido!")
            aguardar(3)
            limpar_tela()
            continue 
        else:
            print(f"Email cadastrado! {email_cadastro}")
            break 

    aguardar(3)
    limpar_tela()

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
 
        


