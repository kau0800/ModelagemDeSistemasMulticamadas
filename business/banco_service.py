from domain.cliente import Cliente
from domain.conta import Conta


class BancoService:
    def __init__(self, repository):
        self.repository = repository

    def criar_conta(self, nome, cpf, saldo_inicial):
        cliente = Cliente(nome, cpf)
        conta = Conta(cliente, saldo_inicial)
        self.repository.salvar(conta)
        return conta

    def buscar_conta(self, numero):
        return self.repository.buscar(numero)

    def depositar(self, numero, valor):
        conta = self._obter_conta(numero)
        conta.depositar(valor)
        self.repository.salvar(conta)
        return conta

    def sacar(self, numero, valor):
        conta = self._obter_conta(numero)
        conta.sacar(valor)
        self.repository.salvar(conta)
        return conta

    def _obter_conta(self, numero):
        conta = self.repository.buscar(numero)
        if conta is None:
            raise ValueError("Conta não encontrada.")
        return conta
