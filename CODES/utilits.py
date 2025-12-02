import os
import time

aguardar = time.sleep 

def limpar_tela():
    """Limpa o terminal a cada instante que foi determinado"""
    if os.name == 'nt': 
        os.system('cls')
    else:  
        os.system('clear')

# Pega a pasta onde o arquivo está (CODES/)
PASTA_ATUAL = os.path.dirname(os.path.abspath(__file__))

# Vai para a raiz do projeto
ROOT = os.path.dirname(PASTA_ATUAL)

# Pasta Arquivos_JSON
PASTA_JSON = os.path.join(ROOT, "Arquivos_JSON")

# Caminho final do arquivo
arquivo = os.path.join(PASTA_JSON, "estoque.json")

arquivo_mov = os.path.join(PASTA_JSON, "movimentacao.json")