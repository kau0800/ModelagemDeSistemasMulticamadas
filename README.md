# Exercício 2 — Arquitetura Multicamadas (Python)

Sistema bancário com cadastro, consulta, depósito, saque e histórico. A camada de negócio valida as regras e a camada de dados mantém as contas em memória.

## Executar
Requer Python 3.10 ou superior. Não precisa instalar dependências.

```bash
python main.py
```

## Camadas
- `presentation/`: interface de terminal.
- `business/`: regras e validações bancárias.
- `data/`: armazenamento em memória.
- `domain/`: entidades Cliente, Conta e Movimentacao.

O armazenamento é em memória; os dados são perdidos ao fechar o programa.
