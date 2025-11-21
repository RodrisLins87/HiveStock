import os
import time

aguardar = time.sleep 

def limpar_tela():
    """Limpa o terminal a cada instante que foi determinado"""
    if os.name == 'nt': 
        os.system('cls')
    else:  
        os.system('clear')

        