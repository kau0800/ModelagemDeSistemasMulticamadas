from datetime import datetime


class Movimentacao:
    def __init__(self, tipo, valor, saldo_apos):
        self.tipo = tipo
        self.valor = float(valor)
        self.saldo_apos = float(saldo_apos)
        self.data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def __str__(self):
        return (f"{self.data} | {self.tipo} | R$ {self.valor:.2f} "
                f"| Saldo após operação: R$ {self.saldo_apos:.2f}")
