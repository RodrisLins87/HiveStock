import json
import os
import re
from CODES.utilits import aguardar, limpar_tela

caracteres_especiais = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', ',', '.', '?', ':', '"', '{', '}', '|', '<', '>']

def email_valido(email):
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(padrao, email))

def validar_senha(senha):
    if len(senha) < 8 or len(senha) > 12:
        return False
    if not any(c.isupper() for c in senha):
        return False
    if not any(c.islower() for c in senha):
        return False
    if not any(c.isdigit() for c in senha):
        return False
    if not any(c in caracteres_especiais for c in senha):
        return False
    return True

def validar_nome(nome):
    return nome.strip() != "" and all(c.isalpha() or c.isspace() for c in nome)

def escolher_bloco():
    while True:
        print("\nSelecione seu bloco/setor:")
        print("[1] DEFS\n[2] DEINFO\n[3] REITORIA\n[4] DEPARTAMENTO DE COMPUTAÇÃO\n[5] OUTRO\n[6] CANCELAR")
        opcoes = ["1", "2", "3", "4", "5", "6"]
        escolha = input("Escolha a opção:").strip()
        if escolha not in opcoes:
            print("Opção inválida!")
            aguardar(2)
            limpar_tela()
            continue
        if escolha == "1":
            return "DEFS"
        elif escolha == "2":
            return "DEINFO"
        elif escolha == "3":
            return "REITORIA"
        elif escolha == "4":
            return "DEPARTAMENTO DE COMPUTAÇÃO"
        elif escolha == "5":
            novo = input("Digite o nome do bloco/setor: ").strip()
            if novo == "":
                print("Bloco/Setor não pode ficar vazio!")
                aguardar(2)
                limpar_tela()
                continue
            return novo
        elif escolha == "6":
            return None  # cancela a alteração do bloco

def editar_adm(usuario_encontrado):
    arquivo_json = os.path.join("Arquivos_JSON", "dados_ADM.json")
    
    while True:
        print("\nSeus dados atuais:")
        for k, v in usuario_encontrado.items():
            print(f"{k}: {v}")
            
        print("\nDigite o campo que deseja alterar (ou '0' para sair):")
        print("[1] Nome\n[2] Matrícula\n[3] Email\n[4] Senha\n[5] Bloco/Setor\n[0] Sair")
        opcao = input("Opção: ").strip()
        
        if opcao == "0":
            print("Saindo da edição...")
            break
        elif opcao == "1":
            novo = input("Novo nome: ").strip()
            if not validar_nome(novo):
                print("Nome inválido! Apenas letras e espaços, não pode ficar vazio.")
                aguardar(2)
                limpar_tela()
                continue
            usuario_encontrado["nome"] = novo
        elif opcao == "2":
            novo = input("Nova matrícula: ").strip()
            if not (novo.isdigit() and len(novo) == 11):
                print("Matrícula inválida! Deve ter 11 números.")
                aguardar(2)
                limpar_tela()
                continue
            usuario_encontrado["matricula"] = novo
        elif opcao == "3":
            novo = input("Novo email: ").strip()
            if not email_valido(novo):
                print("Email inválido!")
                aguardar(2)
                limpar_tela()
                continue
            usuario_encontrado["email"] = novo
        elif opcao == "4":
            novo = input("Nova senha: ").strip()
            if not validar_senha(novo):
                print("Senha inválida! Deve ter maiúscula, minúscula, número, caractere especial e 8-12 caracteres.")
                aguardar(2)
                limpar_tela()
                continue
            usuario_encontrado["senha"] = novo
        elif opcao == "5":
            novo = escolher_bloco()
            if novo is None:
                print("Alteração do bloco cancelada.")
                aguardar(2)
                limpar_tela()
                continue
            usuario_encontrado["bloco/setor"] = novo
        else:
            print("Opção inválida!")
            aguardar(2)
            limpar_tela()
            continue
        
        # Atualiza JSON
        if os.path.exists(arquivo_json):
            with open(arquivo_json, "r") as f:
                try:
                    dados = json.load(f)
                except json.JSONDecodeError:
                    dados = {"usuarios": []}
        else:
            dados = {"usuarios": []}
            
        for i, u in enumerate(dados.get("usuarios", [])):
            if u.get("matricula") == usuario_encontrado.get("matricula"):
                dados["usuarios"][i] = usuario_encontrado
                break
        
        with open(arquivo_json, "w") as f:
            json.dump(dados, f, indent=4)
        
        print("✅ Dados atualizados com sucesso!")
        aguardar(2)
        limpar_tela()


def editar_funcionario(usuario_encontrado):
    arquivo_json = os.path.join("Arquivos_JSON", "dados_FUNCIONARIO.json")
    
    while True:
        print("\nSeus dados atuais:")
        for k, v in usuario_encontrado.items():
            print(f"{k}: {v}")
            
        print("\nDigite o campo que deseja alterar (ou '0' para sair):")
        print("[1] Nome\n[2] Matrícula\n[3] Email\n[4] Senha\n[5] Bloco/Setor\n[0] Sair")
        opcao = input("Opção: ").strip()
        
        if opcao == "0":
            print("Saindo da edição...")
            break
        elif opcao == "1":
            novo = input("Novo nome: ").strip()
            if not validar_nome(novo):
                print("Nome inválido! Apenas letras e espaços, não pode ficar vazio.")
                aguardar(2)
                limpar_tela()
                continue
            usuario_encontrado["nome"] = novo
        elif opcao == "2":
            novo = input("Nova matrícula: ").strip()
            if not (novo.isdigit() and len(novo) == 11):
                print("Matrícula inválida! Deve ter 11 números.")
                aguardar(2)
                limpar_tela()
                continue
            usuario_encontrado["matricula"] = novo
        elif opcao == "3":
            novo = input("Novo email: ").strip()
            if not email_valido(novo):
                print("Email inválido!")
                aguardar(2)
                limpar_tela()
                continue
            usuario_encontrado["email"] = novo
        elif opcao == "4":
            novo = input("Nova senha: ").strip()
            if not validar_senha(novo):
                print("Senha inválida! Deve ter maiúscula, minúscula, número, caractere especial e 8-12 caracteres.")
                aguardar(2)
                limpar_tela()
                continue
            usuario_encontrado["senha"] = novo
        elif opcao == "5":
            novo = escolher_bloco()
            if novo is None:
                print("Alteração do bloco cancelada.")
                aguardar(2)
                limpar_tela()
                continue
            usuario_encontrado["bloco/setor"] = novo
        else:
            print("Opção inválida!")
            aguardar(2)
            limpar_tela()
            continue
        
        # Atualiza JSON
        if os.path.exists(arquivo_json):
            with open(arquivo_json, "r") as f:
                try:
                    dados = json.load(f)
                except json.JSONDecodeError:
                    dados = {"usuarios": []}
        else:
            dados = {"usuarios": []}
            
        for i, u in enumerate(dados.get("usuarios", [])):
            if u.get("matricula") == usuario_encontrado.get("matricula"):
                dados["usuarios"][i] = usuario_encontrado
                break
        
        with open(arquivo_json, "w") as f:
            json.dump(dados, f, indent=4)
        
        print("✅ Dados atualizados com sucesso!")
        aguardar(2)
        limpar_tela()
