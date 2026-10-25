from data.banco_repository import BancoRepository
from business.banco_service import BancoService
from presentation.banco_view import BancoView


def main():
    service = BancoService(BancoRepository())
    view = BancoView(service)
    view.executar()


if __name__ == "__main__":
    main()
