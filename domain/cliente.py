class Cliente:
    def __init__(self, nome, cpf):
        if not nome.strip() or not cpf.strip():
            raise ValueError("Nome e CPF são obrigatórios.")
        self.nome = nome.strip()
        self.cpf = cpf.strip()
