from typing import Type

# Princípio de Liskov -> Genérico em cima, específico embaixo.


class Animal:

    def comer(self) -> None:
        print('O animal está comendo')

    def dormir(self) -> None:
        print('O animal está dormindo')

    def andar(self) -> None:
        print('O animal está andando')


class Aves(Animal):

    def __init__(self) -> None:
        super().__init__()

    def cantar(self) -> None:
        print('A ave está cantando')


class Pinguim(Aves):

    def __init__(self) -> None:
        super().__init__()

    def escorregar(self) -> None:
        print('O pinguim está escorregando no gelo')


class Pessoa:

    def observar(self, animal: Type[Animal]):
        animal.cantar()


roberto = Pessoa()
pinguim = Aves()

roberto.observar(pinguim)
