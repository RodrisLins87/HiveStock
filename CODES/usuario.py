class Usuario:
    def __init__(self,nome_cadastro,matricula_cadastro,estratificacao,email_cadastro,senha_cadastro):
        self.nome_cadastro=nome_cadastro
        self.matricula_cadastro=matricula_cadastro
        self.estratificacao=estratificacao
        self.email_cadastro=email_cadastro
        self.senha_cadastro=senha_cadastro

    def to_dict(self):
        return{
            "nome": self.nome_cadastro,
            "matricula": self.matricula_cadastro,
            "estratificacao": self.estratificacao,
            "email": self.email_cadastro,
            "senha":self.senha_cadastro
        }
    
    