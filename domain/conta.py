from domain.movimentacao import Movimentacao


class Conta:
    _proximo_numero = 1

    def __init__(self, cliente, saldo_inicial):
        if saldo_inicial < 0:
            raise ValueError("O saldo inicial não pode ser negativo.")
        self.numero = Conta._proximo_numero
        Conta._proximo_numero += 1
        self.cliente = cliente
        self.saldo = float(saldo_inicial)
        self.historico = []
        if saldo_inicial > 0:
            self.historico.append(Movimentacao("Depósito inicial", saldo_inicial, self.saldo))

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("O depósito deve ser maior que zero.")
        self.saldo += valor
        self.historico.append(Movimentacao("Depósito", valor, self.saldo))

    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("O saque deve ser maior que zero.")
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente.")
        self.saldo -= valor
        self.historico.append(Movimentacao("Saque", valor, self.saldo))
