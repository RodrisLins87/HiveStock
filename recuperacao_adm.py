import json #biblioteca para gerenciar dados no Json 
import sys #bibilioteca de sistema, utilizada comumente para fechar totalmente o programa
from cadastrar import email_valido #Importação da função declarada 
from utilits import limpar_tela #Importação da função declarada 
from cadastrar import code_verificação #Importação da função declarada 
from cadastrar import limpar_tela #Importação da função declarada 
from utilits import aguardar #Importação da função declarada 
import smtplib #Biblioteca para enviar email (conectar a servido e automatizar )
from email.message import EmailMessage #biblioteca para criar a estrutura de texto 
import mimetypes #biblioteca para gerenciar o tipo de arquivo, caso queira anexá-lo em uma mensagem de email 


# Listas para determinar as possibilidades, uma trativa de erro, para restringir as escolhas do usuário 

SIM_NAO=["1","2"] 
caracteres_especiais = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', ',', '.', '?', ':', '"', '{', '}', '|', '<', '>']

ARQUIVO_JSON2 = "dados_ADM.json" #Cria uma variável, e nomeia com o nome do arquivo jsopn que vai ser utilizado 

def buscar_usuario_por_email_ADM(email):
    try:
        with open(ARQUIVO_JSON2, "r", encoding="utf-8") as f: #Abre e fecha o arquivo Json em modo leitura
            dados = json.load(f) #Lê o arquivo modo objetos, ou seja, carrega os dados do arquivo 
            usuarios = dados["usuarios"]  

    except FileNotFoundError: #Exceção, caso não exista nenhum usuário cadastrado ainda
        print("Nenhum usuário cadastrado ainda.")
        return None

    for usuario in usuarios: # Percorre o dicionário, e é nesse bloco que o retorno vai depender de existir ou não um usuário cadastrado 
        
        if not usuario or "email" not in usuario:
            continue

        if usuario["email"] == email:
            return usuario

    return None

def recuperar_senha_ADM(): 
    """Função para recuperar a senha do usuário administrativo"""
    print("Vamos recuperar o seu acesso!\n")
    while 1>0: #Cria um loop, que só quebra com o alcançe de determinada condição

        email_recuperacao=input("Qual informe o email cadastrado? ")
        if not email_recuperacao: #Esse bloco garante que o espaço seja preenchido 
            print("O campo precisa ser preenchido\n")
            aguardar(2)
            limpar_tela()
            continue
        elif not email_valido(email_recuperacao): #Com o auxilio da biblioteca re, ele verifica se a estrutura condiz com a de um email 
            print("Email não é válido!") 
            aguardar(2)
            limpar_tela()
            continue

        elif not buscar_usuario_por_email_ADM(email_recuperacao): #Busca o email no arquivo Json, caso não ache, ele quebra o loop 
            print("Email não cadastrado!")
            aguardar(2)
            limpar_tela
            break
        
        else: #Caso tudo anteriormente seja atendido, ele continua para verificação 
            
            codigo=code_verificação() #função declarada com o auxilio da biblioteca random 
            remetente="hivestock.logistica@gmail.com" 
            destinatario={email_recuperacao}
            assunto_email="Código de verificação"
            mensagem_email=f""" 
            Olá, Seja Bem-vindo a HiveStock!
                O seu código de recuperação é :
                        {codigo}

            """
            #mensagem que 
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
                            with open(ARQUIVO_JSON2, "r", encoding="utf-8") as f:
                                dados = json.load(f)
                                usuarios = dados["usuarios"]

                            # Procura o usuário correspondente ao e-mail
                            for usuario in usuarios:
                                if usuario.get("email") == email_recuperacao:
                                    usuario["senha"] = nova_senha
                                    break

                            # Salva novamente o JSON atualizado
                            with open(ARQUIVO_JSON2, "w", encoding="utf-8") as f:
                                json.dump(dados, f, indent=4, ensure_ascii=False)

                            print("Senha atualizada com sucesso!")
                            aguardar(2)
                            limpar_tela()
                            return



        

          


    