from typing import Type
from interfaces.formas import FormasInterface


class Engenheiro:

    def __init__(self, nome: str) -> None:
        self.nome = nome

    def medir_perimetro(self, terreno: Type[FormasInterface]) -> None:
        perimetro = terreno.get_perimetro()
        print(f'{self.nome} mediu o perímetro: {perimetro}m')

    def medir_area(self, terreno: Type[FormasInterface]) -> None:
        area = terreno.get_area()
        print(f'{self.nome} mediu o area: {area}m')
