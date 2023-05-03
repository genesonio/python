from produto import Produto
from typing import Type


class Carrinho:

    def __init__(self) -> None:
        self.__produtos = []

    def adicionar_produto(self, produto: Type[Produto]) -> None:
        self.__produtos.append(produto)

    def finalizar(self) -> None:
        print('Compras Finalizadas')

        for prod in self.__produtos:
            prod.inf_prod()
