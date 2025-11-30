import json 
import sys 
from CODES.cadastrar import email_valido
from CODES.cadastrar import limpar_tela
from CODES.cadastrar import code_verificação
from CODES.utilits import limpar_tela
from CODES.utilits import aguardar
import smtplib
from email.message import EmailMessage
import mimetypes

SIM_NAO=["1","2"]
caracteres_especiais = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', ',', '.', '?', ':', '"', '{', '}', '|', '<', '>']

ARQUIVO_JSON1 = "dados_FUNCIONARIO.json"

def buscar_usuario_por_email(email):
    try:
        with open(ARQUIVO_JSON1, "r", encoding="utf-8") as f:
            dados = json.load(f)
            usuarios = dados["usuarios"]  # acessa a lista dentro da chave
    except FileNotFoundError:
        print("Nenhum usuário cadastrado ainda.")
        return None

    for usuario in usuarios:
        # ignora dicionários vazios
        if not usuario or "email" not in usuario:
            continue

        if usuario["email"] == email:
            return usuario

    return None

def recuperar_senha():
    print("Vamos recuperar o seu acesso!\n")
    while 1>0:
        email_recuperacao=input("Qual informe o email cadastrado? ")
        if not email_recuperacao:
            print("O campo precisa ser preenchido\n")
            aguardar(2)
            limpar_tela()
            continue
        elif not email_valido(email_recuperacao):
            print("Email não é válido!")
            aguardar(2)
            limpar_tela()
            continue

        elif not buscar_usuario_por_email(email_recuperacao):
            print("Email não cadastrado!")
            aguardar(2)
            limpar_tela
            break
        
        else:
            
            codigo=code_verificação()
            remetente="hivestock.logistica@gmail.com"
            destinatario={email_recuperacao}
            assunto_email="Código de verificação"
            mensagem_email=f"""
            Olá, Seja Bem-vindo a HiveStock!
                O seu código de recuperação é :
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

            print("Email de recuperação enviado! ")
            tentativas2=3
            while tentativas2>0:
                

                codigo_recuperação=input("Qual o seu código de recuperação? ")
                if codigo_recuperação!=codigo:
                    tentativas2-=1
                    print("Código Inválido")
                    print(f"Número de tentativas restantes: {tentativas2}")
                    aguardar(2)
                    limpar_tela
                    continue

                else: 
                    print("Código válido")
                    aguardar(3)
                    limpar_tela()
                    while 1>0:
                        nova_senha=input("Qual a nova senha? ").strip()
                        if not nova_senha:
                            print("O campo precisa ser preenchido!")
                            aguardar(3)
                            limpar_tela()
                            continue 

                        elif not any(char.isalpha() for char in nova_senha) or not any(char.isdigit() for char in nova_senha):
                            print("\nA senha deve conter letras e números!\n")
                            aguardar(3)
                            limpar_tela()
                            continue

                        elif not any(char.isupper() for char in nova_senha) or not any(char.islower() for char in nova_senha):
                            print("\nA senha precisa conter letra maiúscula e minúscula! ")
                            aguardar(3)
                            limpar_tela()
                            continue

                        elif not any(char in caracteres_especiais for char in nova_senha):
                            print("A senha precisa de caractere especial")
                            aguardar(3)
                            limpar_tela()
                            continue

                        elif len(nova_senha)<8 or len(nova_senha)>12:
                            print("A senha deve conter de 8 a 12 caracteres! ")
                            aguardar(3)
                            limpar_tela()
                            continue 

                        else:
                             # Abre o arquivo e carrega todos os usuários
                            with open(ARQUIVO_JSON1, "r", encoding="utf-8") as f:
                                dados = json.load(f)
                                usuarios = dados["usuarios"]

                            # Procura o usuário correspondente ao e-mail
                            for usuario in usuarios:
                                if usuario.get("email") == email_recuperacao:
                                    usuario["senha"] = nova_senha
                                    break

                            # Salva novamente o JSON atualizado
                            with open(ARQUIVO_JSON1, "w", encoding="utf-8") as f:
                                json.dump(dados, f, indent=4, ensure_ascii=False)

                            print("Senha atualizada com sucesso!")
                            aguardar(2)
                            limpar_tela()
                            return




        

    