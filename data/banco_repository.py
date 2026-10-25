class BancoRepository:
    def __init__(self):
        self._contas = {}

    def salvar(self, conta):
        self._contas[conta.numero] = conta

    def buscar(self, numero):
        return self._contas.get(numero)

    def listar(self):
        return list(self._contas.values())
