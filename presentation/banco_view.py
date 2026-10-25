class BancoView:
    def __init__(self, service):
        self.service = service

    def executar(self):
        while True:
            print("\n=== SISTEMA BANCÁRIO — MULTICAMADAS ===")
            print("1. Criar conta")
            print("2. Consultar conta")
            print("3. Depositar")
            print("4. Sacar")
            print("5. Ver histórico")
            print("0. Sair")
            opcao = input("Escolha: ").strip()
            try:
                if opcao == "1":
                    nome = input("Nome: ")
                    cpf = input("CPF: ")
                    saldo = self._ler_valor("Saldo inicial: R$ ")
                    conta = self.service.criar_conta(nome, cpf, saldo)
                    self._mostrar_conta(conta)
                elif opcao == "2":
                    conta = self.service.buscar_conta(self._ler_numero())
                    if conta:
                        self._mostrar_conta(conta)
                    else:
                        print("Conta não encontrada.")
                elif opcao == "3":
                    conta = self.service.depositar(self._ler_numero(), self._ler_valor("Valor do depósito: R$ "))
                    self._mostrar_conta(conta)
                elif opcao == "4":
                    conta = self.service.sacar(self._ler_numero(), self._ler_valor("Valor do saque: R$ "))
                    self._mostrar_conta(conta)
                elif opcao == "5":
                    conta = self.service.buscar_conta(self._ler_numero())
                    if not conta:
                        print("Conta não encontrada.")
                    elif not conta.historico:
                        print("Ainda não há movimentações.")
                    else:
                        print("\n--- HISTÓRICO ---")
                        for mov in conta.historico:
                            print(mov)
                elif opcao == "0":
                    print("Até logo!")
                    return
                else:
                    print("Opção inválida.")
            except ValueError as erro:
                print(f"Erro: {erro}")

    @staticmethod
    def _ler_numero():
        return int(input("Número da conta: "))

    @staticmethod
    def _ler_valor(prompt):
        return float(input(prompt).replace(",", "."))

    @staticmethod
    def _mostrar_conta(conta):
        print(f"\nConta: {conta.numero}")
        print(f"Cliente: {conta.cliente.nome}")
        print(f"CPF: {conta.cliente.cpf}")
        print(f"Saldo: R$ {conta.saldo:.2f}")
