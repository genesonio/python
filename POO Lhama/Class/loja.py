class Loja:

    tarifa = 1.03

    def __init__(self, adress: str) -> None:
        self.__endereço = adress

    def show_adress(self) -> None:
        print(self.__endereço)

    @classmethod  # Decorador
    def sell(cls) -> float:
        return 40 * cls.tarifa

    @classmethod
    def alterar_tarifa(cls, nova_tar: float) -> None:
        cls.tarifa = nova_tar


loja_praia = Loja('Praia')
loja_centro = Loja('Centro')

loja_praia.show_adress()

print(loja_praia.sell())
print(loja_centro.sell())

loja_centro.alterar_tarifa(1.5)

print(loja_praia.sell())
print(loja_centro.sell())
