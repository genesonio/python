from typing import Type


class Interruptor:

    def __init__(self, comodo) -> None:
        self.__comodo = comodo

    def acender(self) -> None:
        print(f'Acendendo {self.__comodo}')

    def apagar(self) -> None:
        print(f'Apagando {self.__comodo}')


class Pessoa:

    def acender_luz(self, interruptor: Type[Interruptor]) -> None:
        interruptor.acender()

    def apagar_luz(self, interruptor: Type[Interruptor]) -> None:
        interruptor.apagar()

    def dormir(self) -> None:
        print('Dormindo...')


genesio = Pessoa()
interruptor_quarto = Interruptor('quarto')
interruptor_cozinha = Interruptor('cozinha')

interruptor_quarto.acender()  # Chamada direta
genesio.acender_luz(interruptor_cozinha)  # Chamada indireta
