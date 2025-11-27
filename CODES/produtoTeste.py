# ============================================
#   CLASSE PRODUTO
# ============================================

class Produto:
    def __init__(self, codigo, nome, categoria, quantidade, nf, data, mes_ano):
        self.codigo = codigo
        self.nome = nome
        self.categoria = categoria
        self.quantidade = quantidade
        self.nf = nf
        self.data = data
        self.mes_ano = mes_ano

    def to_dict(self):
        return {
            "codigo": self.codigo,
            "nome": self.nome,
            "categoria": self.categoria,
            "quantidade": self.quantidade,
            "nf": self.nf,
            "data": self.data,
            "mes_ano": self.mes_ano
        }
